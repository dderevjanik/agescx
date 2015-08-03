from agescx.enums.eEffect import *


class Effect:

    """Trigger Effect

    Attributes:
        effectType (int): type of effect
        check (int): is checked ?
        aiGoal (int): ai goal
        state (int): diplomacy state
        resource (int): player resource like food, wood, gold, stone,
            kills, death, score
        amount (int): amount of resource
        selectedCount (int): number of selected units
        unitId (int): id of selected unit
        unitName (int): unit new name
        sourcePlayer (int): source player
        targetPlayer (int): target player
        tech (int): technology id to research
        stringId (int): id of string
        unknown1 (int): unknown1
        time (int): display time
        triggerId (int): id of trigger to enable/disable
        x (int): x position
        y (int): y position
        x1 (int): affected area start X position
        y1 (int): affected area start Y position
        x2 (int): affected area end X position
        y2 (int): affected area end Y position
        unitGroup (int): unit group type to affect
        unitType (int): unit type to affect
        instructionId (str): instruction panel
        text (str): instruction text
        filename (str): filename (used for sounds)
        unitIds (list(int)): list with selected units
    """

    def __init__(self, type=0, check=0x17,
                 aiGoal=0, amount=0, resource=0, state=0,
                 selectedCount=0, unitId=0, unitName=0,
                 sourcePlayer=0, targetPlayer=0, tech=0,
                 stringId=0, unknown1=0, time=0, triggerId=0,
                 x=0, y=0, x1=0, y1=0, x2=0, y2=0,
                 unitGroup=0, unitType=0,
                 instructionId=0, text="", filename="", unitIds=[]):
        self.type = type  # effect type
        self.check = check
        self.aiGoal = aiGoal
        self.amount = amount
        self.resource = resource
        self.state = state  # state of trigger
        self.selectedCount = selectedCount
        self.unitId = unitId
        self.unitName = unitName
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.tech = tech
        self.stringId = stringId
        self.unknown1 = unknown1
        self.time = time
        self.triggerId = triggerId
        self.x, self.y = x, y
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.unitGroup = unitGroup
        self.unitType = unitType
        self.instructionId = instructionId
        self.text = text
        self.filename = filename
        self.unitIds = unitIds

    def __repr__(self):
        name = "EFFECT:\n"
        info1 = "\tTYPE:{} - {}\n".format(self.type, eEffect[self.type])
        return name + info1

    def toJSON(self):
        """return JSON"""
        data = dict()
        data["type"] = self.type
        data["check"] = self.check
        data["aiGoal"] = self.aiGoal
        data["amount"] = self.amount
        data["resource"] = self.resource
        data["state"] = self.state
        data["selectedCount"] = self.selectedCount
        data["unitId"] = self.unitId
        data["unitName"] = self.unitName
        data["sourcePlayer"] = self.sourcePlayer
        data["targetPlayer"] = self.targetPlayer
        data["tech"] = self.tech
        data["stringId"] = self.stringId
        data["unknown1"] = self.unknown1
        data["time"] = self.time
        data["triggerId"] = self.triggerId
        data["x"] = self.x
        data["y"] = self.y
        data["x1"] = self.x1
        data["y1"] = self.y1
        data["x2"] = self.x2
        data["y2"] = self.y2
        data["unitGroup"] = self.unitGroup
        data["unitType"] = self.unitType
        data["instructionId"] = self.instructionId
        data["text"] = self.text
        data["filename"] = self.filename
        data["unitIds"] = self.unitIds
        return data
