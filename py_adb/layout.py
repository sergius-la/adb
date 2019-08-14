from py_adb.adb import ADB
from py_adb.files import Files
from py_adb.element import Element
from py_adb.util import Path

import xml.etree.ElementTree as ET
import os


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
        raw_path = ADB.get_terminal_output(command)[0].strip()
        if "UI hierchary dumped to" in raw_path:
            return raw_path.split(":")[1].strip()
        else:
            print("E: {}".format(raw_path))
    
    @staticmethod
    def save_layout(dev_id: str, path_save: str) -> str:
        """
        Method save XML layout of current device screen, return path to saved file
        """
        
        path_layout = Layout.dump_layout(dev_id)
        if path_layout is not None:
            Files.pull(dev_id, path_layout, path_save)
            return os.path.join(path_save, path_layout.split("/")[2])
    
    @staticmethod
    def get_element(path_file: str, id: str) -> dict:
        """
        Method to search Element in the XML layout, return dict with element

        TODO: Add Search Generic Search
        """

        root = ET.parse(path_file).getroot()
        for child in root.iter():
            el_resource_id = child.attrib.get("resource-id")
            if el_resource_id is not None and len(el_resource_id) > 0 and id in el_resource_id:
                return Element(child)

# if __name__ == "__main__":
#     dev_id = ADB.get_connected_devices()[0]
# #
#     Layout.save_layout(dev_id, Path.PROC_FILES.value)
# #
# #     # [616, 48][720, 144]
# #
#     p = os.path.join(Path.PROC_FILES.value, "window_dump.xml")
#     elem = Layout.get_element(p, "com.google.android.youtube:id/mobile_topbar_avatar")
#     print(type(elem))
#     print(elem)
# #     # print(elem.get("resource-id"))
# #     element = Element(raw_elem)
# #     print(element._center_point)
#     elem.tap(dev_id)
# #     # print(element.tap(dev_id))
# #     #
# #     # print(x.get("bounds"))
