from adb import ADB

class UserActions:

    @staticmethod
    def swipe(dev_id, x1, y1, x2 ,y2):
        """
        Method for perform swipe by coordinates
        """

        command = "adb -s {dev_id} shell input swipe {x1} {y1} {x2} {y2}".format(dev_id=dev_id, x1=x1, y1=y1, x2=x2, y2=y2)
        ADB.exec_adb(command)

    @staticmethod
    def tap(dev_id, x, y):
        """
        Method for perform tap by coordinates
        """

        command = "adb -s {dev_id} shell inout tap {x} {y}".format(dev_id=dev_id, x=x, y=y)
        ADB.exec_adb(command)