import os

from py_adb.adb import ADB
from py_adb.layout import Layout
from py_adb.files import Files
from py_adb.util import Path

class TestLayout(object):
    """
    Unit Tests for Layout
    """

    base_layout = "window_dump.xml"   
    
    def test_get_layout(self):
        # TODO: Make a generator
        Files.clear_dir(Path.TEST_FILES.value)

        dev_id = ADB.get_connected_devices()[0]
        print("I: Device - {}".format(dev_id))
        path_to_file = Layout.save_layout(dev_id, Path.TEST_FILES.value)
        print("I: Path to file - {}".format(path_to_file))
        assert os.path.isfile(path_to_file)