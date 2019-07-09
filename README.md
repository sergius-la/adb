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
- __[ADB:](/adb/adb.py)__
  - TODO: Add Unit tests
  - `get_connected_devices()`
- __[User actions:](/adb/user_actions.py)__
  - TODO: Add Unit tests
  - `tap(x, y)`
  - `stipe(x1, y1, x2, y2)`
  - `send_text(text)`
  - TODO: OpenNotifications
  - TODO: PressBack
  - TODO: Apps
  - TODO: LockDevice
- __[Device info:](/adb/device_info.py)__
  - TODO: Add Unit tests
  - `get_PID(process_name)`
  - `get_meminfo(package)`
  - `save_meminfo(path, package)`
  - `get_package_activity()`
- __[Device manipulations:](/adb/device_manipulations.py)__
  - TODO: Add Unit tests
  - `set_screen_brightness(0 to 255)`
  - `screenshot(path_save_device)`
  - `get_screenshot(path_device, path_save: str, delete=False)`
  - TODO: Bluetoth On/Off
  - TODO: Screen Caption
- __[Files:](/adb/files.py)__
  - TODO: Add Unit tests
  - `pull(path_from, path_to)`
  - `push(path_file, path_to)`
  - `delete(path_file)`
- __[Package info:](/adb/package_info.py)__
  - TODO: Add Unit tests
  - `get_list_packages()`
  - `get_packahe_version(package)`
- __[Package manipulations:](/adb/package_manipulations.py)__
  - TODO: Add Unit tests
  - `clear_package_cache(package)`
  - `install_app(path_package)`
  - `start_package(package_name)`
  - `close_package(package_name)`
  - TODO: Grand permissions
  - TODO: Revoke permissions
- __[Layout:](/adb/layout.py)__
  - TODO: Add Unit tests
  - `dump_layout()`
  - `get_layout(path_save)`
  - TODO: Search Element