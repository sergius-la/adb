from enum import Enum


class AndroidKeyevent(Enum):
    command = "command"
    key_code = "key_code"
    BACK = {command: "BACK", key_code: "4"}
    POWER_BUTTON = {command: "POWER BUTTON", key_code: "26"}
    WAKEUP = {command: "Wake Up", key_code: "224"}
