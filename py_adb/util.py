from enum import Enum, auto
import os


class Identify(object):

    # Paths
    _root = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
    _package = os.path.abspath(os.path.dirname(__file__))
    _test_files = os.path.join(_root, "tests", "test_files")
    _processing_files = os.path.join(_root, "processing_files")
    _default_layout = os.path.join(_processing_files, "window_dump.xml")

    @staticmethod
    def path_root():
        return Identify._root

    @staticmethod
    def path_package():
        return Identify._package

    @staticmethod
    def path_test_files():
        return Identify._test_files     

    @staticmethod
    def path_processing_files():
        if not os.path.exists(Identify._processing_files):
            os.makedirs(Identify._processing_files)
        return Identify._processing_files

    @staticmethod
    def path_default_layout():
        return Identify._default_layout


class Path(Enum):
    TEST_FILES = Identify.path_test_files()
    PY_ADB = Identify.path_package()
    ROOT = Identify.path_root()
    PROCESSING_FILES = Identify.path_processing_files()
    DEFAULT_LAYOUT_XML = Identify.path_default_layout()
