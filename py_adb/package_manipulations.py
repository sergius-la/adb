from adb import ADB
from android_prmissions import AndroidPermissions

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
    def start_package(dev_id: str, package: str):
        """
        Method to start package

        TODO: Test
        """

        command = "adb -s {dev_id} shell am startservice {package}".format(dev_id=dev_id, package=package)
        ADB.exec_adb(command)

        
    @staticmethod
    def grant_permission(dev_id: str, package: str, *AndroidPermissions):
        """
        Method to grant permissions for package
        TODO: Unit Test

        :dev_id: device id
        :package: package name
        :permission: permission
        """

        for permission in AndroidPermissions:
            command = "adb -s {dev} shell pm grant {package} {permission}".format(dev=dev_id, package=package, permission=permission.value.get("perm"))
            out = ADB._get_terminal_output(command)
            if len(out) > 0:
                print(out)
            print("I: Prmissions {perm} has been granted to Device ID {dev} for package {package}".format(perm=permission.value.get("name"), dev=dev_id, package=package))

    @staticmethod
    def revoke_permission(dev_id: str, package: str, *AndroidPermissions):
        """
        Method to grant permissions for package
        TODO: Unit Test

        :dev_id: device id
        :package: package name
        :permission: permission
        """

        for permission in AndroidPermissions:
            command = "adb -s {dev} shell pm revoke {package} {permission}".format(dev=dev_id, package=package, permission=permission.value.get("perm"))
            out = ADB._get_terminal_output(command)
            if len(out) > 0:
                print(out)
            else:
                print("I: Prmissions {perm} has been revoke to Device ID {dev} for package {package}".format(perm=permission.value.get("name"), dev=dev_id, package=package))

if __name__ == "__main__":
    dev_id = ADB.get_connected_devices()[0]
    package = "com.google.android.youtube"
    # print(AndroidPermissions.CAMERA.value.get("perm"))
    PackageManipulations.grant_permission(dev_id, package, AndroidPermissions.CAMERA, AndroidPermissions.LOCATION)
    # PackageManipulations.revoke_permission(dev_id, package, AndroidPermissions.CAMERA, AndroidPermissions.LOCATION)