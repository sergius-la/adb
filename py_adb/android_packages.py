from enum import Enum


class AndroidKPackage(Enum):
    app = "App Name"
    package = "package"
    YOUTUBE = {app: "YouTube", package: "com.google.android.youtube"}
    PLAY_STORE = {app: "Play Store", package: "com.android.vending"}


class Package(object):
    """
    Package Info class
    """

    def __init__(self, package, app_name, version):
        self.appName = app_name
        self.version = version
        self.package = package
    
    def __repr__(self):
        return "{appName} - {version} - {package}".format(appName=self.appName,
                                                          version=self.version, package=self.package)
