from enum import Enum

class AndroidPermissions(Enum):
    CAMERA = {"name": "Camera", "perm":"android.permission.CAMERA"}
    LOCATION = {"name": "Camera", "perm":"android.permission.ACCESS_FINE_LOCATION"}
    