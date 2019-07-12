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
    def save_meminfo(dev_id: str, path: str, ps=""):
        """
        Method save meminfo into txt files
        :path: path to save file
        :ps: By default system, pid or package name
        TODO: Refactor, add Utility 
        """
        filename = "sys" if ps == "" else ps
        command = "adb -s {dev} shell dumpsys meminfo {ps} > {path}.txt".format(dev=dev_id, ps=ps, path = os.path.join(path, filename))
        ADB.exec_adb(command) 

    @staticmethod
    def get_package_activity(dev_id: str) -> dict:
        """
        Mwthod return dict{activity, package} from curecnt screen
        """

        command = "adb -s {dev} shell dumpsys window windows | grep -E 'mCurrentFocus'".format(dev=dev_id)
        output = ADB._get_terminal_output(command)[0]
        if "/" in output:
            raw = output.strip().split("/")
            activity = raw[1][:len(raw[1]) - 1:]
            package = raw[0].split(" ").pop()
            return {"activity" : activity, "package" : package}
        else:
            print("W: {}".format(output))
    
    @staticmethod
    def get_android_version(dev_id: str) -> str:
        """
        Return android version
        """

        command = "adb -s {dev} shell getprop ro.build.version.release ".format(dev=dev_id)
        return ADB._get_terminal_output(command)[0].strip()

if __name__ == "__main__":
    system_process = "com.android.systemui"
    # package =     
    dev_id = ADB.get_connected_devices()[0]
    

    print(DeviceInfo.get_android_version(dev_id))
    # meminfo = DeviceInfo.get_meminfo(dev_id, system_process)
    # for line in meminfo:
    #     if len(line) != 0:
    #         print(line)

    # print(dev_id)
    # pid = DeviceInfo.get_pid(dev_id, package)
    # print(pid)