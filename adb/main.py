from adb import ADB

if __name__ == "__main__":
    dev_id = ADB.get_connected_devices()[0]
    print("I: Device - ".format(dev_id))

    