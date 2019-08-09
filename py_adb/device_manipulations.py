from py_adb.adb import ADB
from py_adb.files import Files
from py_adb.device_info import DeviceInfo
from py_adb.android_keyevent import AndroidKeyevent

from enum import Enum, auto


class UnlockType(Enum):
    SWIPE = auto()


class DeviceManipulations:

    @staticmethod
    def set_screen_brightness(dev_id: str, value):
        """
        Method to change screen brightness on the device in range - 0 to 255
        """
        
        if value > 255:
            value = 255
        if value < 0:
            value = 0

        command = "adb -s {dev_id} shell settings put system screen_brightness {value}".format(dev_id=dev_id, value=value)
        ADB.exec_adb(command)
    
    @staticmethod
    def screenshot(dev_id: str, path_save: str):
        """
        Make a screenshot

        TODO: Test 
        """

        command = "adb -s {dev_id} shell screencap {path}".format(dev_id=dev_id, path=path_save)
        ADB.exec_adb(command)
    
    @staticmethod
    def save_screenshot(dev_id: str, path_device: str, path_save: str, delete=False):
        """
        Return path to saved screenshot file

        :dev_id: Device ID
        :path_device: Path to save on the device
        :path_save: Path to save on the Desctop
        :delete: - False (dafault) do not save file on the device
                 - True save file on the device 
        """

        DeviceManipulations.screenshot(dev_id, path_device)
        Files.pull(dev_id, path_device, path_save)

        if delete is True:
            pass
        
    @staticmethod
    def open_notification_center(dev_id):
        """
        Method perform horizontal swipe to open notification center
        TODO: Add Check if notification center is open

        :dev_id: Device ID
        """
        size = DeviceInfo.get_display_size(dev_id)
        x = int(size.get("width")) / 2
        y2 = int(size.get("height")) / 2
        DeviceManipulations.swipe(dev_id, x, 1, x, y2)

    @staticmethod
    def execute_keyevent(dev_id, android_keyevent):
        """
        Method to execute Keyevent

        :dev_id: Device ID
        :android_keyevent: Android KeyEvent
        """

        command = "adb -s {dev_id} shell input keyevent {keycode}".format(
            dev_id=dev_id, keycode=android_keyevent.value.get("key_code"))
        ADB.exec_adb(command)
    
    @staticmethod
    def lock_device(dev_id: str):
        """
        Method to lock the device

        :dev_id: Device ID
        """
        DeviceManipulations.execute_keyevent(dev_id, AndroidKeyevent.POWER_BUTTON)
    
    @staticmethod
    def unlock_device(dev_id: str, unlock_type):
        """
        Method to unlock the device

        :dev_id: Device ID
        """
        is_locked = DeviceInfo.is_locked(dev_id)
        if is_locked:
            DeviceManipulations.execute_keyevent(dev_id, AndroidKeyevent.WAKEUP)
            if unlock_type.SWIPE:
                display_sie = DeviceInfo.get_display_size(dev_id)
                x = display_sie.get("width") / 2
                y = display_sie.get("height")
                DeviceManipulations.swipe(dev_id, x, y * 0.10, x, y * 0.80)

    @staticmethod
    def swipe(dev_id: str, x1: int, y1: int, x2: int, y2: int):
        """
        Method for perform swipe by coordinates
        """

        command = "adb -s {dev_id} shell input swipe {x1} {y1} {x2} {y2}".format(dev_id=dev_id, x1=x1, y1=y1, x2=x2, y2=y2)
        ADB.exec_adb(command)

    @staticmethod
    def tap(dev_id: str, x: int, y: int):
        """
        Method for perform tap by coordinates
        """

        command = "adb -s {dev_id} shell input tap {x} {y}".format(dev_id=dev_id, x=x, y=y)
        ADB.exec_adb(command)
    
    @staticmethod
    def send_text(dev_id: str, text: str):
        """
        Method perform typing text
        NOTE: Before use, make sure input text field in selected
        """

        command = "adb -s {dev_id} shell input text {text}".format(
            dev_id=dev_id, text=text.strip().replace(" ", "%s"))  # %s - Space
        ADB.exec_adb(command)
