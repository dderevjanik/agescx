class Camera:

    """Initial player camera

    Attributes:
        x (float): x position
        y (float): y position
        unknown1 (int): unknown
        unknown2 (int): unknown
    """

    def __init__(self, x=0.0, y=0.0, unknown1=0, unknown2=0):
        self.x = x
        self.y = y
        self.unknown1 = unknown1
        self.unknown2 = unknown2

    def __repr__(self):
        name = "CAMERA:\n"
        info1 = "\tX:{} Y:{}".format(self.x, self.y)
        return name + info1

    def toJSON(self):
        """return JSON"""
        data = dict()
        data['x'] = self.x
        data['y'] = self.y
        return data
