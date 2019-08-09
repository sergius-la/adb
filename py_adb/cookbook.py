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
        - Brand
        - Model
        
        - Package version

        :dev_id: device id
        :package: package

        TODO: Unit test
        """

        print("Device - {dev}".format(dev=dev_id))
        properties = DeviceInfo.get_prop(dev_id, Properties.BRAND, Properties.MODEL)
        for prop, value in properties.items():
            print("{} - {}".format(prop, value))
        print()
        print("Package - {pac}".format(pac=package))
        package_versions = PackageInfo.get_package_version(dev_id, package)
        for version in package_versions:
            print("Version - {ver}".format(pac=package, ver=version))
    
    @staticmethod
    def get_packages_info(dev_id: str, *android_packages) -> list:
        """
        Return a list<Package>

        :dev_id: Device ID
        :*AndroidKPackage: AndroidPackage(enum)
        """

        # TODO: Add check for each package
        # assert android_packages isinstance(Package)

        packages = []
        for package in android_packages:
            package = Package(package.value.get("package"), package.value.get("App Name"),
                              PackageInfo.get_package_version(dev_id, package.value.get("package")))
            packages.append(package)
        return packages

# if __name__ == "__main__":
#     package = "com.android.vending"
#     Info.get_environment(ADB.get_connected_devices()[0], package)

    # adb shell dumpsys package com.android.vending | grep version
    # adb shell dumpsys package com.google.android.youtube | grep version
