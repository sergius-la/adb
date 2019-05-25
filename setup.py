import os
from setuptools import setup

NAME = "adb"
VERSION = None

package_root = os.path.abspath(os.path.dirname(__file__))

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_")
    with open(os.path.join(package_root, project_slug, '__version__.py')) as file:
        exec(file.read(), about)
        VERSION = about["__version__"]

setup (
    name = NAME,
    version =  VERSION,
    package_dir={'': "adb"},
    packages=['']
)