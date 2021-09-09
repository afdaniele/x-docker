from docker import DockerClient

from xdocker.lib import XDockerConfigurator


class XDockerMacOSConfigurator(XDockerConfigurator):

    @staticmethod
    def get_configuration(client: DockerClient) -> dict:
        raise NotImplementedError("X-Docker does not support MacOS at this time. "
                                  "You can upvote the corresponding issue on "
                                  "'https://github.com/afdaniele/x-docker/issues/1'.")


__all__ = [
    "XDockerMacOSConfigurator"
]
