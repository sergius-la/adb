import os

from py_adb.adb import ADB
from py_adb.layout import Layout
from py_adb.files import Files

class TestLayout(object):
    """
    Unit Tests for Layout
    """

    test_files = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test_files")
    base_layout = "window_dump.xml"   
    
    def test_get_layout(self):
        # TODO: Make a generator
        Files.clear_dir(self.test_files)

        dev_id = ADB.get_connected_devices()[0]
        print("I: Device - {}".format(dev_id))
        path_to_file = Layout.get_layout(dev_id, self.test_files)
        print(path_to_file)
        assert os.path.isfile(path_to_file)