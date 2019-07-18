from py_adb.device_manipulations import DeviceManipulations
from py_adb.android_keyevent import AndroidKeyevent
from py_adb.device_info import DeviceInfo
from py_adb.adb import ADB

class TestDeviceManipulations(object):
    
    devices = ADB.get_connected_devices()

    def test_open_close_notification_center(self):
        """
        Unit test to Perform open and close Notification Center
        """

        dev_id = self.devices[0]

        main = DeviceInfo.get_current_activity(self.devices[0])
        print(main)
        android_version = DeviceManipulations.open_notificastion_center(self.devices[0])
        notif = DeviceInfo.get_current_activity(self.devices[0])
        print(notif)

        out = DeviceManipulations.execute_keyevent(dev_id, AndroidKeyevent.BACK)

        main = DeviceInfo.get_current_activity(self.devices[0])
        print(main)

        assert False

