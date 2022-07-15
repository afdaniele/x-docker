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
            "ps aux | grep $APP_NAME | grep -v grep | wc -l | awk '{print $1}'", shell=True)
        try:
            app_count = int(app_count)
        except ValueError:
            app_count = 0
        if app_count <= 0:
            # start Xquartz
            subprocess.check_call("open -a XQuartz")
            time.sleep(4)
        # get default gateway device
        NET_DEVICE = subprocess.check_output(
            "route get default | grep 'interface: ' | head -1 | awk '{ print $2 }'")
        # get ip
        NET_IP = subprocess.check_output(
            "ifconfig %s | grep inet | awk '$1==\"inet\" {print $2}'" % NET_DEVICE)
        # get display number
        DISPLAY_NO = subprocess.check_output(
            "ps - ef | grep \"Xquartz :\" | grep -v xinit | awk '{ print $9; }'")
        environment["DISPLAY"] = DISPLAY_NO
        # allow X-server to receive connections from current machine
        subprocess.check_call(f"xhost + {NET_IP}")
        # ---
        config["environment"] = environment
        return config


__all__ = [
    "XDockerMacOSConfigurator"
]
