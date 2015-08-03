from agescx.enums.eUnit import *


class Unit:

    """Player specific unit

    Attributes:
        x (int): unit X position
        y (int): unit Y position
        type (int): Unit type
        angle (int): Unit starting angle
        frame (int): Unit starting frame
        inID (int): in which ID is unit garissoned, 4294967295 isn't
        unknown1 (int): Unknown variable
        unknown2 (int): Unknown variable

    Todo:
        Cargo: iterable units in cargo
        Unload: unload all units from cargo
        Load: will load units to cargo
        ChangeOwner: changing owner
    """
    nextID = None

    @property
    def id(self):
        return self.__id

    @property
    def owner(self):
        return self.__owner

    def __init__(self, id=None, x=0, y=0, owner=0,
                 type=0, angle=0, frame=0, inId=-1,
                 unknown1=2, unknown2=2):
        """Create new unit

        Args:
            id (int): unit ID
            x (int, optional): unit X position, 0
            y (int, optional): unit Y position, 0
            owner (int, optional): Player, who owns this unit, 0
            type (int, optional): Unit type, 0
            angle (int, optional): Unit starting angle, 0
            frame (int, optional): Unit starting Frame, 0
            inID (int, optional): in which ID is unit garissoned, -1 isn't
            unknown1 (int, optional): Unknown variable
            unknown2 (int, optional): Unknown variable

        Return:
            self

        Raises:
            TypeError: if one of argument is dictory
        """
        if id is None:
            id = Unit.nextID()  # get next id

        self.__owner, self.x, self.y = owner, x, y
        self.unknown1, self.unknown2 = unknown1, unknown2
        self.__id, self.type, self.angle = id, type, angle
        self.frame, self.inId = frame, inId

    def __repr__(self):
        name = "UNIT:\n"
        info1 = "\tID:{} X:{} Y:{} IN:{}\n".format(self.__id, self.x, self.y, self.inId)
        info2 = "\tOWNER:{} UNK1:{} UNK2:{}\n".format(self.__owner, self.unknown1, self.unknown2)
        info3 = "\tANGLE:{} FRAME:{}\n".format(self.angle, self.frame)
        info4 = "\tTYPE:{} - {}".format(self.type, eUnit[self.type][:20])
        return name + info1 + info2 + info3 + info4

    def toJSON(self):
        """return JSON object"""
        data = {}
        data['id'] = self.id
        data['owner'] = self.owner
        data['type'] = self.type
        data['x'] = self.x
        data['y'] = self.y
        data['angle'] = int(self.angle)
        data['frame'] = self.frame
        data['inId'] = self.inId
        return data

    def move(self, dx, dy):
        """move unit

        Args:
            dx (int): how much move x
            dy (int): how much move y
        """
        self.x += dx
        self.y += dy
