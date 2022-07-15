import subprocess
import time

from docker import DockerClient

from xdocker.lib import XDockerConfigurator


class XDockerMacOSConfigurator(XDockerConfigurator):

    @staticmethod
    def get_configuration(client: DockerClient) -> dict:
        # prepare output
        environment = {}
        config = {}
        # give XQuartz permissions to run iglx
        subprocess.check_call(
            ["defaults", "write", "org.macosforge.xquartz.X11", "enable_iglx", "-bool", "true"])
        # start XQuartz
        app_count = subprocess.check_output(
            "ps aux | grep XQuartz | grep -v grep | wc -l | awk '{print $1}'", shell=True).decode("utf-8").split('\n')[0]
        try:
            app_count = int(app_count)
        except ValueError:
            app_count = 0
        if app_count <= 0:
            # start Xquartz
            subprocess.check_call("open -a XQuartz", shell=True)
            time.sleep(5)
        # get default gateway device
        NET_DEVICE = subprocess.check_output(
            "route get default | grep 'interface: ' | head -1 | awk '{ print $2 }'", shell=True).decode("utf-8").split('\n')[0]
        print(f"X-Docker: Detected default gateway is: {NET_DEVICE}")
        # get ip
        NET_IP = subprocess.check_output(
            "ifconfig %s | grep inet | awk '$1==\"inet\" {print $2}'" % NET_DEVICE, shell=True).decode("utf-8").split('\n')[0]
        print(f"X-Docker: Detected gateway device IP is: {NET_IP}")
        # get display number
        DISPLAY_NO = subprocess.check_output(
            "ps -ef | grep \"Xquartz :\" | grep -v xinit | awk '{ print $9; }'", shell=True).decode("utf-8").split('\n')[0]
        print(f"X-Docker: Detected display number is: {DISPLAY_NO}")
        environment["DISPLAY"] = f"{NET_IP}{DISPLAY_NO}"
        # allow X-server to receive connections from current machine
        subprocess.check_call(f"xhost + {NET_IP}", shell=True)
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
    "XDockerMacOSConfigurator"
]
