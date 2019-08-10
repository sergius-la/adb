from py_adb.device_info import DeviceInfo
from py_adb.adb import ADB
from py_adb.android_properties import Properties


class TestDeviceInfo(object):
    
    _devices = ADB.get_connected_devices()
    assert len(_devices) > 0, "Check connected Device"
    device = _devices[0]

    def test_android_version(self):
        """
        Unit test for Android version
        Return Example - Android Version 6.0.1
        """

        android_version = DeviceInfo.get_prop(self.device, Properties.ANDROID_VERSION)
        print(android_version)
        assert isinstance(android_version, dict)
        version = android_version.get("Android Version") 
        assert len(version) > 0

    def test_getprop(self):
        """
        Unit test for all getprop should return in dict
        """

        getprop = DeviceInfo.all_getprop(self.device)
        assert isinstance(getprop, dict)
        assert len(getprop) > 0
