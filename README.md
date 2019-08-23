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
from py_adb.adb import ADB

dev_id = ADB.get_connected_devices()[0]
ADB.swipe(dev_id, 370, 1200, 370, 160)
```

- TODO: Add more examples

## Package methods

### Cookbook
- __[Info:](/py_adb/cookbook.py)__
    - `get_environment(package)`
    - `get_packages_version(AndroidPackage)`
      - [_All AndroidPackages_](/py_adb/android_packages.py)
        - _`YouTube`_
        - _`Play Store`_

***

###  Commands
- TODO: Add Dependencies into `setup.py`
- TODO: __`Runner`__
- [__`ADB`__](/py_adb/adb.py)
  ```python
  from py_adb.adb import ADB
  
  authorised_devices = ADB.get_connected_devices()
  all_connected_devices = ADB.get_connected_devices(False)
  ```
- __[Device info:](/py_adb/device_info.py)__
  - `get_PID(process_name)`
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
    - TODO: Screen Caption
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
  - `clear_dir(path_dir)`
- __[Package info:](/py_adb/package_info.py)__
    ```python
  from py_adb.package_info import PackageInfo
  
  PackageInfo.get_list_packages("<Device ID>") # List of installed apps
  PackageInfo.is_package_exist("<Device ID>", "package.name") # Check is package installed
  PackageInfo.get_package_version("<Device ID>", "package.name") # Get version of package
    ```
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
- [__`Layout - UI Interacting`__](/py_adb/layout.py)
    - TODO: Search multiple elements
    - [__Element__](/py_adb/element.py)
    ```python
  from py_adb.layout import Layout
  from py_adb.by import By
      
  element = Layout.get_element(By.ID, "<resource-id>")
  element.tap("<Device ID>")
    ```
  
  - [__By - Element search strategy__](/py_adb/by.py)
   ```python
  from py_adb.by import By
  
  # Search Element strategy  
  By.ID # Element id
  By.XPATH # xPath TODO: Implement
   ```

## Unit Tests

> __Requirements:__ <br>
> Connect Android Device in the Developer Mode

- Run Unit test (package root) - `pytest --cov=py_adb tests/` 
- To get report - `coverage html`