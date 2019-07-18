from py_adb.adb import ADB
from py_adb.package_info import PackageInfo
from py_adb.android_packages import AndroidKPackage

class TestPackageInfo(object):
    
    dev_id = ADB.get_connected_devices()[0]  

    def test_is_package_exist(self):
        
        notExist = PackageInfo.is_package_exist(self.dev_id, "com.android.not_a_package")
        assert notExist is False
        exist = PackageInfo.is_package_exist(self.dev_id, "com.android.vending")
        assert exist is True
    
    def test_get_packages_version(self):

        versions = PackageInfo.get_packages_version(self.dev_id, AndroidKPackage.PLAYMARKET, AndroidKPackage.YOUTUBE)
        print(versions)
        for k, v in versions.items():
            print("W: Values <{}>".format(v))
            assert len(v) > 0
            assert False 