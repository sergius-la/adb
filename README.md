# <img src="/img/py.png" width="32" height="32"> ADB Commands

Python package for executing adb commands.

[_List of adb commands_](https://github.com/sergius-la/Cheatsheet/blob/master/adb/adb.md)

TODO: Add tests status

## Install

> __Requirements:__ <br>
> Android SDK Tools - https://developer.android.com/studio/releases/sdk-tools <br>
> adb - PATH variable

Install with PIP <br>
`pip install git+https://github.com/sergius-la/adb.git`

## Usage

Usage example:
```python
dev_id = ADB.get_connected_devices()[0]
ADB.swipe(dev_id, 370, 1200, 370, 160)
```

- TODO: Add more examples

## Package methods

### Cookbook
- __[Info:](/py_adb/info.py)__
    - `get_environment(package)`
    - `get_packages_version(AndroidPackage)`
      - [_All AndroidPackages_](/py_adb/android_packages.py)
        - _`YouTube`_
        - _`Play Store`_

***

###  Commands
- TODO: Main Runner
- __[ADB:](/py_adb/adb.py)__
  - `get_connected_devices()`
  - TODO: Add Dependensys into setup.py
- __[Device info:](/py_adb/device_info.py)__
  - `get_PID(process_name)`dd
  - `get_meminfo(package)`
  - `save_meminfo(path, package)`
  - `get_package_activity()`
  - `get_display_size(Device ID)`
  - `all_getprop(Device ID)`
  - `get_prop(Device ID, Properties)`
  - [_All Properties_](/py_adb/android_properties.py)
    - _`Android Version`_
    - _`Device Brand`_
    - _`Device Model`_
- __[Device manipulations:](/py_adb/device_manipulations.py)__
  - `set_screen_brightness(0 to 255)`
  - `screenshot(path_save_device)`
  - `save_screenshot(path_device, path_save, delete=False)`
    - TODO: Name generator
    - TODO: Add Flag to delete file after save
  - `open_notification_center(Device_ID)`
    - TODO: Add Check is Notification center is vivible
    - TODO: Screen Caption
- __[User actions:](/py_adb/user_actions.py)__
  - TODO: Refactor Move to device Manupulations  
  - `tap(x, y)`
  - `stipe(x1, y1, x2, y2)`
  - `send_text(text)`
  - `lock_device(Device ID)`
  - `unlock_device`
    - _UnlockType:_
      - _`SWIPE`_
  - [_All Keyevent_](/py_adb/android_keyevent.py)
    - _`BACK`_
    - _`POWER_BUTTON`_
    - TODO: Recent Apps
- __[Files:](/py_adb/files.py)__
  - `pull(path_from, path_to)`
  - `push(path_file, path_to)`
  - `delete(path_file)`
      - TODO: Test
      - TODO: Add check before executing
      - TODO: Add check after executing
  - `clear_dir(path_dir)`
- __[Package info:](/py_adb/package_info.py)__
  - `get_list_packages()`
  - `is_package_exist(dev_id, package)`
  - `get_packahe_version(package)`
- __[Package manipulations:](/py_adb/package_manipulations.py)__
  - `clear_package_cache(package)`
  - `install_app(path_package)`
    - TODO: App ENUM Flags -d, -r
    - TODO: Test
    - TODO: Check path
  - `start_package(package_name)`
  - `close_package(package_name)`
    - TODO: Test
  - `grant_permission(package_name, permissions)`
  - `revoke_permission(package_name, permissions)`
- __[Packages](/py_adb/android_packages.py)__
- __[Layout:](/py_adb/layout.py)__
  - `dump_layout()`
  - `get_layout(path_save)`
  - `search_element(path_file, id)`
    - TODO: Add search strategy (XPATH)
    - TODO: Search multiple lements
- __[TODO: Element Class]()__
  - TODO: Tap
  - TODO: Send Key
- __[Utility:](/py_adb/util.py)__
  - `Paths`

## Unit Tests

> __Requirements:__ <br>
> Connect Android Device in the Developer Mode

- Run Unit test (package root) - `pytest --cov=py_adb tests/` 
- To get report - `coverage html`