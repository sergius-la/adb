from enum import Enum

class AndroidKPackage(Enum):
    app = "App Name"
    package = "package"
    YOUTUBE = {app: "YouTube", package:"com.google.android.youtube"}
    PLAYMARKET = {app: "Play Store", package:"com.android.vending"}