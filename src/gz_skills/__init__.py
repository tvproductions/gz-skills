"""Portable GovZero skills and installation tooling."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("govzero-skills")
except PackageNotFoundError:  # Running directly from a source checkout.
    __version__ = "0.5.0"
