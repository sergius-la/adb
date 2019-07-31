import xml.etree.ElementTree as ET
import os

from py_adb.adb import ADB
from py_adb.files import Files
from py_adb.util import Path
from py_adb.user_actions import UserActions
from py_adb.element import Element

# from adb import ADB
# from files import Files
# from util import Path
# from user_actions import UserActions
# from element import Element

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
    
    @staticmethod
    def search_element(path_file: str, id: str) -> dict:
        """
        Method to search Element in the XML layout, return dict with element

        TODO: Add element cast
        """

        root = ET.parse(path_file).getroot()
        for child in root.iter():
            el_resource_id = child.attrib.get("resource-id")
            if el_resource_id is not None and len(el_resource_id) > 0 and id in el_resource_id:
                return child
    
    @staticmethod
    def cast_to_element(path_file: str, id: str):
        """
        TEST MODE method
        """
        
        raw_element = Layout.search_element(path_file, id)
        el = Element(raw_element)
        print(el)
        return el
        




if __name__ == "__main__":
    # dev_id = ADB.get_connected_devices()[0]

    # Layout.get_layout(dev_id, Path.PROC_FILES.value)
    # path_to_file = os.path.join( Path.PROC_FILES.value, "window_dump.xml")
    # x = Layout.get_element_center_point(path_to_file, "com.android.vending:id/play_search_container")
    
    Layout.cast_to_element(Path.PROC_FILES.value, "com.android.vending:id/play_search_container")

    # print(x.get("bounds"))