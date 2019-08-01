
from py_adb.user_actions import UserActions

class Element(object):
    """
    Class to represent the Android element
    """

    def __init__(self, raw_value: dict):
        assert isinstance(raw_value, dict), "Raw Element value shoud come in dict format"
        self._id = Element._bounds_parser(raw_value.get("recource-id"))
        self._bounds = raw_value.get("bounds")
        self._center_point = Element.get_element_center_point()
        # TODO: Check for text value in the element and convert it
        self._content_desc = raw_value.get("content-desc")
        self._is_enable = raw_value.get("enabled")
        self._is_clickable = raw_value.get("clickable")
        # TODO: Check tags in the mobile
        self._tag = "TODO"
    
    def __repr__(self):
        return "Recource-ID {id} - Content desc - {content_desc} ".format(id=_id, content_desc=_content_desc)
    
    @property
    def x(self):
        """
        Return center x of Element
        """
        
        return self._center_point.get("x")
    
    @property
    def y(self):
        """
        Return center y of Element
        """

        return self._center_point.get("y")

    @classmethod
    def get_element_center_point():
        """
        Helper method to get a center points from the element
        TODO: Test!
        """

        bounds = Element._bounds_parser(Element._bounds)
        x = int(bounds[1] + ((bounds[2] - bounds[1]) / 2))
        y = int(bounds[0] + ((bounds[3] - bounds[0]) / 2))
        return {"x":x, "y":y}

    @classmethod
    def _bounds_parser(str_bounds: str) -> list:
        """
        Helper method to parce string like [8,56][712,165]
        and return a list of int [8, 56, 712, 165]
        TODO: Test!
        """

        raw = str_bounds.replace("[", "").replace("]", ",").split(",")
        return list(map(int, list(filter(None, raw))))