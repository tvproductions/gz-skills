# Python environment standard for adopting heavy projects

Status: agreed guidance for the Python implementation of the heavy profile.
A consuming project's constitution and quality gate make its adopted choices
binding. This is guidance; selecting `heavy` in `.gz-skills/settings.json`
does not install tools or prove that the environment is ready. The standard is
informed by the [cross-repository inventory](../research/python-install-profile-evidence-2026-09-27.md)
and the [gzkit tool inventory](../research/gzkit-python-environment-profile-2026-09-27.md).

## Two interpreter profiles, one tool assortment

| Profile | Selection | Interpreter |
| --- | --- | --- |
| Normal Python | Python project without an XPPython3 host constraint | Use the latest supported 3.13.x patch for development. |
| XPPython3-oriented Python | Code loaded by XPPython3 or shared with that code | Use the latest supported 3.12.x patch for development and verify against the installed XPPython3 host. |

Use `.python-version` to record the exact development patch. A 3.12.x pin is
the discovery hint for the XPPython3 profile, not proof by itself; inspect the
project's runtime and architecture. Declare the actual package support range
with `[project].requires-python`. A multi-minor claim needs verification on
each claimed minor. Update the patch pin, CI interpreter, tool constraints, and
lock together. `gzs-update-dependencies` can discover current compatible
releases and carry out that refresh; daily installs use the committed lock.
Preserve an adopting project's existing supported range until a migration is
deliberately reviewed.

Both profiles use the same **development assortment**:

| Category | Standard tools | Installation and use |
| --- | --- | --- |
| Astral | `uv`, `ruff`, `ty` | uv is the project manager; Ruff and ty belong to development dependencies. Keep the current compatible versions in project-managed constraints and `uv.lock`. |
| Code quality | `bandit`, `vulture`, `interrogate`, `detect-secrets` | Install as development tools. Define source scope, reviewed exclusions, docstring policy, and secret baseline handling. |
| Testing | `unittest`, `coverage`, `behave`, `unittest-parallel`, `cosmic-ray` | `unittest` is in the standard library; install the other four for development. Keep unit, BDD, coverage, parallel, and mutation commands explicit. |
| Complexity | `radon`, `xenon`, `lizard`, `cohesion` | Install as development tools when used to inspect adopter code. Record thresholds, scope, and response to findings. |
| Documentation | `mkdocs`, `mkdocs-material` | Maintain repository documentation and a reproducible site build, ready for subsequent Read the Docs publication when chosen. |
| Packaging | `uv_build`; `pyinstaller` when shipping an executable | Prefer uv_build for pure-Python distributions. PyInstaller is in the standard assortment but is installed and gated only when the product delivers a standalone executable. |

`uv_build` is the target backend for both gzkit and gz-skills, subject to
package-content parity. Existing adopters migrate rather than replacing a
working backend in one unverified edit. In particular, gz-skills authors skills
only under top-level `skills/` and its installed CLI reads
`gz_skills/bundled`; any backend change must preserve one authored tree and
that wheel resource contract. Verify the wheel, sdist, installed entry point,
and bundled resources. A project with native extension or unsupported build
requirements records a justified backend exception.

The assortment names what a heavy Python project should provision or make
available. It does not require every expensive check on every local edit:
`unittest`, Ruff, ty, coverage, static scans, documentation, and package checks
can be part of the ordinary gate; Behave runs the applicable acceptance
scenarios; Cosmic Ray runs selected consequential modules against a passing
baseline. Classify killed, survived, invalid, and inconclusive mutants
separately. Do not declare a universal mutation score or copy gzkit's coverage
threshold. `unittest-parallel` is available in the standard environment, but
only run suites concurrently after shared fixtures are made safe. The project
owns its precise commands, thresholds, and cadence.

## Runtime boundary

Start with the Python standard library. Add a runtime package when a shipped
capability needs it, declare it under `[project].dependencies`, and keep
development-only tools out of the shipped runtime. A tool can legitimately be a
runtime dependency when the product uses it as a library, as gzkit does for
Radon, Lizard, and Cohesion; record that purpose explicitly.

**Pydantic is an approved runtime option for the normal 3.13 profile**, for
modeling and validation where it helps. It is not mandatory in every package.
Do not add Pydantic to the XPPython3-oriented 3.12 profile. This is the
profile's policy, not a claim that Pydantic cannot run on Python 3.12. Other
packages such as Jinja2, JSON Schema, PyYAML, Rich, Structlog, NetworkX, and
Tree-sitter remain capability-justified rather than universally installed.

For XPPython3-loaded code, keep development tools in the separate uv-managed
environment. Prefer a standard-library-only shared core. Verify any other
approved runtime package under the host's own interpreter and on supported
platforms; a development `.venv` does not populate XPPython3's site-packages.
Add a plugin load/startup or functional host test to the ordinary Python gate.
An external Web API client, supervisor, scenery generator, or telemetry UI uses
the profile appropriate to **its own** runtime even when it interacts with
X-Plane.

## Adoption and migration

Inventory the adopting project's manifests, locks, interpreter pins, CI,
existing tests, package outputs, documentation, and deployment requirements.
Map existing tools and checks into these categories, add missing capabilities
incrementally, and keep behavior working. Project setup and a later
`gzs-update-dependencies` run both reconcile missing required tools and stale
pins against the adopted heavy profile; approved exceptions remain project-owned.
Record the profile, supported Python
range, current patch pin, tool assortment, runtime exceptions, complete gate,
and any deferred migration with an owner and completion condition in the
project's approved guidance. Material architecture or packaging departures
get an ADR. Do not rewrite an existing project just to make adoption look
complete.

## Primary references

- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
  and [dependency groups](https://packaging.python.org/en/latest/specifications/dependency-groups/)
  define package and development dependency surfaces.
- [uv Python version requests](https://docs.astral.sh/uv/concepts/python-versions/),
  [project configuration](https://docs.astral.sh/uv/concepts/projects/config/),
  [dependency management](https://docs.astral.sh/uv/concepts/projects/dependencies/),
  and [build backend](https://docs.astral.sh/uv/concepts/build-backend/)
  document the interpreter pin, lock, and package builder.
- [XPPython3 installation](https://xppython3.readthedocs.io/en/latest/usage/installation_plugin.html)
  shows the embedded Python 3.12 layout;
  [XPPython3 package installation](https://xppython3.readthedocs.io/en/latest/development/modules/xp_pip.html)
  documents its separate interpreter.
- [Cosmic Ray](https://cosmic-ray.readthedocs.io/en/stable/)
  documents the mutation-testing engine.
