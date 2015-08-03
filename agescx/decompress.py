from .utilities import *
from .controller import *
from .models import *
import zlib
import time


def inflate(data):
    decompress = zlib.decompressobj(
        -zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()

    return inflated


def deflate(data, compresslevel=9):
    compress = zlib.compressobj(
            compresslevel,        # level: 0-9
            zlib.DEFLATED,        # method: must be DEFLATED
            -zlib.MAX_WBITS,      # window size in bits:
                                  #   -15..-8: negate, suppress header
                                  #   8..15: normal
                                  #   16..30: subtract 16, gzip header
            zlib.DEF_MEM_LEVEL,   # mem level: 1..8/9
            0                     # strategy:
                                  #   0 = Z_DEFAULT_STRATEGY
                                  #   1 = Z_FILTERED
                                  #   2 = Z_HUFFMAN_ONLY
                                  #   3 = Z_RLE
                                  #   4 = Z_FIXED
    )

    deflated = compress.compress(data)
    deflated += compress.flush()

    return deflated


class Decompress:

    def __init__(self, scenario, bData, version=1.21, temp=False):
        """!
        """
        self.scenario = scenario
        self.version = version
        start = time.time()
        headerLength = self.decompressHeader(bData)
        decompressed = self.unzip(bData[headerLength:])
        dataLenght = self.decompressData(decompressed)
        end = time.time() - start
        print(end)
        if temp:
            f = open('decompressed.temp', 'wb')
            f.write(decompressed)
            f.close()

    def decompressHeader(self, bData):
        decoder = Decoder(bData)
        decode, unpack, skip = decoder.decode, decoder.unpack, decoder.skip

        self.scenario.version = decode('ascii 4').decode('utf-8')  # scenario version
        version = float(self.scenario.version)
        length  = unpack('i')  # header length
        skip(4)  # skip Constant
        self.scenario.timestamp = unpack('i')[0]  # date of last save
        self.scenario.instructions = decode('str32')  # scenario instructions
        skip(4)  # skipt Constant and number of Players
        self.scenario.plrnumb = unpack('i')[0]

        return decoder.offset()

    def unzip(self, bytes):
        return zlib.decompress(bytes, -zlib.MAX_WBITS)

    def decompressData(self, bData):
        decoder = Decoder(bData)
        decode, unpack, skip = decoder.decode, decoder.unpack, decoder.skip

        # Shortcuts: Decoder
        getInt8 = decoder.getInt8
        getInt32 = decoder.getInt32
        getUInt32 = decoder.getUInt32
        getInt16 = decoder.getInt16
        getUInt16 = decoder.getUInt16
        getStr32 = decoder.getStr32
        getStr16 = decoder.getStr16
        getFloat = decoder.getFloat
        getBytes = decoder.getBytes
        getAscii = decoder.getAscii
        getDouble = decoder.getDouble

        # Shortcuts: Scenario
        scenario = self.scenario
        players = self.scenario.players
        messages = self.scenario.messages
        debug = self.scenario.debug
        triggers = self.scenario.triggers

        Units.nextID = getUInt32()

        self.version = getFloat()  # version 2
        self.scenario.version2 = self.version
        version = self.version

        for i in range(8):
            players[i+1].name = getAscii(256)
        skip(256*8)  # other player names 9-16

        if (self.version >= 1.18):
            for i in range(8):
                players[i+1].nameID = getInt32()
            skip(8*4)  # other player names string ID

        for i in range(8):
            players[i].active = getUInt32()
            players[i].human = getUInt32()
            players[i].civilization = getUInt32()
            players[i].unknown1 = getUInt32()
        skip(8*16)  # other players data

        decode('i')  # unk1
        decode('f')  # unk2
        skip(1)  # separator
        scenario.filename = getStr16()  # original filename

        # section: MESSAGES
        if (self.version >= 1.18):
            messages.objectives.id = getInt32()
            messages.hints.id = getInt32()
            messages.victory.id = getInt32()
            messages.loss.id = getInt32()
            messages.history.id = getInt32()
            if (self.version >= 1.22):
                messages.scouts.id = getInt32()
        messages.objectives.text = getStr16()
        messages.hints.text = getStr16()
        messages.victory.text = getStr16()
        messages.loss.text = getStr16()
        messages.history.text = getStr16()
        if (self.version >= 1.22):
            messages.scouts.text = getStr16()

        # section: CINEMATICS
        scenario.cinematics.intro = getStr16()
        scenario.cinematics.defeat = getStr16()
        scenario.cinematics.victory = getStr16()

        # section: BACKGROUND
        scenario.background.filename = getStr16()
        scenario.background.included = getInt32()
        scenario.background.width = getInt32()
        scenario.background.height = getInt32()

        self.scenario.background.include = getInt16()
        include = self.scenario.background.include
        if (include == -1 or include == 2):
            scenario.size = getUInt32()
            scenario.width = getInt32()
            scenario.height = getInt32()
            scenario.planes = getInt16()
            scenario.bitCount = getInt16()
            scenario.compression = getInt32()
            scenario.sizeImage = getInt32()
            scenario.xPels = getInt32()
            scenario.yPels = getInt32()
            scenario.colors = getUInt32()
            scenario.iColors = getInt32()
            scenario.colorTable = getBytes(scenario.colors*4)
            scenario.rawData = getBytes(scenario.sizeImage)

        # section: PLAYER DATA 2
        for i in range(16):
            getStr16()
            getStr16()

        for i in range(8):
            players[i+1].ai.name = getStr16()
        for i in range(8):
            getStr16()  # Other players ai names

        for i in range(8):
            getInt32()  # Unknown 1
            getInt32()  # Unknown 2
            players[i+1].ai.source = getStr32()
        for i in range(8):  # for another 8 players
            skip(8)
            getStr32()

        for i in range(8):
            players[i+1].ai.type = getInt8()
        skip(8)  # Other players AI TYPE
        skip(4)  # Separator 0xFFFFFF9D
        skip(16*24)  # Unused resources
        skip(4)  # another separator

        # section: Goals
        """!
            @todo optimize this section with 1 unpack
        """
        goals = scenario.goals
        goals.conquest = getInt32()
        goals.unknown1 = getInt32()
        goals.relics = getInt32()
        goals.unknown2 = getInt32()
        goals.exploration = getInt32()
        goals.unknown3 = getInt32()
        goals.all = getInt32()
        goals.mode = getInt32()
        goals.score = getInt32()
        goals.time = getInt32()

        # section: Diplomacy
        for i in range(8):
            for j in range(8):
                players[i].diplomacy[j] = getInt32()
            skip(8*4)  # skip another 8 unused players
        skip(8*16*4)  # skip another 8 unused player, with 16 dipls

        skip(11520)  # unused space
        skip(4)  # separator
        skip(16*4)  # allied victory, ignored

        skip(16*4)  # techs count
        for i in range(8):
            players[i].disabledTech = unpack('i'*30)
        skip(4*8*30)  # skip for another players
        if version >= 1.30:
            for i in range(8):
                players[i].disabledTechExtra = unpack('i'*30)
            skip(4*8*30)

        skip(16*4)  # units count
        for i in range(8):
            players[i].disabledUnits = unpack('i'*30)
        skip(4*8*30)  # skip for another players
        if version >= 1.30:
            for i in range(8):
                players[i].disabledUnitsExtra = unpack('i'*30)
            skip(4*8*30)

        skip(16*4)  # buildings count
        for i in range(8):
            players[i].disabledBuildings = unpack('i'*20)
        skip(4*8*20)  # skip for another players
        if version >= 1.30:
            for i in range(8):
                players[i].disabledBuildingsExtra = unpack('i'*40)
            skip(4*8*40)

        getInt32()  # unused
        getInt32()  # unused
        getInt32()  # All tech
        for i in range(8):
            players[i+1].age = getInt32()
        players[0].age = getUInt32()  # for gaia player
        skip(7*4)  # another players

        skip(4)  # separator
        x, y = getInt32(), getInt32()  # starting camera
        if version >= 1.21:
            scenario.map.aiType = getUInt32()
        w = getInt32()
        h = getInt32()
        scenario.map.camera = x, y
        scenario.map.resize(w, h)

        for tile in self.scenario.tiles:
            tile.type = getInt8()
            tile.elevation = getInt8()
            tile.unknown = getInt8()

        skip(4)  # number of units section

        for i in range(8):
            resource = players[i+1].resource
            resource.food = getFloat()
            resource.wood = getFloat()
            resource.gold = getFloat()
            resource.stone = getFloat()
            resource.ore = getFloat()
            getFloat()  # padding
            if version >= 1.21:
                players[i+1].population = getFloat()

        # Units section
        for i in range(9):
            units = getUInt32()
            newUnit = players[i].units.new
            for u in range(units):
                newUnit(x=getFloat(), y=getFloat(),
                     unknown1=getFloat(), id=getUInt32(), type=getUInt16(),
                     unknown2=getInt8(), angle=getFloat(), frame=getUInt16(),
                     inId=getInt32())

        skip(4)  # number of plyers, again
        for i in range(1, 9):  # only for playable players
            players[i].constName = getStr16()
            players[i].camera.x = getFloat()
            players[i].camera.y = getFloat()
            players[i].camera.unknown1 = getInt16()
            players[i].camera.unknown2 = getInt16()
            players[i].allyVictory = getInt8()
            dip = getUInt16()  # Player count for diplomacy
            skip(dip*1)  # 0 = allied, 1 = neutral, 2 = ? , 3 = enemy
            #  skip(dip*4)  # 0 = GAIA, 1 = self,
            #  2 = allied, 3 = neutral, 4 = enemy
            for j in range(9):
                players[i].diplomacy.gaia[j] = getInt32()
            players[i].color = getUInt32()
            unk1 = getFloat()
            unk2 = getUInt16()
            if unk1 == 2.0:
                skip(8*1)
            skip(unk2*44)
            skip(7*1)
            skip(4)
        skip(8)
        getInt8()  # unknown

        n = getUInt32()  # number of triggers
        for t in range(n):
            # print("Trigger: {}".format(t))
            triggers.new(
                    enable=getUInt32(),
                    loop=getUInt32(),
                    unknown1=getInt8(),
                    objective=getInt8(),
                    objectiveOrd=getUInt32(),
                    unknown2=getUInt32(),
                    text=getStr32(),
                    name=getStr32()
                )

            ne = getInt32()  # number of effects
            for e in range(ne):
                # print("\tEffect: {}".format(e))
                triggers[t].newEffect(
                    type=getInt32(),
                    check=getInt32(),
                    aiGoal=getInt32(),
                    amount=getInt32(),
                    resource=getInt32(),
                    state=getInt32(),
                    selectedCount=getInt32(),
                    unitId=getInt32(),
                    unitName=getInt32(),
                    sourcePlayer=getInt32(),
                    targetPlayer=getInt32(),
                    tech=getInt32(),
                    stringId=getInt32(),
                    unknown1=getInt32(),
                    time=getInt32(),
                    triggerId=getInt32(),
                    x=getInt32(), y=getInt32(),
                    x1=getInt32(), y1=getInt32(),
                    x2=getInt32(), y2=getInt32(),
                    unitGroup=getInt32(),
                    unitType=getInt32(),
                    instructionId=getInt32(),
                    text=getStr32(),
                    filename=getStr32()
                    )
                for k in range(triggers[t].effects[e].selectedCount):
                    triggers[t].effects[e].unitIds.append(getInt32())
            skip(ne*4)  # effects order

            nc = getInt32()  # number of conditions
            for c in range(nc):
                # print("\tCondition: {}".format(c))
                triggers[t].newCondition(
                    type=getUInt32(),
                    check=getInt32(),
                    amount=getInt32(),
                    resource=getInt32(),
                    unitObject=getInt32(),
                    unitId=getInt32(),
                    unitName=getInt32(),
                    sourcePlayer=getInt32(),
                    tech=getInt32(),
                    timer=getInt32(),
                    unknown1=getInt32(),
                    x1=getInt32(), y1=getInt32(),
                    x2=getInt32(), y2=getInt32(),
                    unitGroup=getInt32(),
                    unitType=getInt32(),
                    aiSignal=getInt32()
                    )
            skip(nc*4)  # conditions order
        skip(n*4)

        debug.included = getUInt32()
        debug.error = getUInt32()
        if debug.included:
            debug.raw = getBytes(396)  # AI DEBUG file
        """
        for i in range(1, 9):
            scenario.players[i].constName   = getStr16()
            scenario.players[i].cameraX     = getFloat()
            scenario.players[i].cameraY     = getFloat()
            scenario.players[i].cameraXX    = getInt16()
            scenario.players[i].cameraYY    = getInt16()
            scenario.players[i].allyVictory = getInt8()
        """
