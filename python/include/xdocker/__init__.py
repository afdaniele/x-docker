__version__ = '0.0.1'

from sys import platform
from typing import Type

from docker import DockerClient

from .lib import XDockerConfigurator
from .lib_linux import XDockerLinuxConfigurator
from .lib_macos import XDockerMacOSConfigurator


def _from_system() -> Type[XDockerConfigurator]:
    if platform == "linux" or platform == "linux2":
        # linux
        return XDockerLinuxConfigurator
    elif platform == "darwin":
        # OS X
        return XDockerMacOSConfigurator
    else:
        raise RuntimeError(f"Platform '{platform}' not supported")


def get_configuration(client: DockerClient) -> dict:
    configurator = _from_system()
    return configurator.get_configuration(client)
