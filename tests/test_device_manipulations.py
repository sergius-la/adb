from py_adb.device_manipulations import DeviceManipulations, UnlockType
from py_adb.android_keyevent import AndroidKeyevent
from py_adb.device_info import DeviceInfo
from py_adb.files import Files
from py_adb.adb import ADB

import os
import time


class TestDeviceManipulations(object):
    test_files_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_files")
    _devices = ADB.get_connected_devices()
    assert len(_devices) > 0, "Check connected Device"
    device = _devices[0]

    def test_open_close_notification_center(self):
        """
        Unit test to Perform open and close Notification Center
        TODO: Fix the test
        """

        if DeviceInfo.is_locked:
            DeviceManipulations.unlock_device(self.device, UnlockType.SWIPE)

        DeviceManipulations.open_notification_center(self.device)
        current_activity = DeviceInfo.get_current_activity(self.device)
        assert current_activity.get("activity") == "StatusBar"

        DeviceManipulations.execute_keyevent(self.device, AndroidKeyevent.BACK)
        current_activity = DeviceInfo.get_current_activity(self.device)
        assert current_activity.get("activity") == "com.sec.android.app.launcher.activities.LauncherActivity"

    def test_lock_device(self):
        """
        Unit test for device lock
        """

        DeviceManipulations.lock_device(self.device)
        time.sleep(1)
        lock_status = DeviceInfo.is_locked(self.device)
        print("Device lock status - {}".format(lock_status))
        assert lock_status

    def test_save_screenshot(self):
        """
        Unit test for save_screenshot
        """

        if DeviceInfo.is_locked:
            DeviceManipulations.unlock_device(self.device, UnlockType.SWIPE)

        test_device_path = "/sdcard/sc2.png"
        test_file_name = "sc2.png"

        Files.clear_dir(self.test_files_dir)

        DeviceManipulations.save_screenshot(self.device, "/sdcard/sc2.png", self.test_files_dir)
        assert os.path.isfile(os.path.join(self.test_files_dir, test_file_name))

    def test_unlock_device(self):
        """
        Unit test for unlock the device
        """

        if not DeviceInfo.is_locked:
            DeviceManipulations.lock_device(self.device)

        DeviceManipulations.unlock_device(self.device, UnlockType.SWIPE)
        assert not DeviceInfo.is_locked(self.device)
