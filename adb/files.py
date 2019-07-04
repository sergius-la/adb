from adb import ADB

class Files:
    
    @staticmethod
    def pull(dev_id: str, path_from: str, path_to: str):
        """
        Print ADB pull execution into terminal
        :dev_id: device id
        :path_from: Path to file on the device
        :path_to: Path to save a file
        """

        command = "adb -s {dev_id} pull {path_from} {path_to}".format(dev_id=dev_id, path_from=path_from, path_to=path_to)
        output = ADB._get_terminal_output(command)
        print("I: {}".format(output))