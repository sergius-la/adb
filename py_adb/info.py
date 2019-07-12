from py_adb.adb import ADB
from py_adb.package_info import PackageInfo

class Info:

    @staticmethod
    def get_environment(dev_id: str, package: str):
        """
        Method print into console
        - TODO: Android version
        - TODO: Device model
        - Package version

        :dev_id: device id
        :package: package

        TODO: Unit test
        """

        package_ver = PackageInfo.get_packahe_version(package)
        print("{pac} - version - {ver}".format(pac=package, ver=package_ver))