# Compatibility and versioning

## Version policy

The distribution uses Semantic Versioning. Version 1.0.0rc1 exposes the final
proposed 1.x API recorded in `library.json` and `stable-api-v1.json`; its
snapshot is identical to 0.5.0. Starting with 1.0.0, breaking changes to that
surface require 2.0. A deprecation remains
documented for at least one minor release and 90 days before removal in the
next major version. Patch releases may tighten validation when previously
accepted inputs were ambiguous, non-finite, silently coerced, or capable of
bypassing a fail-closed boundary.

Schema versions embedded in logs, contracts, and evidence are independent of
the package version. Readers may add support for a new schema without changing
the meaning of an old one. Existing canonical bytes and digests are immutable.

## Python and native ABI

- Supported interpreters: GIL-enabled CPython 3.11, 3.12, 3.13, 3.14, and 3.15.
- Native implementation: Rust 2024 edition, minimum Rust 1.85.
- The extension uses the `cp310-abi3` stable ABI and wheel metadata enforces
  `Requires-Python >=3.11`. Every release wheel is installed on Python 3.11
  and 3.15 on each supported platform.
- Supported wheel targets for a public release: Linux x86-64 and ARM64,
  macOS x86-64 and ARM64, and Windows x86-64. Each artifact must be built from
  the same signed source revision and pass isolated import and smoke tests.

Until the release workflow builds and verifies that complete matrix, source
installs require a compatible Rust toolchain and are not the preferred public
installation path.

## Migration rules

Version 0.4.0 changes the PyPI distribution name from
`safe-slate-recommender` to `tommyslate`. It does not rename the Python package:
applications continue to import `safe_slate`. The preferred intake command is
`tommyslate-freeze-inputs`; `safe-slate-freeze-inputs` remains an equivalent
compatibility alias throughout the 0.x series. Do not install both
distributions in one environment because they provide the same Python module.

- Never reinterpret an existing safety threshold, digest encoding, or evidence
  schema in place.
- Add a new versioned encoding or schema, retain the old reader, and record the
  selected version in every audit artifact.
- Root attributes outside the manifest remain available only in 0.5.x. They
  are removed in 1.0.0rc1; import them from their documented `safe_slate`
  submodule; see [the migration guide](1.0-migration.md).
- A change that can alter a previously certified decision requires a minor
  version, explicit migration notes, and native/Python parity tests.
