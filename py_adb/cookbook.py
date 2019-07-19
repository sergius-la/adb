from py_adb.adb import ADB
from py_adb.package_info import PackageInfo
from py_adb.device_info import DeviceInfo
from py_adb.android_properties import Properties
from py_adb.android_packages import Package


class Info:
    """
    TODO: Module or Class for it
    """

    @staticmethod
    def get_environment(dev_id: str, package: str):
        """
        Method print into console
        - Device - id
        - Braand
        - Model
        
        - Package version

        :dev_id: device id
        :package: package

        TODO: Unit test
        """

        print("Device - {dev}".format(dev=dev_id))
        DeviceInfo.get_prop(dev_id, Properties.BRAND, Properties.MODEL)
        print()
        print("Package - {pac}".format(pac=package))
        package_versions = PackageInfo.get_package_version(dev_id, package)
        for version in package_versions:
            print("Version - {ver}".format(pac=package, ver=version))
    
    @staticmethod
    def get_packages_info(dev_id: str, *AndroidKPackages) -> list:
        """
        Return a list<Package>

        :dev_id: Device ID
        :*AndroidKPackage: AndroidPackage(enum)
        """

        packages = []
        for package in AndroidKPackages:
            package = Package(package.value.get("package"), package.value.get("App Name"), PackageInfo.get_package_version(dev_id, package.value.get("package")))
            packages.append(package)
        return packages

# if __name__ == "__main__":
    # package = "com.android.vending"
    # Info.get_environment(ADB.get_connected_devices()[0], package)

    # adb shell dumpsys package com.android.vending | grep version
    # adb shell dumpsys package com.google.android.youtube | grep version