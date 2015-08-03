from agescx.models import *
from itertools import chain


class Tiles:

    """Holds tiles
        With this class you are able to manipulate with tiles in scenario
        There's som helpfull classes
    """

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __init__(self, width, height):
        """create tiles

        Args:
            width (int, optional): default width, 32
            height (int, optional): default height, 32
        """
        self._tiles = list()
        self.__recreate(width, height)
        self._width = width
        self._height = height

    def __getitem__(self, r):
        """Get row of tiles

        Args:
            r (int): row tiles

        Return:
            (list): tiles
        """
        if (r < 0):
            raise ValueError("r can't be < 0")
        if (r > self._width - 1):
            raise ValueError("r can't be > map width")
        return self._tiles[r]

    def __iter__(self):
        """iterate over all tiles in scenario"""
        return iter(chain(*self._tiles))

    def __len__(self):
        """number of tiles

        Return:
            (int): number of tiles
        """
        return self._height * self._width

    def __repr__(self):
        name = "Tiles: \n"
        info = "\tRows:{} \tCollumns:{}\n".format(
            self._height, self._width)
        info2 = "\tTiles:{}".format(self._height * self._width)

        return name + info + info2

    def __recreate(self, width, height):
        self._tiles = list()
        for r in range(height):
            self._tiles.append(list())
            for c in range(width):
                self._tiles[r].append(Tile(r, c))
        self._height = height
        self._width = width

    def toJSON(self):
        """return JSON"""
        data = list()
        for h in range(self.height):
            data.append(list())
            for w in range(self.width):
                data[h].append(self[h][w].toJSON())
        return data

    def resize(self, newWidth, newHeight):
        """resize map

        Todo:
            add description
            if resize < new Size, shrink and delete tempory tiles
            clean section
        """
        width, height = self._width, self._height
        wDiff = abs(newWidth - width)
        hDiff = abs(newHeight - height)

        if newWidth > self._width:
            for r in range(height):
                for i in range(wDiff):
                    self._tiles[r].append(Tile(r, width + i))
            width = newWidth
        elif newWidth < self._width:
            for r in range(height):
                self._tiles[r] = self._tiles[r][:width - wDiff]
            width = newWidth

        if newHeight > self._height:
            for i in range(hDiff):
                l = [Tile(height + i, c) for c in range(width)]
                self._tiles.append(l)
        elif newHeight < self._height:
            self._tiles = self._tiles[:height - hDiff]

        self._height = newHeight
        self._width = newWidth

    def row(self, row):
        """Get Row or Y tiles

        Args:
            row (int): row

        Return:
            (list): tiles
        """
        if (row < 0):
            raise ValueError("row can't be < 0")
        if (row > self._height - 1):
            raise ValueError("row can't be > tiles rows")

        return self._tiles[row]

    def collumn(self, collumn):
        """Get Collumn or X tiles

        Args:
            collumn (int): collumn

        Return:
            (list): tiles
        """
        if (collumn < 0):
            raise ValueError("collumn can't be < 0")
        if (collumn > self._width):
            raise ValueError("collumn can't be > tiles collumns")

        return [row[collumn] for row in self._tiles]

    def clearTerrain(self, terrainType=0, safe=True):
        """clear all tiles

        Args:
            terrainType (int): type of terrain
            safe (boolean): throw exception on unexcepted behavior
        """
        if (safe):
            if (terrainType < 0):
                raise ValueError("terrainType can't be {}".format(terrainType))
        for tile in self:
            tile.type = terrainType

    def clearElevation(self, elevation=0, safe=True):
        """clear all elevation

        Args:
            elevation (int): elevation level
            safe (boolean): throw exception on unexcepted behavior
        """
        if (safe):
            if (elevation < 0):
                raise ValueError("elevation can't be {}".format(elevation))
        for tile in self:
            tiel.elevation = elevation

    def size(self):
        """get map size

        Return:
            (tuple): width height
        """
        return (self._width, self._height)

    def getByTerrain(self, terrainType):
        """get all tiles by terrain type

        Args:
            terrainType (int): terrain type

        Return:
            (list): tiles
        """
        tiles = list()

        for tile in self:
            if tile.type == terrainType:
                tiles.append(tile)

        return tiles

    def getByElevation(self, elevation):
        """get all tiles by elevation level

        Args:
            elevation (int): elevation level

        Return:
            (list): tiles
        """
        tiles = list()

        for tile in self:
            if tile.elevation == elevation:
                tiles.append(tile)

        return tiles

    def getArea(self, x1, y1, x2, y2):
        """Get tiles from selected area

        Args:
            x1 (int): point 1 x
            y1 (int): point 1 y
            x2 (int): point 2 x
            y2 (int): point 2 y

        Return:
            (list): tiles

        Raises:
            IndexError: If points are outside map
        """
        if (x1 < 0) or (x2 < 0) or (y1 < 0) or (y2 < 0):
            raise IndexError("one of parameter is <0 ")
        if (x1 > self._width - 1) or (x2 > self._width - 1):
            raise IndexError("one of parameter is > map width or > map height")
        if (y1 > self._height) or (y2 > self._height):
            raise IndexError("one of parameter is > map width or > map height")
        result = list()
        nx, ny = 0, 0
        for y in range(0, abs(y2-y1)+1):
            ny = y1 + y
            for x in range(0, abs(x2-x1)+1):
                nx = x1 + x
                result.append(self[ny][nx])

        return result

    def replaceTerrain(self, terrainType, newType):
        """replace all terrain type with new type

        Args:
            terrainType (int): terrain you want replace
            newType (int): new terrain type

        Return:
            (int): number of replaced tiles
        """
        count = 0

        for tile in self:
            if tile.type == terrainType:
                tile.type = newType
                count += 1

        return count

    def incElevation(self, increase=1):
        """increase elevation on all tiles

        Args:
            increase (int): how much will be incresed
        """
        for tile in self:
            tile.up(increase)

    def decElevation(self, decrease=1):
        """decrease elevation on all tiles

        Args:
            decrease (int): how much will be decreased
        """
        for tile in self:
            tile.down(decrease)
