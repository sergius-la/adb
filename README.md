# <img src="/img/py.png" width="24" height="24"> <img src="/img/adb.gif" width="24" height="24"> ADB Commands

Python package for executing adb commands.

> Requirements: <br>
> Android SDK Tools - https://developer.android.com/studio/releases/sdk-tools <br>
> adb - PATH variable

Install with PIP <br>
`pip install git+https://github.com/sergius-la/adb.git`

Usage example:
```python
dev_id = ADB.get_connected_devices()[0]
ADB.swipe(dev_id, 370, 1200, 370, 160)
```

[List of commands](https://github.com/sergius-la/Cheatsheet/blob/master/adb/adb.md)

## Commands
- __ADB:__
  - get_connected_devices()
- __User actions:__
  - tap(x, y)
  - stipe(x1, y1, x2, y2)
- __Device info:__
  - get_PID(process_name)
  - get_meminfo(package)
  - save_meminfo(path, package)
  - TODO: Get currect package activity name
- __Device manipulations:__
  - set_screen_brightness(0 to 255)
  - TODO: Bluetoth On/Off
  - TODO: Screenshot
- __Files:__
  - pull(path_from, path_to)
  - TODO: Push File
- __Package info:__
  - get_list_packages()
  - get_packahe_version(package)
- __TODO: Package manipulations:__
  - TODO: Install
  - TODO: Grand permissions
  - TODO: Revoke permissions
  - TODO: Start activity
  - TODO: Stop activity
  - TODO: Clear app cache
- __Layout:__
  - dump_layout()
  - get_layout(path_save)
  - TODO: Search Element