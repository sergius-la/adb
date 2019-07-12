from enum import Enum

class Properties(Enum):
    BRAND = {"name": "Brand", "prop":"ro.product.brand"}
    MODEL = {"name":"Model", "prop":"ro.product.model"}
    ANDROID_VERSION = {"name":"Android Version", "prop":"ro.build.version.release"}


    