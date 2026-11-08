# Security policy

Please report suspected vulnerabilities privately to the repository owner
through GitHub's private vulnerability reporting feature. Do not open a public
issue before coordinated disclosure, and do not include user data, credentials,
private storage locations, model files, or production traces.

The latest stable 1.x release is the supported security line. Before 1.0, only
the latest published Beta or release candidate is assessed. The best-effort
target is to acknowledge a private report within seven calendar days. No fix or
disclosure deadline is guaranteed. After validation, the maintainer will agree
on disclosure timing with the reporter, prepare a new immutable release, and
publish a GitHub Security Advisory when disclosure is appropriate.

The library treats malformed inputs, missing runtime evidence, uncertainty
validation failures, predicate errors, and incomplete search as no-change or
rechecked-incumbent outcomes. This is not a substitute for a process-level
service timeout, resource isolation, authentication, authorization, or privacy
review in the embedding system.

Release artifacts must be built from locked dependencies, include their SBOM,
and be matched to an approved source revision by SHA-256. See
`RELEASE_CHECKLIST.md`.
