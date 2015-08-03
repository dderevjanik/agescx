from agescx.models import *


class Players:

    """Store players"""

    def __init__(self):
        """Create player controller"""
        self._players = list()
        for i in range(9):  # include gaia = player 0
            self._players.append(Player(index=i))

    def __len__(self):
        """Number of players

        Return:
            int: number of players, 9
        """
        return len(self._players)

    def __getitem__(self, index):
        """Get player with selected index

        Args:
            index (str): index of player

        Return:
            Player: player with index
        """
        return self._players[index]

    def __repr__(self):
        name = "Players: \n"
        info1 = "\tCount:{} \tActive: {}\n".format(self.__len__(), len(self.activePlayers()))
        return name + info

    def toJSON(self):
        """return JSON"""
        data = dict()
        for pIndex in range(len(self)):
            data[pIndex] = self[pIndex].toJSON()
        return data

    def byColor(self, color):
        """return all players with specific color

        Args:
            color (int): color

        Return:
            list(Player): players
        """
        players = list()

        for player in self._players:
            if player.color == color:
                players.append(player)

        return players

    def byCivilization(self, civlization):
        """return all players with specific civlization

        Args:
            civlization (int): civlization

        Return:
            list(Player): players
        """
        players = list()

        for player in self._players:
            if player.civlization == civlization:
                players.append(player)

        return players

    def byAge(self, age):
        """return all players with specific age

        Args:
            age (int): age

        Return:
            list(Player): players
        """
        players = list()

        for player in self._players:
            if player.age == age:
                players.append(player)

        return players

    def humans(self):
        """return all human players

        Return:
            list(Player): players
        """
        players = list()

        for player in self._players:
            if player.human == 1:
                players.append(player)

        return players

    def computers(self):
        """return all computer players

        Return:
            list(Player): players
        """
        players = list()

        for player in self._players:
            if player.human == 0:
                players.append(player)

        return players

    def startResources(self, food=None, wood=None, gold=None, stone=None, ore=None):
        """Set starting resource for all players

        Args:
            food (int, optional): food
            wood (int, optional): wood
            gold (int, optional): gold
            stone (int, optional): stone
            ore (int, optional): ore
        """
        for player in self._players:
            if food:
                player.Resource.food = food
            if wood:
                player.Resource.wood = wood
            if gold:
                player.Resource.gold = gold
            if stone:
                player.Resource.stone = stone
            if ore:
                player.Resource.ore = ore

    def activeAll(self):
        """activate all players"""
        for player in self._players:
            player.active = 1

    def deactiveAll(self):
        """deactive all players"""
        for player in self._players:
            player.active = 1

    def active(self):
        """Return of active players

        Return:
            list(Player): active players
        """
        result = list()

        for player in self._players:
            if player.active == 1:
                result.append(player)

        return list()

    def inactive(self):
        """Return inactive players

        Return:
            list(Player): inactive players
        """
        result = list()

        for player in self._players:
            if player.active == 0:
                result.append(player)

        return list()
