# <img src="/img/py.png" width="32" height="32"> ADB Commands

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
  - get_package_activity()
- __Device manipulations:__
  - set_screen_brightness(0 to 255)
  - TODO: Bluetoth On/Off
  - TODO: Screenshot
  - TODO: Screen Caption
- __Files:__
  - pull(path_from, path_to)
  - push(path_file, path_to)
- __Package info:__
  - get_list_packages()
  - get_packahe_version(package)
- __TODO: Package manipulations:__
  - clear_package_cache(package)
  - install_app(path_package)
  - start_package(package_name)
  - close_package(package_name)
  - TODO: Grand permissions
  - TODO: Revoke permissions
- __Layout:__
  - dump_layout()
  - get_layout(path_save)
  - TODO: Search Element