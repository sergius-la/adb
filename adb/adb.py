import os

class ADB:
    
    @staticmethod
    def exec_adb(command):
        output = ADB._get_terminal_output(command)
        if len(output) > 0:
            print(output)
    
    @staticmethod
    def get_connected_devices() -> list:
        """
        Method return list() of connected authorized devices ids.
        """

        command = "adb devices"
        devices = []
        raw_out = ADB._get_terminal_output(command)
        for line in raw_out:
            if "device" in line and "devices" not in line:
                devices.append(line.split()[0])
        
        if len(devices) == 0:
            print("W: Check connected devices")

        return devices

    @staticmethod
    def _get_terminal_output(command: str) -> list:
        """
        :command: executable terminal command
        """

        return os.popen(command).readlines()