# Release checklist — TommySlate 0.4.1 Beta

Version 0.4.1 aligns the GitHub repository with the `tommyslate` distribution
name and changes the PyPI classifier from Alpha to Beta. Runtime behavior, the
`safe_slate` import, and the stable API remain unchanged from 0.4.0.

Frozen source: `ea5745472bc19a536bef3318a2357ff222a20c99`.
[Publication-disabled qualification](https://github.com/natomi1203/tommyslate/actions/runs/42384926807),
[TestPyPI qualification](https://github.com/natomi1203/tommyslate/actions/runs/42385302459),
and [production promotion](https://github.com/natomi1203/tommyslate/actions/runs/42385996695)
all completed successfully.

## Source and identity contract

- [x] Freeze the exact 40-character merge commit selected from `main`.
- [x] Rename the repository to `natomi1203/tommyslate` and update the local
      `origin` remote.
- [x] `pyproject.toml`, `Cargo.toml`, `CITATION.cff`, `library.json`, and the
      release workflow agree on distribution `tommyslate` and version `0.4.1`.
- [x] Package metadata uses `Development Status :: 4 - Beta` and contains no
      Alpha classifier.
- [x] Repository, documentation, changelog, issue, citation, and CI badge URLs
      point to `https://github.com/natomi1203/tommyslate`.
- [x] The native module remains `safe_slate._core`; all registered public
      interfaces and both intake CLI names retain their existing behavior.

## Verification for the frozen source SHA

- [x] `uv sync --frozen` and `uv run maturin develop --release` succeed.
- [x] Python tests, mypy, `mypy.stubtest`, and bytecode compilation pass.
- [x] Rust tests and warning-free Clippy pass with the locked graph.
- [x] Python and Rust coverage gates remain at 100%.
- [x] A local wheel and sdist identify `tommyslate==0.4.1`, contain the Beta
      classifier and `safe_slate`, and pass `twine check`.
- [x] Five platform wheels and one sdist are built from one source SHA and pass
      isolated Python 3.15 smoke tests.

## OIDC and TestPyPI

- [x] Update the active Trusted Publisher on TestPyPI and PyPI from repository
      `natomi1203/safe-slate-recommender` to `natomi1203/tommyslate`, retaining
      workflow `safe-slate-release.yml` and protected environments
      `testpypi`/`pypi`.
- [x] Confirm both GitHub Environments still require owner review and remain
      restricted to `main`.
- [x] Run a publication-disabled five-platform build and freeze the manifest.
- [x] Publish and verify the exact manifest on TestPyPI through OIDC.
- [x] Reinstall `tommyslate==0.4.1` from TestPyPI on all five target runners.
- [x] Obtain explicit owner approval for the production artifact hashes.

## Production publication

- [x] Recover the exact TestPyPI-qualified files without rebuilding.
- [x] Upload through the protected `pypi` environment and OIDC.
- [x] Match all production filenames and SHA-256 values to TestPyPI.
- [x] Reinstall `tommyslate==0.4.1` from PyPI on all five target runners.
- [x] Replace candidate wording with the immutable 0.4.1 release evidence.

Do not delete or overwrite 0.4.0 or the historical
`safe-slate-recommender==0.3.1` distribution. Tags, GitHub Release creation,
containers, deployments, and announcements remain separate decisions.
