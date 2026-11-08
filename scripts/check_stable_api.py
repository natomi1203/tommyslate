#!/usr/bin/env python3
"""Build and verify TommySlate's frozen 1.x API contract."""

from __future__ import annotations

import argparse
import ast
from dataclasses import MISSING, fields, is_dataclass
import inspect
import json
from pathlib import Path
from textwrap import dedent
from typing import Any

import safe_slate


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "library.json"
SNAPSHOT_PATH = ROOT / "docs" / "stable-api-v1.json"


def _annotation(value: object) -> str:
    return value if isinstance(value, str) else inspect.formatannotation(value)


def _native_stub_declarations() -> dict[str, str]:
    path = ROOT / "python" / "safe_slate" / "_core.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = {"optimize_slate", "optimize_replacements"}
    return {
        node.name: " ".join(ast.unparse(node).split())
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in names
    }


def _callable_contract(
    value: object, *, stub_declaration: str | None = None
) -> dict[str, object]:
    contract: dict[str, object] = {"signature": str(inspect.signature(value))}
    annotations = inspect.get_annotations(value, eval_str=False)
    if annotations:
        contract["annotations"] = {
            name: _annotation(annotation) for name, annotation in annotations.items()
        }
    if stub_declaration is not None:
        contract["stub_declaration"] = stub_declaration
    return contract


def _to_dict_keys(value: type[object]) -> list[str]:
    method = getattr(value, "to_dict", None)
    if method is None:
        return []
    tree = ast.parse(dedent(inspect.getsource(method)))
    candidates: list[list[str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [
            key.value
            for key in node.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)
        ]
        if keys:
            candidates.append(keys)
    return max(candidates, key=len, default=[])


def _field_contract(value: type[object]) -> list[str]:
    if not is_dataclass(value):
        return []
    result: list[str] = []
    for field in fields(value):
        if field.default is not MISSING:
            default = repr(field.default)
        elif field.default_factory is not MISSING:
            default = "<factory>"
        else:
            default = "<required>"
        result.append(f"{field.name}: {_annotation(field.type)} = {default}")
    return result


def _type_contract(value: type[object]) -> dict[str, object]:
    public_attributes = sorted(
        name for name in value.__dict__ if not name.startswith("_")
    )
    return {
        "public_attributes": public_attributes,
        "dataclass_fields": _field_contract(value),
        "to_dict_keys": _to_dict_keys(value),
    }


def build_snapshot(manifest: dict[str, Any]) -> dict[str, object]:
    stable = manifest["stable_api"]
    entrypoints = [name.rsplit(".", 1)[1] for name in stable["entrypoints"]]
    root_types = [name.rsplit(".", 1)[1] for name in stable["root_types"]]
    native_stubs = _native_stub_declarations()
    return {
        "schema_version": "1.0.0",
        "contract_version": stable["contract_version"],
        "entrypoints": {
            name: _callable_contract(
                getattr(safe_slate, name), stub_declaration=native_stubs.get(name)
            )
            for name in entrypoints
        },
        "root_types": {
            name: _type_contract(getattr(safe_slate, name)) for name in root_types
        },
    }


def _load_manifest() -> dict[str, Any]:
    payload = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "1.0.0":
        raise SystemExit("unsupported library.json schema_version")
    stable = payload.get("stable_api")
    if not isinstance(stable, dict) or stable.get("contract_version") != "1.0.0":
        raise SystemExit("missing stable 1.0 API contract")
    if payload.get("public_api") != stable.get("entrypoints"):
        raise SystemExit("public_api and stable entrypoints differ")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="replace the snapshot after an intentional compatibility review",
    )
    args = parser.parse_args()
    manifest = _load_manifest()
    actual = build_snapshot(manifest)
    stable = manifest["stable_api"]
    expected_all = {
        name.rsplit(".", 1)[1]
        for name in [*stable["entrypoints"], *stable["root_types"]]
    }
    if set(safe_slate.__all__) != expected_all or len(safe_slate.__all__) != len(
        expected_all
    ):
        raise SystemExit("safe_slate.__all__ does not match the stable root API")
    if args.write:
        SNAPSHOT_PATH.write_text(
            json.dumps(actual, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        return 0
    if not SNAPSHOT_PATH.is_file():
        raise SystemExit(f"stable API snapshot is missing: {SNAPSHOT_PATH}")
    expected = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    if expected != actual:
        raise SystemExit(
            "stable API differs from docs/stable-api-v1.json; "
            "review compatibility before updating the snapshot"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
