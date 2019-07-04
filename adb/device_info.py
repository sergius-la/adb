from adb import ADB

class DeviceInfo:

    @staticmethod
    def get_pid(dev_id: str, ps: str) -> str:
        """
        Method return pid of package of process
        :dev_id: device id
        :ps: process or package name
        
        TODO: Fix for processes with multiple PIDs
        """
        command = "adb -s {dev} shell ps | grep {ps} | cut -d ' ' -f 4".format(dev=dev_id, ps=ps)
        print(command)
        pid = ADB._get_terminal_output(command)
        return pid[0].strip() if len(pid) > 0 else ""
    
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
    def save_meminfo(dev_id, path, ps=""):
        """
        Method save meminfo into txt files
        :path: path to save file
        :ps: By default system, pid or package name
        TODO: Refactor, add Utility 
        """
        filename = "sys" if ps == "" else ps
        command = "adb -s {dev} shell dumpsys meminfo {ps} > {path}.txt".format(dev=dev_id, ps=ps, path = os.path.join(path, filename))
        exec_adb(command) 

if __name__ == "__main__":
    system_process = "com.android.systemui"
    # package =     
    dev_id = ADB.get_connected_devices()[0]
    
    # meminfo = DeviceInfo.get_meminfo(dev_id, system_process)
    # for line in meminfo:
    #     if len(line) != 0:
    #         print(line)

    # print(dev_id)
    # pid = DeviceInfo.get_pid(dev_id, package)
    # print(pid)