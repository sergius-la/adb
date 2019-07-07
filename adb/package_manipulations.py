from adb import ADB

class PackageManipulations:
    
    @staticmethod
    def clear_package_cache(dev_id, package):
        """
        Method to clean app cashe
        :dev_id: device id
        :package: package name
        """

        command = "adb -s {dev_id} shell pm clear {package}".format(dev_id=dev_id, package=package)
        ADB.exec_adb(command)

    @staticmethod
    def install_app(dev_id, path_package):
        """
        Method to install package to the device.

        TODO: App ENUM Flags -d, -r
        TODO: Test
        TODO: Check path
        """
        
        command = "adb -s {dev_id} install {path}".format(dev_id=dev_id, path=path_package)
        ADB.exec_adb(command)

    @staticmethod
    def close_package(dev_id, package):
        """
        Method to close package

        TODO: Test
        """

        command = "adb -s {dev_id} shell am force-stop {package}".format(dev_id, dev_id, package=package)
        ADB.exec_adb(command)

    @staticmethod
    def start_package(dev_id, package):
        """
        Method to start package

        TODO: Test
        """

        command = "adb -s {dev_id} shell am startservice {package}".format(dev_id=dev_id, package=package)
        ADB.exec_adb(command)