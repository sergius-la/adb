from py_adb.adb import ADB
from py_adb.android_packages import AndroidKPackage

# from adb import ADB
# from android_packages import AndroidKPackage

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
    def is_package_exist(dev_id, package) -> bool:
        """
        Method check is package installed on the device
        """

        check = "package:{pack}".format(pack=package)
        for pack in PackageInfo.get_list_packages(dev_id):
            print(pack)
            if check == pack.lower():
                return True
        return False
    
    @staticmethod
    def get_package_version(dev_id: str, package: str) -> str:
        """
        Return a package version

        :dev_id: device id
        :package: package name
        """

        command = "adb -s {dev_id} shell dumpsys package {package} | grep versionName".format(dev_id=dev_id, package=package)
        raw_out = ADB._get_terminal_output(command)
        versions = []
        for ver in raw_out:
            versions.append(ver.strip().split("=")[1])
        return versions

if __name__ == "__main__":
    dev_id = ADB.get_connected_devices()[0]

    # x = PackageInfo.get_packages_version(dev_id, AndroidKPackage.YOUTUBE)