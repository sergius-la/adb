from py_adb.device_manipulations import DeviceManipulations
from py_adb.android_keyevent import AndroidKeyevent
from py_adb.device_info import DeviceInfo
from py_adb.files import Files
from py_adb.adb import ADB

import os

class TestDeviceManipulations(object):
    
    test_files_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_files")
    devices = ADB.get_connected_devices()
    dev_id = devices[0]

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
    
    def test_save_screenshot(self):
        """
        Unit test for save_screenshot
        """
        
        test_device_path = "/sdcard/sc2.png"
        test_file_name = "sc2.png"

        Files.clear_dir(self.test_files_dir)

        DeviceManipulations.save_screenshot(self.dev_id, "/sdcard/sc2.png", self.test_files_dir)
        assert os.path.isfile(os.path.join(self.test_files_dir, test_file_name))