import os

class ADB:

    @staticmethod
    def exec_adb(dev_id):
        pass

    @staticmethod
    def save_meminfo(dev_id, path, ps=""):
        """
        Method save meminfo into txt files
        :path: path to save file
        :ps: By default system, pid or package name
        """
        filename = "sys" if ps == "" else ps
        command = "adb -s {dev} shell dumpsys  meminfo {ps} > {path}.txt".format(dev=dev_id, ps=ps, path = os.path.join(path, filename))
        ADB._get_terminal_output(command)

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
        command = "adb -s {dev} shell ps | grep {ps} | cut -d ' ' -f 5".format(dev=dev_id, ps=ps)
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
    
    @staticmethod
    def _get_terminal_output(command: str) -> list:
        """
        :command: executable terminal command
        """

        return os.popen(command).readlines()


if __name__ == "__main__":
    dev_id = ADB.get_connected_devices()[0]
    ADB.save_meminfo(dev_id, "/Users/Admin/Desktop/Projects/adb", "com.android.vending")
            