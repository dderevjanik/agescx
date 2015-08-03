class Resource:

    """Information about player resource.
        Include Ore, which is unused, but it can be enabled.

    Attributes:
            food (int): food
            wood (int): wood
            gold (int): gold
            stone (int): stone
            ore (int): ore
    """

    def __init__(self, food=0, wood=0, gold=0, stone=0, ore=0):
        """Create Resource container for a player

        Args:
            food (int): starting food
            wood (int): starting wood
            gold (int): starting gold
            stone (int): starting stone
            ore (int): starting ore. unused
        """
        self.food = food
        self.wood = wood
        self.gold = gold
        self.stone = stone
        self.ore = ore

    def __repr__(self):
        name = "Player resources: \n"
        res1 = "\tWood: {}\n\tFood: {}\n".format(self.wood, self.food)
        res2 = "\tGold: {}\n\tStone: {}\n".format(self.gold, self.stone)
        res3 = "\tOre*: {}".format(self.ore)
        return name + res1 + res2 + res3

    def toJSON(self):
        """return JSON"""
        data = dict()
        data['food'] = self.food
        data['wood'] = self.wood
        data['stone'] = self.stone
        data['gold'] = self.gold
        return data

    def setAll(self, value):
        """Set value to all resources

        Args:
            value (int): a value set to all resources
        """
        self.food = value
        self.wood = value
        self.gold = value
        self.stone = value
        self.ore = value

    def getAll(self):
        """get all resource

        Return:
            (tuple): resource values
        """
        return (self.food, self.wood, self.gold, self.stone, self.ore)
