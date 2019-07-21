from py_adb.device_info import DeviceInfo
from py_adb.adb import ADB
from py_adb.android_properties import Properties

class TestDeviceInfo(object):
    
    devices = ADB.get_connected_devices()

    def test_android_version(self):
        """
        Unit test for Android version
        Return Example - Android Version 6.0.1
        """

        android_version = DeviceInfo.get_prop(self.devices[0], Properties.ANDROID_VERSION)
        print(android_version)
        assert isinstance(android_version, dict)
        version = android_version.get("Android Version") 
        assert len(version) > 0

    def test_getprop(self):
        """
        Unit test for all getprop shoud return in dict
        """

        getprop = DeviceInfo.all_getprop(self.devices[0])
        assert isinstance(getprop, dict)
        assert len(getprop) > 0
    
    def test_is_locked(self):

        res = DeviceInfo.is_locked(self.devices[0])
        print(res)
        assert False