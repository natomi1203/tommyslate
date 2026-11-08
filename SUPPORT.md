# Support policy

TommySlate is maintained on a best-effort basis by a single maintainer. The
latest stable 1.x release is the supported production line. Pre-releases are
supported only for collecting release-candidate feedback, and older 0.x
releases receive no routine fixes.

Use GitHub Issues for reproducible bugs, compatibility regressions, and
documentation problems. Include the TommySlate version, Python version,
operating system, CPU architecture, a minimal example, and the observed
fallback or error. Do not include user data, credentials, private paths, model
files, or production traces.

Security reports must follow [SECURITY.md](SECURITY.md) and remain private. The
best-effort target is to acknowledge a private security report within seven
calendar days. TommySlate does not promise a remediation deadline, uptime,
general-support response time, or commercial SLA.

Within the stable surface documented in `library.json`, 1.x releases preserve
source compatibility. Deprecations remain documented for at least one minor
release and 90 days; removal requires a new major version. Provisional
submodule APIs outside that manifest may change in a minor release with
migration notes.
