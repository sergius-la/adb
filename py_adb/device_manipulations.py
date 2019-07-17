from adb import ADB
from files import Files
from user_actions import UserActions
from device_info import DeviceInfo

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
    def get_screenshot(dev_id: str, path_device: str, path_save: str, delete=False):
        """
        Return path to saved screenshot file

        :dev_id: Device ID
        :path_device: Path to save on the device
        :path_save: Path to save on the Desctop
        :delete: - False (dafault) do not save file on the device
                 - True save file on the device 

        TODO: Test
        TODO: Add Flag to delete file after save
        """

        DeviceManipulations.screenshot(dev_id, path_device)
        Files.pull(dev_id, path_device, path_save)

        if delete is True:
            pass
        
    @staticmethod
    def open_notificastion_center(dev_id):
        """
        Method perform horizontal swipe to open notification center
        TODO: Add Check if notification center is open

        :dev_id: Device ID
        """
        size = DeviceInfo.get_display_size(dev_id)
        x = int(size.get("width")) / 2
        y2 = int(size.get("hight")) / 2
        UserActions.swipe(dev_id, x, 1, x, y2)