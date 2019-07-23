from py_adb.util import Path

class TestUtil(object):

    def test_path(self):

        for p in Path:
            assert len(p.value) > 0