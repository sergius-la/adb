from py_adb.device_info import DeviceInfo
from py_adb.adb import ADB

class TestDeviceInfo(object):
    
    devices = ADB.get_connected_devices()

    def test_android_version(self):
        """
        Unit test for Android version
        """

        assert len(DeviceInfo.get_android_version(self.devices[0])) > 0