from adb import ADB

class PackageInfo:

    @staticmethod
    def get_list_packages(dev_id: str) -> list:
        """
        Return a list of installed packages on the device
        """

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

