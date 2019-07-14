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

# if __name__ == "__main__":
#     dev_id = ADB.get_connected_devices()[0]
#     ver = PackageInfo.get_package_version(dev_id, "com.android.vending")
#     # print(ver)
