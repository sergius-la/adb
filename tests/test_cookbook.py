from py_adb.adb import ADB
from py_adb.cookbook import Info
from py_adb.android_packages import AndroidKPackage

class TestCookbook(object):
    
    dev_id = ADB.get_connected_devices()[0]

    def test_packages_info(self):
        """
        Unit test to check return for Cookbook.get_packages_info()
        """
        
        packages = Info.get_packages_info(self.dev_id, AndroidKPackage.YOUTUBE, AndroidKPackage.PLAY_STORE)
        for package in packages:
            assert len(package.appName) > 0
            assert len(package.version) > 0
            assert len(package.package) > 0
