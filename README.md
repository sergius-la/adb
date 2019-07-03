# ADB Commands

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
- __Device manipulations:__
  - set_screen_brightness(0 to 255)