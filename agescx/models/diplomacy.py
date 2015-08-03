class Diplomacy:

    """
    Respresents every player diplomacy stances with others
    """

    def __init__(self, stances=[0]*8):
        """
        Initialize Diplomacy

        Args:
            stances (list(int)): stances with other player
        Note:
            there's 8 stances with other players
        """
        self.stances = stances
        self.gaia = [0]*9

    def __repr__(self):
        name = "Diplomacy:\n"
        stances = "\t"

        for ind in range(len(self.stances)):
            stances += "P{}: {}; ".format(ind, self.stances[ind])

        return name + stances

    def __setitem__(self, playerIndex, stance):
        """
        Todo:
            describe method
        """
        self.stances[playerIndex] = stance

    def __getitem__(self, playerIndex):
        """
        Get diplomacy stance with another player

        Args:
            playerIndex (int): index of another player

        Return:
            (int): player stance (0=allied, 1=neutral, 3=enemy)
        """
        return self.stances[playerIndex]

    def toJSON(self):
        """return JSON"""
        data = dict()
        for i in range(len(self.stances)):
            data[i] = self.stances[i]
        return data

    def allStances(self, stance):
        """
        Set diplomacy stance with all players

        Args:
            stance (int): diplomacy stance
        """
        for i in range(len(self.stances)):
            self.stances[i] = stance

    def getPlayersByStance(self, stance):
        """
        Get Players, which have selected stance

        Args:
            stance (int): 0=allied, 1=neutral, 3=enemy

        Return:
            (list(int)): player indexes, which have selected stance

        Todo:
            describe param stance
        """
        result = list()

        for ind in range(len(self.stances)):
            if self.stances[ind] == stance:
                result.append(ind)

        return result

    def allies(self):
        """
        Get all players indexes with ally stance (0)

        Return:
            (list(int)): player indexes, which are allies
        """
        return self.getPlayersByStance(0)

    def neutrals(self):
        """
        Get all players indexes with neutral stance (1)

        Return:
            (list(int)): player indexes, which are neutrals
        """
        return self.getPlayersByStance(1)

    def enemies(self):
        """
        Get all players indexes with enemy stance (2)

        Return:
            (list(int)): player indexes, which are enemies
        """
        return self.getPlayersByStance(3)
