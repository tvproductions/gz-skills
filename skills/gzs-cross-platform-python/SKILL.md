---
name: gzs-cross-platform-python
description: Review or implement Python filesystem, text, subprocess, temporary-resource, and test behavior for Windows, macOS, and Linux portability. Use when Python code handles paths, files, encodings, processes, cleanup, platform branches, or failures seen on only one operating system.
compatibility: Requires Python and the target repository's supported platform and version policy.
metadata:
  govzero-version: "0.2.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Cross-Platform Python

Make portability explicit at the operating-system seams. Preserve the project's
supported Python floor and verification tools; these rules do not require a
particular package manager.

## Review and implementation rules

- Use `pathlib.Path` for filesystem paths and join path segments structurally.
  Treat stored or protocol paths separately when their format is intentionally
  POSIX-like.
- Specify text encodings, normally UTF-8. Use `newline=""` for CSV files and
  test newline-sensitive behavior deliberately.
- Use context-managed temporary files and directories. Close files, database
  connections, memory maps, and subprocess handles before cleanup so Windows
  locking semantics are exercised honestly.
- Pass subprocess arguments as a sequence with `shell=False`. Invoke the current
  interpreter with `sys.executable` when a child Python process must match the
  running environment. Use a shell only when shell semantics are the actual
  requirement and quote through a reviewed platform adapter.
- Avoid locale, timezone, executable suffix, path separator, case sensitivity,
  signal, and permission assumptions. Isolate unavoidable differences behind a
  named adapter and test both branches.
- In tests, compare paths as paths, normalize protocol text only at the protocol
  boundary, and clean resources deterministically. A cleanup failure is a test
  failure, not something to hide with `ignore_errors=True`.
- A test that asserts exact bytes must build its fixture through a byte-exact
  channel. A text-mode write translates the newline to the platform separator,
  so a fixture written that way holds CRLF on Windows while the assertion
  carries a line feed. This passes everywhere the separator already matches,
  which is why it survives review and reaches only the platform that runs least
  often.

## Deterministic checks

`scripts/audit_portability.py` carries two static checks. Both use only the
standard library, both run on any platform, and neither needs the defect to
reproduce locally. That last property is the point: these defects are invisible
on whichever platform continuous integration happens to run.

```
python scripts/audit_portability.py --root .
python scripts/audit_portability.py --root . --check subprocess-errors
python scripts/audit_portability.py --root . --format json
```

`line-endings` fails on a missing or weak `.gitattributes` normalization
directive, and on any tracked text surface committed with CRLF. It reads the
git index rather than the working tree, because a Windows checkout renders line
feed blobs as CRLF on disk and git normalizes them away again on commit.

`subprocess-errors` fails on a text-mode subprocess capture that decodes child
output without an `errors=` argument. Undecodable bytes then raise
`UnicodeDecodeError`, which is a `ValueError`, so a handler catching `OSError`
does not catch it and the command aborts mid-run. Bytes-mode calls are never
flagged, because adding `errors=` there would silently switch the call to text
mode and flip its return type.

Exit status is 0 when clean, 1 when findings are reported, and 2 on a usage
error. Scanning covers the whole repository by default; narrow it with repeated
`--path` arguments when a project scopes its own gate to specific trees.

## Discovery and fallback

Prefer the project's own portability gate when one exists, and treat this skill
as the invariant rather than the implementation. In order:

1. A repository-local portability check or lint rule that already covers the
   seam under review. Run it and read its scope before adding anything.
2. A documented project command that aggregates verification, such as
   `gz check` in a GovZero project, where a portability scope may already be
   registered and fail closed on every push.
3. `scripts/audit_portability.py` in this skill, which needs nothing but Python
   and, for the line-ending arm, a git work tree.

When a project gate exists it stays authoritative. A fail-closed gate must keep
its implementation inside the repository it guards, because a gate whose code
lives in an installed plugin cannot run where the plugin is absent. Use the
bundled script to widen coverage, to audit a project that has no gate of its
own, or to check a seam before a gate exists. Do not make a project's gate
depend on it.

## Workflow

1. Read the supported-platform policy and identify the relevant OS seam.
2. Run the deterministic checks above, preferring the project's gate per the
   discovery order, and record which scope actually ran.
3. Reproduce the behavior on the current platform with a focused test or script.
4. Inspect for assumptions in paths, text, resources, subprocesses, environment,
   and assertions. Change only assumptions evidenced by the code path.
5. Add a regression test that would fail under the alternate platform's
   semantics. Prefer a static assertion over a runtime one when the defect is
   only observable on a platform the project rarely runs, since a test that can
   only fail on the absent platform is not a detector. Use CI or an actual
   alternate host when available; otherwise state which platform remains
   unobserved.
6. Run the repository's full quality gate and every configured platform job
   available locally.

## Evidence

Report the portability assumption found, affected platforms, which checks ran
and at what scope, the regression test, commands and results, and any platform
that could not be exercised.
