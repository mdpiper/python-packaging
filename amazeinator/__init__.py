import pkg_resources
from .amazeinator import Amazeinator


__version__ = pkg_resources.get_distribution("amazeinator").version

__all__ = ["Amazeinator"]
