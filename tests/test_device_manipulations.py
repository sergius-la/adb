from py_adb.device_manipulations import DeviceManipulations
from py_adb.device_info import DeviceInfo
from py_adb.adb import ADB

class TestDeviceManipulations(object):
    
    devices = ADB.get_connected_devices()

    def test_open_notification_center(self):
        """
        Unit test to Perform Open Notification Center
        """

        main = DeviceInfo.get_package_activity(self.devices[0])
        print(main)
        android_version = DeviceManipulations.open_notificastion_center(self.devices[0])
        notif = DeviceInfo.get_package_activity(self.devices[0])
        print(notif)
        assert False

