from py_adb.util import Path

class TestUtil(object):

    def test_path(self):

        for p in Path:
            print(p.value)
            assert len(p.value) > 0
            assert False