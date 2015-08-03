from .effect import *
from .condition import *


class Trigger:

    """Scenario trigger

    Args:
        name (str): name of trigger (displayed in game editor)
        enable (bool): is trigger enabled ?
        loop (bool): looping trigger ?
        objective (bool): display objective, when enabled is fired?
        objectiveOrder (int): display objective on row
        text (str): objective text to display
        unknown1 (int): unknown1
        unknown2 (int): unknown2
        effects (list(Effect)): effects stored in trigger
        conditions (list(Condition)): conditions stored in trigger
    """

    @property
    def effects(self):
        return self.__effects

    @property
    def conditions(self):
        return self.__conditions

    def __init__(self, name="", enable=True, loop=False,
                 objective=True, objectiveOrd=0, text="",
                 unknown1=0, unknown2=0):
        """Initialize scenario trigger"""
        self.name = name  # name of trigger
        self.enable = enable  # ? enabled from start
        self.loop = loop  # ? loop trigger

        self.objective = objective  # ? objective
        self.objectiveOrder = objectiveOrd  # line number in objectives menu
        self.text = text

        self.unknown1 = unknown1
        self.unknown2 = unknown2

        self.__effects = list()
        self.__conditions = list()

    def __repr__(self):
        name = "TRIGGER: \n"
        info1 = "\tNAME: {}\n\tENABLED: {}\n".format(self.name, self.enable)
        info2 = "\tLOOP: {}\n\tOBJECTIVES: {}\n".format(
            self.loop, self.objective)
        info3 = "\tOBJECTIVES ORDER: {}\n".format(self.objectiveOrder)
        info4 = "\tTEXT: {}".format(self.text)
        return name + info1 + info2 + info3 + info4

    def toJSON(self):
        """return JSON"""
        data = dict()
        data["name"] = self.name
        data["enable"] = self.enable
        data["loop"] = self.loop
        data["objective"] = self.objective
        data["objectiveOrder"] = self.objectiveOrder
        data["text"] = self.text
        data["effects"] = list()
        for effect in self.__effects:
            data["effects"].append(effect.toJSON())
        data["conditions"] = list()
        for condition in self.__conditions:
            data["conditions"].append(condition.toJSON())
        return data

    def newEffect(self, **config):
        """
        Create new effect for this trigger

        Note:
            check effect params
        """
        self.__effects.append(Effect(**config))

    def newCondition(self, **config):
        """
        Create new condition for this trigger

        Note:
            check effect params
        """
        self.__conditions.append(Condition(**config))
