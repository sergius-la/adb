from adb import ADB

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