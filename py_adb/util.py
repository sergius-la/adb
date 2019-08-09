from enum import Enum, auto
import os


class Identify(object):

    # Paths
    _root = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
    _package = os.path.abspath(os.path.dirname(__file__))
    _test_files = os.path.join(_root, "tests", "test_files")
    _proc_files = os.path.join(_root, "proc_files")

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
    def path_proc_files():
        return Identify._proc_files   


class Path(Enum):
    TEST_FILES = Identify.path_test_files()
    PY_ADB = Identify.path_package()
    ROOT = Identify.path_root()
    PROC_FILES = Identify.path_proc_files()
