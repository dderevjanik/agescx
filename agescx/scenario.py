from .models import *
from .controller import *
from .utilities import *
# utilities
from .decompress import *
from .compress import *


class Scenario:

    """ Scenario class """

    def __init__(self, filename=None, ver=1.21):
        """create scenario with defaults values,
            check default.txt for more information

            Args:
                filename (str, optional): load scenario from file
                version (float, optional): specific version"""
        self.version = ver
        if filename:
            self.load(filename)
        else:
            self._clear()

    def __repr__(self):
        name = "SCENARIO:{}\n".format(self.filename)
        info1 = "\tWIDTH:{} HEIGHT:{}\n".format(self.tiles.width, self.tiles.height)
        info2 = "\tUNITS:{}\n".format(len(self.units))
        info3 = "\tTRIGGERS:{}".format(len(self.triggers))
        return name + info1 + info2 + info3

    def load(self, filename, ver=1.21):
        """
            load scenario from file
            it doesn't save current scenario

            Args:
                filename (str): scenario filename
                ver (float, optional): version of scenario

            Raises:
                IOError: if file doesn't exits or is broken
        """
        self._clear()

        try:
            f = open(filename, 'rb')
        except:
            raise(IOError("File is broken or doesn't exists"))
        b = f.read()  # get bytes from file

        Decompress(self, b, ver, False)  # load data

    def save(self, filename=None, ver=1.21):
        """
            save scenario as scx format

            Args:
                filename (str, optional): if set, it will create new
                    scenario file, otherwise rewrite current
                ver (float, optional): save with specific

            Todo:
                finish this section
        """
        if filename is None:
            filename = self.filename  # save to this scenario file

        Compress(self, filename, ver)

    def new(self, filename):
        """create whole new blank scenario

            Args:
                terrainType (int, optional): starting terrain type, 0
                eleavtion (int, optional): starting elevation, 0
                filename (str, optional): if sets, it will create
                    new scenario file
                ver (float, optional): create version specific scenario

            Todo:
                finish starting terrainType and elevation
        """
        self._clear()

        self.version = "1.21"
        self.version2 = 1.22
        self.filename = filename

    def _clear(self):
        """clear all scenario data"""
        self.filename = None  # scenario filename
        self.version = None  # scenario version

        self.instructions = ""
        self.plrnumb = 8

        self.players = Players()    # initialize players
        self.messages = Messages()   #
        self.cinematics = Cinematics()  # movies
        self.background = Background()  # pre-game image
        self.map = Map()
        self.tiles = self.map.tiles
        self.goals = Goals()
        self.units = Units()
        self.triggers = Triggers()
        self.debug = Debug()

        for i in range(len(self.players)):
            self.players[i].units = self.units[i]

        self.timestamp = 0  # last save
