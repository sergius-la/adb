from py_adb.device_manipulations import DeviceManipulations


class Element(object):
    """
    Class to represent the Android element
    """

    def __init__(self, raw_xml_element):
        self._id = raw_xml_element.get("resource-id")
        self._bounds = Element._bounds_parser(raw_xml_element.get("bounds"))
        self._center_point = Element.get_element_center_point(self._bounds)
        # TODO: Check for text value in the element and convert it
        self._content_desc = raw_xml_element.get("content-desc")
        self._is_enable = raw_xml_element.get("enabled")
        self._is_clickable = raw_xml_element.get("clickable")
        # TODO: Check tags in the mobile
        self._tag = "TODO"
    
    def __repr__(self):
        return "Element: \nResource-ID - <{id}> \nContent desc - <{content_desc}> "\
            .format(id=self._id, content_desc=self._content_desc)
    
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
    def get_element_center_point(cls, raw_bounds):
        """
        Helper method to get a center points for the element

        # [X1-616, Y1-48][X2-720, Y2-144]
        The center counting by - X1 + (X1 + X2)/2
        """

        x = int(raw_bounds[0] + ((raw_bounds[2] - raw_bounds[0]) / 2))
        y = int(raw_bounds[1] + ((raw_bounds[3] - raw_bounds[1]) / 2))
        return {"x": x, "y": y}

    @staticmethod
    def _bounds_parser(str_bounds: str) -> list:
        """
        Helper method to parce string like [8,56][712,165]
        and return a list of int [8, 56, 712, 165]
        """

        raw = str_bounds.replace("[", "").replace("]", ",").split(",")
        return list(map(int, list(filter(None, raw))))
    
    def tap(self, dev_id):
        """
        Method to tap on the element
        """

        DeviceManipulations.tap(dev_id, self.x, self.y)
