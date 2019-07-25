from py_adb.util import Path

import os

class TestUtil(object):

    def test_path(self):
        """
        Unit tests for Util Path class, each value shoud be a path to the host dir
        """

        for p in Path:
            assert len(p.value) > 0
            assert os.path.isdir(p.value)