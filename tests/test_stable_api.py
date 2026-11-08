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


def test_legacy_root_attributes_are_removed_from_the_release_candidate() -> None:
    manifest = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    transitive_names = {
        qualified_name.rsplit(".", 1)[1]
        for qualified_name in manifest["stable_api"]["transitive_support_api"]
    }
    legacy_names = {
        "CalibrationResult",
        "build_candidate_pool_operations",
        "create_input_manifest",
        *transitive_names,
    }
    for name in legacy_names:
        assert not hasattr(safe_slate, name)
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


def test_stable_readiness_is_fail_closed_during_rc_soak() -> None:
    readiness = json.loads(
        (ROOT / "docs" / "stable-readiness.json").read_text(encoding="utf-8")
    )
    assert readiness["schema_version"] == "1.0.0"
    assert readiness["phase"] == "release-candidate"
    assert readiness["beta_version"] == "0.5.0"
    assert readiness["release_candidate"]["version"] == "1.0.0rc1"
    assert readiness["release_candidate"]["source_sha"] == (
        "1a55918a348e59ef74e7b46b2fdda88e1c8e75b2"
    )
    assert readiness["release_candidate"]["pypi_published_at"] == (
        "2026-11-08T13:06:13.756977Z"
    )
    assert readiness["release_candidate"]["soak_not_before"] == (
        "2026-12-08T13:06:13.756977Z"
    )
    assert readiness["release_candidate"]["api_snapshot_sha256"] == (
        "ca13ac1e164c002e5c4203706862685c3c7346900c75fb989debd27583c71b26"
    )
    assert readiness["release_candidate"]["artifact_manifest_sha256"] == (
        "d3237ac735296eda537a24c262234d933dee28f47132afe9efaa67e0eefd9d06"
    )
    for field in (
        "no_publish_run_url",
        "testpypi_run_url",
        "pypi_run_url",
        "github_release_run_url",
        "github_release_url",
    ):
        assert readiness["release_candidate"][field].startswith("https://")
    assert readiness["external_validation"]["required"] == 1
    assert readiness["external_validation"]["accepted_issue_urls"] == []
    assert readiness["stable_release_ready"] is False
