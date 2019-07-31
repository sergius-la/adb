# from py_adb.adb import ADB

from adb import ADB

class UserActions:

    @staticmethod
    def swipe(dev_id: str, x1: int, y1: int, x2: int ,y2: int):
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

        command = "adb -s {dev_id} shell input text {text}".format(dev_id=dev_id, text=text.strip().replace(" ", "%s")) # %s - Space
        ADB.exec_adb(command)