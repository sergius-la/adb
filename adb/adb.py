import os

class ADB:
    """
    TODO: Make ADB abstract

    TODO: User Actions Class
    
    TODO: Device manipulation
        - Bluetoth On/Off
        - Grand / Revoke Permissions - https://stackoverflow.com/questions/16410167/how-do-i-use-adb-grant-or-adb-revoke

    TODO: Device Information
        - DUMP layout
    """

    @staticmethod
    def exec_adb(command):
        output = ADB._get_terminal_output(command)
        if len(output) > 0:
            print(output)
    
    @staticmethod
    def swipe(dev_id, x1, y1, x2 ,y2):
        """
        User actions 
            - Method for swipe by coordinates
        """

        command = "adb -s {dev_id} shell input swipe {x1} {y1} {x2} {y2}".format(dev_id=dev_id, x1=x1, y1=y1, x2=x2, y2=y2)
        exec_adb(command)

    @staticmethod
    def tap(dev_id, x, y):
        """
        User actions
            - Method for tap by coordinates
        TODO: Test
        """

        command = "adb -s {dev_id} shell inout tap {x} {y}".format(dev_id=dev_id, x=x, y=y)
        exec_adb(command)

    @staticmethod
    def save_meminfo(dev_id, path, ps=""):
        """
        Method save meminfo into txt files
        :path: path to save file
        :ps: By default system, pid or package name
        TODO: Refactor, add Utility 
        """
        filename = "sys" if ps == "" else ps
        command = "adb -s {dev} shell dumpsys  meminfo {ps} > {path}.txt".format(dev=dev_id, ps=ps, path = os.path.join(path, filename))
        exec_adb(command)

    @staticmethod
    def get_meminfo(dev_id, ps="") -> list:
        """
        Method return dumpsys meminfo memory snapshot, by default will return system memory
        :dev_id: device id
        :ps: pid or process name
        """

        command = "adb -s {dev} shell dumpsys  meminfo {ps}".format(dev=dev_id, ps=ps)
        return ADB._get_terminal_output(command)

    @staticmethod
    def get_pid(dev_id: str, ps: str) -> str:
        """
        Method return pid of package of process
        :dev_id: device id
        :ps: process or package name
        """
        command = "adb -s {dev} shell ps | grep {ps} | cut -d ' ' -f 4".format(dev=dev_id, ps=ps)
        pid = ADB._get_terminal_output(command)
        return pid[0].strip() if len(pid) > 0 else ""

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
        return devices

    """
    Device Manipulation
    """
    
    @staticmethod
    def set_screen_brightness(dev_id: str, value):
        """
        Method to change screen brightness on the device in range - 0 to 255
        """
        
        if value > 255:
            value = 255
        if value < 0:
            value = 0

        command = "adb -s {dev_id} shell settings put system screen_brightness {value}".format(dev_id=dev_id, value=value)
        ADB.exec_adb(command)

    """
    Device Manipulation
    """
    
    @staticmethod
    def _get_terminal_output(command: str) -> list:
        """
        :command: executable terminal command
        """

        return os.popen(command).readlines()


if __name__ == "__main__":
    dev_id = ADB.get_connected_devices()[0]
    # ADB.swipe(dev_id, 370, 1200, 370, 160)
    print(dev_id)
    ADB.set_screen_brightness(dev_id, -10)
    ADB.set_screen_brightness(dev_id, 300)
            