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

    """
    ADB
    """

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
        return devices

    @staticmethod
    def _get_terminal_output(command: str) -> list:
        """
        :command: executable terminal command
        """

        return os.popen(command).readlines()

    """
    ADB
    """

    """
    Device Actions
    """

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

    """
    Device Actions
    """

    """
    Device Information
    """

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

    """
    Device Information
    """

    """
    Package Information
    """

    @staticmethod
    def get_list_packages(dev_id: str) -> list:
        command = "adb -s {dev_id} shell pm list packages".format(dev_id=dev_id)
        raw_packages = ADB._get_terminal_output(command)
        return [x.strip() for x in raw_packages]
    
    @staticmethod
    def get_packahe_version(dev_id: str, package: str) -> str:
        """
        Return a package version
        
        :dev_id: device id
        :package: package name
        """

        command = "adb -s {dev_id} shell dumpsys package {package} | grep versionName".format(dev_id=dev_id, package=package)
        return ADB._get_terminal_output(command)[0].strip().split("=")[1]

    """
    Package Information
    """

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

if __name__ == "__main__":
    dev_id = ADB.get_connected_devices()[0]
    print("I: Working with {}".format(dev_id))
    # packages = ADB.get_list_packages(dev_id)
    # for pac in packages:
        # print(pac)
    package = "com.android.systemui"
    x = ADB.get_packahe_version(dev_id, package) 
    print(x)   