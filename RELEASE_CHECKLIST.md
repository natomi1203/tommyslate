# Release checklist — TommySlate 1.0.0rc1 Beta

Version 1.0.0rc1 removes the 0.5.x compatibility-only root attributes and
freezes the final proposed 1.x API. It remains Beta during the mandatory soak.

Install the opt-in RC with:

```bash
uv add "tommyslate==1.0.0rc1"
```

## RC source and API contract

- [x] Freeze the exact protected `main` source commit:
      `1a55918a348e59ef74e7b46b2fdda88e1c8e75b2`.
- [x] Python metadata uses `1.0.0rc1`; Cargo metadata uses the equivalent
      SemVer `1.0.0-rc.1`; citation, manifest, lockfiles, and workflows agree.
- [x] Metadata remains `Development Status :: 4 - Beta` and supports
      GIL-enabled CPython 3.11–3.15.
- [x] The root exposes exactly seven entrypoints and their direct result types.
      Advanced support APIs remain importable from documented submodules.
- [x] The RC API snapshot is byte-for-byte identical to the 0.5.0 snapshot.

## RC verification and publication

- [x] All required checks pass on the frozen source SHA, including Python
      3.11–3.15, Rust 1.85 MSRV, Rust 1.99 tests/Clippy, mypy, stubtest,
      CodeQL, audits, and 100% Python/Rust coverage.
- [x] The [publication-disabled matrix](https://github.com/natomi1203/tommyslate/actions/runs/42481554610)
      builds five wheels and one sdist and verifies local installs.
- [x] The protected [TestPyPI run](https://github.com/natomi1203/tommyslate/actions/runs/42481873114)
      publishes the exact manifest, matches all hashes, and verifies Python
      3.11/3.15 installs on every runner.
- [x] The protected [PyPI run](https://github.com/natomi1203/tommyslate/actions/runs/42483220811)
      promotes the TestPyPI-qualified files without rebuilding, matches all
      hashes, and repeats every install.
- [x] The [signed-release run](https://github.com/natomi1203/tommyslate/actions/runs/42483657312)
      creates keyless-signed tag `tommyslate-v1.0.0rc1`; the
      [GitHub Prerelease](https://github.com/natomi1203/tommyslate/releases/tag/tommyslate-v1.0.0rc1)
      attaches the same six packages, manifest, `SHA256SUMS`, and SBOMs.

## Stable gates opened by RC publication

- [x] Record the RC source SHA, PyPI publication time, and UTC timestamp 30
      days later in `docs/stable-readiness.json`.
- [ ] Accept one integration report from a non-author with clean install,
      stable-entrypoint execution, approved update, and baseline fallback.
- [ ] Reach the recorded soak date with no unresolved High/Critical
      vulnerability, P0/P1 issue, compatibility blocker, or RC code change.
- [ ] Confirm the latest required checks are green and the RC/1.0 API snapshots
      are identical before preparing 1.0.0.

Do not publish 1.0.0, change its classifier to Production/Stable, or claim the
external-validation gate before every stable gate above is evidenced.

## Completed 0.5.0 Beta evidence

Version 0.5.0 expands supported GIL-enabled CPython versions to 3.11–3.15 and
freezes the proposed 1.x API. It does not change ranking decisions, fail-closed
behavior, artifact count, or the `safe_slate` import.

### Source and API contract

- [x] Freeze the exact 40-character merge commit selected from protected `main`:
      `d65116e83929b07ac10e5ad30303482c7e67e073`.
- [x] `pyproject.toml`, `Cargo.toml`, `CITATION.cff`, `library.json`, and the
      release workflow agree on distribution `tommyslate` and version `0.5.0`.
- [x] Metadata declares Beta and `Requires-Python >=3.11` with CPython
      classifiers 3.11–3.15.
- [x] `safe_slate.__all__` contains only seven entrypoints and their stable
      root result types; 0.4.1 root attributes remain available for migration.
- [x] The 1.x API snapshot records signatures, defaults, types, result
      attributes, dataclass fields, and `to_dict()` keys.

### Verification for the frozen source SHA

- [x] Python tests pass on 3.11, 3.12, 3.13, 3.14, and 3.15.
- [x] Rust 1.85 `cargo check --locked --all-targets` succeeds.
- [x] Rust 1.99 tests, Clippy, mypy, stubtest, and bytecode compilation pass.
- [x] Python and Rust coverage gates remain at 100%.
- [x] CodeQL for Python, Rust, and Actions succeeds.
- [x] `cargo-audit` and `pip-audit` report no High/Critical vulnerability.
- [x] A local wheel and sdist identify `tommyslate==0.5.0`, include Apache-2.0
      and type metadata, and pass `twine check`.
- [x] Five `cp310-abi3` wheels and one sdist are built from one source SHA.
- [x] Every wheel passes isolated Python 3.11 and 3.15 import, `pip check`,
      approved-update, and baseline-fallback smoke tests.

### OIDC publication

- [x] Run the publication-disabled five-platform matrix and freeze its manifest:
      [run 42472279309](https://github.com/natomi1203/tommyslate/actions/runs/42472279309).
- [x] Publish the exact manifest to TestPyPI through the protected environment:
      [run 42472616483](https://github.com/natomi1203/tommyslate/actions/runs/42472616483).
- [x] Match all TestPyPI filenames and SHA-256 values to the manifest.
- [x] Reinstall from TestPyPI on Python 3.11 and 3.15 on all five runners.
- [x] Promote the TestPyPI-qualified files to PyPI without rebuilding:
      [run 42473505109](https://github.com/natomi1203/tommyslate/actions/runs/42473505109).
- [x] Match all production filenames and hashes and repeat the ten installs.

### Signed GitHub prerelease

- [x] Create keyless-signed tag `tommyslate-v0.5.0` from the frozen source SHA.
- [x] Verify the tag with pinned gitsign 0.17.1, including the Git signature,
      Rekor entry, and certificate claims.
- [x] Publish a [GitHub Prerelease](https://github.com/natomi1203/tommyslate/releases/tag/tommyslate-v0.5.0) with the six packages, manifest,
      `SHA256SUMS`, SBOMs, source SHA, and TestPyPI/PyPI run URLs.

Do not publish 1.0.0 until the latest RC completes a 30-day soak and an
author-external integration is accepted. Do not publish the sidecar container,
free-threaded wheels, musllinux wheels, or Windows ARM64 wheels in this release.
