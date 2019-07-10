from adb.adb import ADB

class TestADB(object):
    
    def test_get_connected_devices(self):
        
        devices = ADB.get_connected_devices()
        print("NOTE: Execute test with connected devices")
        print("E: Found Devices {}".format(devices))
        assert len(devices) > 0