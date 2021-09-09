import os
import subprocess

from docker import DockerClient

from xdocker.lib import XDockerConfigurator


class XDockerLinuxConfigurator(XDockerConfigurator):

    @staticmethod
    def get_configuration(client: DockerClient) -> dict:
        # prepare output
        environment = {}
        config = {}
        # get display number
        environment["DISPLAY"] = os.environ.get("DISPLAY", ":0")
        # run `xhost +local:root`
        subprocess.check_call(["xhost", "+local:root"])
        # add nvidia capabilities if we are using nvidia GPUs
        if XDockerLinuxConfigurator.nvidia_gpu(client):
            environment["NVIDIA_VISIBLE_DEVICES"] = "all"
            environment["NVIDIA_DRIVER_CAPABILITIES"] = "graphics"
            config["runtime"] = "nvidia"
        # support QT
        environment["QT_X11_NO_MITSHM"] = "1"
        # mount x-server socket
        config["volumes"] = {
            '/tmp/.X11-unix': {'bind': '/tmp/.X11-unix', 'mode': 'rw'}
        }
        # ---
        config["environment"] = environment
        return config


__all__ = [
    "XDockerLinuxConfigurator"
]
