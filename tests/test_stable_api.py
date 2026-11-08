from __future__ import annotations

import importlib
import importlib.util
import json
from pathlib import Path
import tomllib

import safe_slate


ROOT = Path(__file__).resolve().parents[1]


def _checker():
    spec = importlib.util.spec_from_file_location(
        "check_stable_api", ROOT / "scripts" / "check_stable_api.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_stable_api_snapshot_matches_runtime_and_stubs() -> None:
    manifest = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    expected = json.loads(
        (ROOT / "docs" / "stable-api-v1.json").read_text(encoding="utf-8")
    )
    assert _checker().build_snapshot(manifest) == expected


def test_root_all_is_exactly_the_stable_surface() -> None:
    manifest = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    stable = manifest["stable_api"]
    expected = {
        name.rsplit(".", 1)[1]
        for name in [*stable["entrypoints"], *stable["root_types"]]
    }
    assert set(safe_slate.__all__) == expected
    assert len(safe_slate.__all__) == len(expected)


def test_transitive_support_api_is_importable_from_documented_submodules() -> None:
    manifest = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    for qualified_name in manifest["stable_api"]["transitive_support_api"]:
        module_name, attribute = qualified_name.rsplit(".", 1)
        assert hasattr(importlib.import_module(module_name), attribute), qualified_name


def test_legacy_root_attributes_remain_available_but_are_not_stable_exports() -> None:
    for name in (
        "CalibrationResult",
        "build_candidate_pool_operations",
        "create_input_manifest",
    ):
        assert hasattr(safe_slate, name)
        assert name not in safe_slate.__all__


def test_python_compatibility_metadata_agrees() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))[
        "project"
    ]
    manifest = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    assert project["requires-python"] == manifest["python_requires"] == ">=3.11"
    assert manifest["python_versions"] == ["3.11", "3.12", "3.13", "3.14", "3.15"]
    for version in manifest["python_versions"]:
        assert f"Programming Language :: Python :: {version}" in project["classifiers"]


def test_stable_readiness_is_fail_closed_before_rc_soak() -> None:
    readiness = json.loads(
        (ROOT / "docs" / "stable-readiness.json").read_text(encoding="utf-8")
    )
    assert readiness["schema_version"] == "1.0.0"
    assert readiness["phase"] == "beta"
    assert readiness["beta_version"] == "0.5.0"
    assert readiness["release_candidate"]["version"] is None
    assert readiness["external_validation"]["required"] == 1
    assert readiness["external_validation"]["accepted_issue_urls"] == []
    assert readiness["stable_release_ready"] is False
