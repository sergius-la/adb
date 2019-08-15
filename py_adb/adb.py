import os


class ADB:
    
    @staticmethod
    def exec_adb(command):
        output = ADB.get_terminal_output(command)
        if len(output) > 0:
            print(output)
    
    @staticmethod
    def get_connected_devices(is_connected=False) -> list:
        """
        Method return list() of connected authorized devices ids.
        """

        command = "adb devices"
        devices = []
        raw_out = ADB.get_terminal_output(command)
        for line in raw_out:
            if "device" in line and "devices" not in line:
                devices.append(line.split()[0])
        
        if (is_connected):
            assert len(devices) > 0, "Connected Devices not Found"
        return devices

    @staticmethod
    def get_terminal_output(command: str) -> list:
        """
        :command: executable terminal command
        """

        return os.popen(command).readlines()
