import os
from adb_commands import Commands

class ADB:

    @staticmethod
    def exec_adb(dev_id):
        pass

    @staticmethod
    def get_connected_devices() -> list:
        """
        Method return list() of connected authorized devices ids.
        """

        devices = []
        raw_out = ADB._get_terminal_output(Commands.DEVICES.value)
        for line in raw_out:
            if "device" in line and "devices" not in line:
                devices.append(line.split()[0])
        return devices
    
    @staticmethod
    def _get_terminal_output(command: str) -> list:
        """
        :command: executable terminal command
        """

        return os.popen(command).readlines()