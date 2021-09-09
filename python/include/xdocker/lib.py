from abc import abstractmethod

from docker import DockerClient


class XDockerConfigurator:

    @staticmethod
    def nvidia_gpu(client: DockerClient) -> bool:
        info = client.info()
        return 'Runtimes' in info and 'nvidia' in info['Runtimes']

    @staticmethod
    @abstractmethod
    def get_configuration(client: DockerClient) -> dict:
        pass
