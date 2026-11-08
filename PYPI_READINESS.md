# PyPI release evidence

Assessment date: 2026-11-08 (Asia/Tokyo).

## TommySlate 1.0.0rc1 Beta release candidate

TommySlate 1.0.0rc1 is published on
[PyPI](https://pypi.org/project/tommyslate/1.0.0rc1/) and
[TestPyPI](https://test.pypi.org/project/tommyslate/1.0.0rc1/). The frozen
source is `1a55918a348e59ef74e7b46b2fdda88e1c8e75b2`. The RC exposes the
final proposed 1.x root API but intentionally retains the Beta classifier.

The [publication-disabled run](https://github.com/natomi1203/tommyslate/actions/runs/42481554610)
validated five wheels and one sdist. The protected
[TestPyPI run](https://github.com/natomi1203/tommyslate/actions/runs/42481873114)
and [production run](https://github.com/natomi1203/tommyslate/actions/runs/42483220811)
matched every remote filename and SHA-256 value, then installed the exact RC on
Python 3.11 and 3.15 across all five runners. Transient Simple API cache misses
were retried without rebuilding or re-uploading any artifact.

The [signed finalization run](https://github.com/natomi1203/tommyslate/actions/runs/42483657312)
created keyless-signed tag `tommyslate-v1.0.0rc1`, verified its Git signature,
Rekor entry, workflow identity, and OIDC issuer, then published the
[GitHub Prerelease](https://github.com/natomi1203/tommyslate/releases/tag/tommyslate-v1.0.0rc1).
The Rekor transparency-log index is `3755793960`.

The complete PyPI artifact set was available at
`2026-11-08T13:06:13.756977Z`. The earliest stable-release time is therefore
`2026-12-08T13:06:13.756977Z`, subject to all other gates remaining satisfied.

## TommySlate 1.0.0rc1 production manifest

| Artifact | SHA-256 |
| --- | --- |
| `tommyslate-1.0.0rc1-cp310-abi3-macosx_11_0_arm64.whl` | `1cc7011f8328c530f75a451b1a22c91523a56a283c3662a6863e3a285c0026fd` |
| `tommyslate-1.0.0rc1-cp310-abi3-macosx_11_0_x86_64.whl` | `89c569a22e03d1b4472a106d2d0ea4f1040fb7be0f5603242f86243656c78633` |
| `tommyslate-1.0.0rc1-cp310-abi3-manylinux_2_28_aarch64.whl` | `2f4b256c6c91b1748efb6fb1a09e36b62d30348e332f0df5f9f95b95c4908904` |
| `tommyslate-1.0.0rc1-cp310-abi3-manylinux_2_28_x86_64.whl` | `5526f9f2082e278424245e942d5bb35d241b9297301230d28f02bea62edc2178` |
| `tommyslate-1.0.0rc1-cp310-abi3-win_amd64.whl` | `f19c172cc368587d2dc19c4f2f8a9885bf4d3a02fc9006c931d889be7b012055` |
| `tommyslate-1.0.0rc1.tar.gz` | `fd31dd349d6f8faf03061ae447bfa0692fc57c1711e36b2370c3973c04885de7` |

The release manifest itself has SHA-256
`d3237ac735296eda537a24c262234d933dee28f47132afe9efaa67e0eefd9d06`.
Production/Stable remains blocked until the RC completes its 30-day soak and
one author-external integration is accepted.

## TommySlate 0.5.0 Beta production release

TommySlate 0.5.0 is published on
[PyPI](https://pypi.org/project/tommyslate/0.5.0/) and
[TestPyPI](https://test.pypi.org/project/tommyslate/0.5.0/). It expands
supported GIL-enabled CPython versions to 3.11–3.15 and freezes the proposed
1.x API without changing the ranking contract or the `safe_slate` import.

The frozen source is `d65116e83929b07ac10e5ad30303482c7e67e073`. The
[publication-disabled run](https://github.com/natomi1203/tommyslate/actions/runs/42472279309)
built and smoke-tested five wheels and one sdist. The approved
[TestPyPI qualification run](https://github.com/natomi1203/tommyslate/actions/runs/42472616483)
published through OIDC, matched all six remote hashes, and completed Python
3.11 and 3.15 reinstalls on all five runners. The approved
[production promotion run](https://github.com/natomi1203/tommyslate/actions/runs/42473505109)
recovered that exact bundle without rebuilding, matched the production hashes,
and repeated all ten installs.

The
[signed-release finalization run](https://github.com/natomi1203/tommyslate/actions/runs/42479429791)
verified the keyless `tommyslate-v0.5.0` tag against the GitHub Actions OIDC
identity and Rekor, then published the
[GitHub Prerelease](https://github.com/natomi1203/tommyslate/releases/tag/tommyslate-v0.5.0)
with the six packages, immutable manifest, `SHA256SUMS`, and five wheel SBOMs.

## TommySlate 0.5.0 production manifest

| Artifact | SHA-256 |
| --- | --- |
| `tommyslate-0.5.0-cp310-abi3-macosx_11_0_arm64.whl` | `11ef1e996b0287305a7cb48866c40e06d9054bff89506e6d3219e05bad366f96` |
| `tommyslate-0.5.0-cp310-abi3-macosx_11_0_x86_64.whl` | `1346f96e17f2848e6289d52ad410b9ea8d290c616b12704e9345079c49e1b4ec` |
| `tommyslate-0.5.0-cp310-abi3-manylinux_2_28_aarch64.whl` | `667dd53becbce64cf1852ee69ed931978c38e5a9f32803ab2496e556ef50325f` |
| `tommyslate-0.5.0-cp310-abi3-manylinux_2_28_x86_64.whl` | `d037b65816550816b9a05b52ce222b2b9461303cbf5643cb071d3c786a1acf20` |
| `tommyslate-0.5.0-cp310-abi3-win_amd64.whl` | `5583194bdad5b78b16503c90cd4ac7dbb09f2a43670e6b1fee966bbf957ec6e3` |
| `tommyslate-0.5.0.tar.gz` | `00532c948b4e4964b3d936e2652714831f44131cb872d802adce50a589c8270e` |

Production PyPI, TestPyPI, the GitHub Prerelease, and the archived manifest
expose these exact six package filenames and SHA-256 values.

## TommySlate 0.4.1 Beta production release

Version 0.4.1 renames the GitHub repository to
[`natomi1203/tommyslate`](https://github.com/natomi1203/tommyslate), matching
the PyPI distribution name, and changes the development-status classifier from
Alpha to Beta. It does not change runtime behavior, the `safe_slate` import,
the seven registered stable interfaces, or the release artifact policy.

TommySlate 0.4.1 is published on
[PyPI](https://pypi.org/project/tommyslate/0.4.1/) and
[TestPyPI](https://test.pypi.org/project/tommyslate/0.4.1/). The active Trusted
Publishers on both indexes are bound to repository `natomi1203/tommyslate`,
workflow `safe-slate-release.yml`, and the owner-reviewed `testpypi`/`pypi`
environments. Both environments are restricted to `main`; no long-lived index
token was created.

The frozen source is `ea5745472bc19a536bef3318a2357ff222a20c99`. A
[publication-disabled run](https://github.com/natomi1203/tommyslate/actions/runs/42384926807)
first built and smoke-tested five wheels and one sdist. The approved
[TestPyPI qualification run](https://github.com/natomi1203/tommyslate/actions/runs/42385302459)
published those six files through OIDC, matched every remote SHA-256 to the
manifest, and reinstalled version 0.4.1 on all five target runners.

The approved
[production promotion run](https://github.com/natomi1203/tommyslate/actions/runs/42385996695)
recovered the exact TestPyPI-qualified bundle without rebuilding, verified the
source run and manifest, uploaded through OIDC, matched every production hash,
and reinstalled from PyPI on Linux x86-64 and ARM64, macOS x86-64 and ARM64,
and Windows x86-64.

## TommySlate 0.4.1 production manifest

| Artifact | SHA-256 |
| --- | --- |
| `tommyslate-0.4.1-cp310-abi3-macosx_11_0_arm64.whl` | `f8cf367b7279cfc1508b4ce8f330cb9f2385e08c6d0199836ca9c1f5f1dea538` |
| `tommyslate-0.4.1-cp310-abi3-macosx_11_0_x86_64.whl` | `442c8636be40f547ad9a001f8258a356193f58970f4921eb01b17645686326e2` |
| `tommyslate-0.4.1-cp310-abi3-manylinux_2_28_aarch64.whl` | `61d8f281027eb7293135930aedca95781aade2cb353a5c0f310a6620b010aa56` |
| `tommyslate-0.4.1-cp310-abi3-manylinux_2_28_x86_64.whl` | `8112ed49e2171ae7fa0555f0d40b783ef79e8553f23f40b98e8059c3a53978d6` |
| `tommyslate-0.4.1-cp310-abi3-win_amd64.whl` | `23dbeb941b81d208f4dd3c7660b9186d3819f797f1b3c1ef7aef2dbec74bfb8b` |
| `tommyslate-0.4.1.tar.gz` | `f4da82ccbaabcc2aa631b34f7b6bfe9e47a5e09c722e0edccdb4aa6b40b7e371` |

Production PyPI, TestPyPI, the archived manifest, and the downloaded files all
expose these exact six filenames and SHA-256 values.

## TommySlate 0.4.0 production release

Version 0.4.0 changes only the distribution identity and migration-facing
metadata: users will install `tommyslate`, while Python continues to import
`safe_slate`. The new preferred CLI is `tommyslate-freeze-inputs`; the existing
`safe-slate-freeze-inputs` entry point remains an alias. The stable API and
runtime behavior are unchanged from 0.3.1.

TommySlate 0.4.0 is published on
[PyPI](https://pypi.org/project/tommyslate/0.4.0/). Publication used protected
`testpypi` and `pypi` environments and OIDC Trusted Publishing. At release
time, the publisher was bound to the former repository name
`natomi1203/safe-slate-recommender` and workflow `safe-slate-release.yml`; the
repository was subsequently renamed. No long-lived package-index token was
created.

The frozen source is `9594cc0fd96a667cc323a3a8e99b42b04d3100db`. A
[publication-disabled run](https://github.com/natomi1203/tommyslate/actions/runs/42222485659)
first completed all five wheel builds, local installs, smoke tests, sdist build,
metadata checks, and manifest generation.

The approved
[TestPyPI qualification run](https://github.com/natomi1203/tommyslate/actions/runs/42224307122)
then published version 0.4.0 through OIDC, matched all six remote hashes to its
manifest, and reinstalled `tommyslate==0.4.0` successfully on Linux x86-64 and
ARM64, macOS x86-64 and ARM64, and Windows x86-64. The project is available at
[TestPyPI](https://test.pypi.org/project/tommyslate/0.4.0/).

The approved
[production promotion run](https://github.com/natomi1203/tommyslate/actions/runs/42233403791)
recovered that exact TestPyPI-qualified bundle without rebuilding, matched all
six production filenames and SHA-256 values, and reinstalled
`tommyslate==0.4.0` successfully on all five target runners.

## TommySlate 0.4.0 production manifest

| Artifact | SHA-256 |
| --- | --- |
| `tommyslate-0.4.0-cp310-abi3-macosx_11_0_arm64.whl` | `04017dd6015a91bd6aca241983123d366c000d5990a0eb6b5d0db03ed2f27a24` |
| `tommyslate-0.4.0-cp310-abi3-macosx_11_0_x86_64.whl` | `aacc49de42fa0c80c2d053c22215b68628e9c65e856e5c50b4d9c0816a0a665e` |
| `tommyslate-0.4.0-cp310-abi3-manylinux_2_28_aarch64.whl` | `e7966677c35c63ba33737c3d0dfac3eaa744eb58976d92d32c4b7d5ce06a66b8` |
| `tommyslate-0.4.0-cp310-abi3-manylinux_2_28_x86_64.whl` | `974379266174ed985a3ecc2aa535b051ee319c0fa40ec4f424d46ef41a4934a5` |
| `tommyslate-0.4.0-cp310-abi3-win_amd64.whl` | `dffd79c9f1e0c52a99ccc960d0782b0a25e34640c00fa160e6dca48f85d6b7ac` |
| `tommyslate-0.4.0.tar.gz` | `c413975ffe09e7df341cac81986944f6285ea2a20ccf5024db372e6349fdcb5d` |

Production PyPI and TestPyPI expose the same six filenames and SHA-256 values
listed above. The promotion recovered the artifact bundle from qualification
run `42224307122`, verified the run identity, source SHA, manifest, local hashes
and TestPyPI hashes, and uploaded those exact files without rebuilding.

## Version 0.3.1 production release

Version 0.3.1 is published on
[PyPI](https://pypi.org/project/safe-slate-recommender/0.3.1/) from source
commit `342a016d644d72da15f9fc2a8d59a70f6ffda3c2`. The approved
[release workflow](https://github.com/natomi1203/tommyslate/actions/runs/42215206667)
built one source distribution and five wheels, qualified the exact artifacts
on TestPyPI, then uploaded the same files to production PyPI without rebuilding.

Both indexes matched every filename and SHA-256 value in the frozen manifest.
The production package was reinstalled and smoke-tested successfully on Linux
x86-64/ARM64, macOS x86-64/ARM64, and Windows x86-64.

Publication used protected `testpypi` and `pypi` GitHub Environments with OIDC
Trusted Publishing. No long-lived package-index token was created. The first
two Linux x86-64 TestPyPI reinstall attempts observed stale Simple API cache
data; the unchanged workflow succeeded after the cache refreshed, with no
artifact or hash mismatch.

## Production release manifest

| Artifact | SHA-256 |
| --- | --- |
| `safe_slate_recommender-0.3.1-cp310-abi3-macosx_11_0_arm64.whl` | `c94312c517162f0f35819ec81547ac4bf69bae2e9cb1af8edf00429e33e002a7` |
| `safe_slate_recommender-0.3.1-cp310-abi3-macosx_11_0_x86_64.whl` | `58ca4bfb47cff21cfada335e3d32dfd3b1a0e9ff895d897f8ad5cd81abf8d990` |
| `safe_slate_recommender-0.3.1-cp310-abi3-manylinux_2_28_aarch64.whl` | `1f40aca49499a126cc92f56d27a12652592ac58f897bc93d546a6f6ef4e3c2ab` |
| `safe_slate_recommender-0.3.1-cp310-abi3-manylinux_2_28_x86_64.whl` | `3a645a143e005f9cbcc7dfd0cd03df9486c07736f761ce29738b1752026175f9` |
| `safe_slate_recommender-0.3.1-cp310-abi3-win_amd64.whl` | `62f3130bc5d9009bab347246e4ca0a10cac145018633ad3515ae3292dfd05352` |
| `safe_slate_recommender-0.3.1.tar.gz` | `ae6d13274ccf686472050d488245d80d2eca8f49bdd28bd25c801147a23f447b` |

The rights holder selected Apache-2.0 for this reusable software distribution;
repository-level research remains CC-BY-4.0. Tags, GitHub Releases, containers,
deployments, and announcements were not part of this publication.

The historical 0.3.0 TestPyPI qualification remains valid only for its exact
artifacts and is not the recommended installation target.
