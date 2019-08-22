from py_adb.adb import ADB
from py_adb.files import Files
from py_adb.element import Element
from py_adb.util import Path
from py_adb.by import By

import xml.etree.ElementTree as ElementTree
import os


class Layout:
    """
    Layout

    https://stackoverflow.com/questions/26586685/is-there-a-way-to-get-current-activitys-layout-and-views-via-adb
    """

    @staticmethod
    def _dump_layout(dev_id: str) -> str:
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

        :dev_id - Device Id:
        """
        
        path_layout = Layout._dump_layout(dev_id)
        if path_layout is not None:
            Files.pull(dev_id, path_layout, path_save)
            return os.path.join(path_save, path_layout.split("/")[2])
    
    @staticmethod
    def get_element(by: By, locator: str) -> Element:
        """
        Method to search Element in the XML layout, return dict with element

        TODO: Add Search Generic Search
        """

        path_to_xml = Path.DEFAULT_LAYOUT_XML.value
        assert isinstance(by, By)

        if by is by.ID:
            root = ElementTree.parse(path_to_xml).getroot()
            for child in root.iter():
                el_resource_id = child.attrib.get("resource-id")
                if el_resource_id is not None and len(el_resource_id) > 0 and locator in el_resource_id:
                    return Element(child)
        elif by is by.XPATH:
            root = ElementTree.parse(path_to_xml)
            # Bug in the xml.etree.ElementTree, remove . after bug will be fixed
            raw = root.find(".{}".format(locator))
            return Element(raw)
