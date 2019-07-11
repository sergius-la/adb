import os

from adb import ADB
from files import Files

class Layout:

    """
    Layout

    https://stackoverflow.com/questions/26586685/is-there-a-way-to-get-current-activitys-layout-and-views-via-adb
    """

    @staticmethod
    def dump_layout(dev_id: str) -> str:
        """
        Method call the uiautomator to dump screen layout and Return path to it
        :dev_id: device id
        """

        command = "adb -s {dev_id} shell uiautomator dump".format(dev_id=dev_id)
        raw_path = ADB._get_terminal_output(command)[0].strip()
        if "UI hierchary dumped to" in raw_path:
            return raw_path.split(":")[1].strip()
        else:
            print("E: {}".format(raw_path))
    
    @staticmethod
    def get_layout(dev_id: str, path_save: str) -> str:
        """
        Method save XML layout of current device screen, return path to saved file
        """
        
        path_layout = Layout.dump_layout(dev_id)
        if path_layout is not None:
            Files.pull(dev_id, path_layout, path_save)
            return os.path.join(path_save, path_layout.split("/")[2])

# if __name__ == "__main__":
#     package_root = os.path.abspath(os.path.dirname(__file__))
#     print("Root {}".format(package_root))