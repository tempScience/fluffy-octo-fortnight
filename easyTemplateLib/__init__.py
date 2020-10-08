__author__ = "github.com/wardsimon"
import sys


if sys.version_info >= (3, 8):
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
else:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0.dev"
