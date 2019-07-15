from adb import ADB
from package_info import PackageInfo
from device_info import DeviceInfo
from android_properties import Properties


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

if __name__ == "__main__":
    package = "com.android.vending"
    Info.get_environment(ADB.get_connected_devices()[0], package)

    # adb shell dumpsys package com.android.vending | grep version
    # adb shell dumpsys package com.google.android.youtube | grep version