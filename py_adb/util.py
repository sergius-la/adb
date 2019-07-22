from enum import Enum, auto
import os

class Identify(object):

    @staticmethod
    def paths():    
        root = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
        package = os.path.abspath(os.path.dirname(__file__))
        test_files = os.path.join(package, "tests", "test_files")
        return {"root":root, "package":package, "test_files":test_files}        

class Path(Enum):
    _paths = Identify.paths()
    TEST_FILES = _paths.get("test_files")
    PY_ADB = _paths.get("package")
    ROOT = _paths.get("root")