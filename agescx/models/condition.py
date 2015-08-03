from agescx.enums.eCondition import *


class Condition:

    """Initialize Condition

    Attributes:
        conditionType (int): type of condition
        check (int): is checked ? (always)
        resource (int): resource type
        amount (int): amount of resource
        unitObject (int): unit object
        unitId (int): id of unit
        unitName (int): name of unit
        sourcePlayer (int): affected player
        tech (int): is tech discovered ?
        timer (int): how much time
        unknown1 (int): unknown1
        x1 (int): selected area start X position
        y1 (int): selected area start Y position
        x2 (int): selected area end X position
        y2 (int): selected area end Y position
        aiSinal (int): check signal from ai
    """

    def __init__(self, type=0, check=0x10,
                 amount=0, resource=0, unitObject=0,
                 unitId=0, unitName=0, sourcePlayer=0,
                 tech=0, timer=0, unknown1=0,
                 x1=0, y1=0, x2=0, y2=0,
                 unitGroup=0, unitType=0, aiSignal=0
                 ):
        self.type = type  # condition type
        self.check = check
        self.amount = amount
        self.resource = resource
        self.unitObject = unitObject
        self.unitId = unitId
        self.unitName = unitName
        self.sourcePlayer = sourcePlayer
        self.tech = tech
        self.timer = timer
        self.unknown1 = unknown1
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.unitGroup = unitGroup
        self.unitType = unitType
        self.aiSignal = aiSignal

    def __repr__(self):
        name = "CONDITION:\n"
        info1 = "\tTYPE:{} - {}".format(self.type, eCondition[self.type])
        return name + info1

    def toJSON(self):
        """return JSON"""
        data = dict()
        data["type"] = self.type
        data["check"] = self.check
        data["amount"] = self.amount
        data["resource"] = self.resource
        data["unitObject"] = self.unitObject
        data["unitId"] = self.unitId
        data["unitName"] = self.unitName
        data["sourcePlayer"] = self.sourcePlayer
        data["tech"] = self.tech
        data["timer"] = self.timer
        data["x1"] = self.x1
        data["y1"] = self.y1
        data["x2"] = self.x2
        data["y2"] = self.y2
        data["unitGroup"] = self.unitGroup
        data["unitType"] = self.unitType
        data["aiSignal"] = self.aiSignal
        return data
