from py_adb.adb import ADB
from py_adb.package_info import PackageInfo
from py_adb.device_info import DeviceInfo
from py_adb.android_properties import Properties

class Cockbook:

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
        def get_packages_version(dev_id: str, *AndroidKPackages) -> dict:
            """
            Return a dict{package:<App Name - str>, version:<str>/<list>}

            :dev_id: Device ID
            :*AndroidKPackage: AndroidPackage(enum)
            """

            versions = {}
            for package in AndroidKPackages:
                packID = package.value.get("package")
                print(packID)
                app_name = package.value.get("App Name")
                print(app_name)
                pack_version = PackageInfo.get_package_version(dev_id, packID)
                print(pack_version)
                versions[package] = app_name
                versions["version"] = pack_version
            return versions

if __name__ == "__main__":
    package = "com.android.vending"
    Info.get_environment(ADB.get_connected_devices()[0], package)

    # adb shell dumpsys package com.android.vending | grep version
    # adb shell dumpsys package com.google.android.youtube | grep version