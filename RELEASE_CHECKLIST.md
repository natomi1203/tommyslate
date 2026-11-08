# Release checklist — TommySlate 0.5.0 Beta

Version 0.5.0 expands supported GIL-enabled CPython versions to 3.11–3.15 and
freezes the proposed 1.x API. It does not change ranking decisions, fail-closed
behavior, artifact count, or the `safe_slate` import.

## Source and API contract

- [ ] Freeze the exact 40-character merge commit selected from protected `main`.
- [x] `pyproject.toml`, `Cargo.toml`, `CITATION.cff`, `library.json`, and the
      release workflow agree on distribution `tommyslate` and version `0.5.0`.
- [x] Metadata declares Beta and `Requires-Python >=3.11` with CPython
      classifiers 3.11–3.15.
- [x] `safe_slate.__all__` contains only seven entrypoints and their stable
      root result types; 0.4.1 root attributes remain available for migration.
- [x] The 1.x API snapshot records signatures, defaults, types, result
      attributes, dataclass fields, and `to_dict()` keys.

## Verification for the frozen source SHA

- [ ] Python tests pass on 3.11, 3.12, 3.13, 3.14, and 3.15.
- [ ] Rust 1.85 `cargo check --locked --all-targets` succeeds.
- [ ] Rust 1.99 tests, Clippy, mypy, stubtest, and bytecode compilation pass.
- [ ] Python and Rust coverage gates remain at 100%.
- [ ] CodeQL for Python, Rust, and Actions succeeds.
- [ ] `cargo-audit` and `pip-audit` report no High/Critical vulnerability.
- [ ] A local wheel and sdist identify `tommyslate==0.5.0`, include Apache-2.0
      and type metadata, and pass `twine check`.
- [ ] Five `cp310-abi3` wheels and one sdist are built from one source SHA.
- [ ] Every wheel passes isolated Python 3.11 and 3.15 import, `pip check`,
      approved-update, and baseline-fallback smoke tests.

## OIDC publication

- [ ] Run the publication-disabled five-platform matrix and freeze its manifest.
- [ ] Publish the exact manifest to TestPyPI through the protected environment.
- [ ] Match all TestPyPI filenames and SHA-256 values to the manifest.
- [ ] Reinstall from TestPyPI on Python 3.11 and 3.15 on all five runners.
- [ ] Promote the TestPyPI-qualified files to PyPI without rebuilding.
- [ ] Match all production filenames and hashes and repeat the ten installs.

## Signed GitHub prerelease

- [ ] Create keyless-signed tag `tommyslate-v0.5.0` from the frozen source SHA.
- [ ] Verify the tag with the pinned `gitsign` version.
- [ ] Publish a GitHub Prerelease with the six packages, manifest,
      `SHA256SUMS`, SBOMs, source SHA, and TestPyPI/PyPI run URLs.

Do not publish 1.0.0 until the latest RC completes a 30-day soak and an
author-external integration is accepted. Do not publish the sidecar container,
free-threaded wheels, musllinux wheels, or Windows ARM64 wheels in this release.
