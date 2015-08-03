from .utilities import *
from .controller import *
from .models import *
import zlib


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
            0                     # stra0 = Z_DEFAULT_STRATEGY
                                  #   tegy:
                                  #   1 = Z_FILTERED
                                  #   2 = Z_HUFFMAN_ONLY
                                  #   3 = Z_RLE
                                  #   4 = Z_FIXED
    )

    deflated = compress.compress(data)
    deflated += compress.flush()

    return deflated


class Compress:

    def __init__(self, scenario, path, version=1.21, temp=True):
        self.scenario = scenario
        self.version = version
        print(path)
        f1 = open('c1.temp', 'wb')
        f2 = open('c2.temp', 'wb')
        self.compressHeader(f1)
        self.compressData(f2)
        f1.close()
        f2.close()
        data = open('c1.temp', 'rb').read()
        d = deflate(open('c2.temp', 'rb').read())
        open(path, 'wb').write(data + d)

    def compressHeader(self, f):
        encoder = Encoder(f)
        scenario = self.scenario

        putAscii = encoder.putAscii
        putUInt32 = encoder.putUInt32
        putInt32 = encoder.putInt32
        putStr32 = encoder.putStr32

        putAscii(scenario.version[:4])
        putInt32(20 + len(scenario.instructions))  # header length
        putInt32(2)  # unknown constant
        putInt32(scenario.timestamp)
        putStr32(scenario.instructions)
        putUInt32(0)  # unknown constant
        putUInt32(scenario.plrnumb)

    def compressData(self, f):
        encoder = Encoder(f)
        version = self.version

        scenario = self.scenario
        players = self.scenario.players
        messages = self.scenario.messages
        triggers = self.scenario.triggers
        debug = self.scenario.debug

        putAscii = encoder.putAscii
        putUInt32 = encoder.putUInt32
        putInt8 = encoder.putInt8
        putInt16 = encoder.putInt16
        putUInt16 = encoder.putUInt16
        putInt32 = encoder.putInt32
        putStr16 = encoder.putStr16
        putStr32 = encoder.putStr32
        putFloat = encoder.putFloat
        putBytes = encoder.putBytes

        putUInt32(Units.nextID)
        putFloat(scenario.version2)

        for i in range(1, 9):
            putAscii(players[i].name, 256)
        putAscii('\x00' * 8 * 256)

        if version >= 1.18:
            for i in range(8):
                putInt32(players[i + 1].nameID)
            for i in range(8):
                putInt32(-1)

        for i in range(8):
            putUInt32(players[i].active)
            putUInt32(players[i].human)
            putUInt32(players[i].civilization)
            putUInt32(players[i].unknown1)
        for i in range(8):
            putUInt32(0)
            putUInt32(0)
            putUInt32(0)
            putUInt32(0)

        putUInt32(0)  # unknown <!>
        putFloat(0)  # unknown <!>
        putAscii('.')  # separator
        putStr16(scenario.filename)

        putInt32(messages.objectives.id)
        putInt32(messages.hints.id)
        putInt32(messages.victory.id)
        putInt32(messages.loss.id)
        putInt32(messages.history.id)
        putInt32(messages.scouts.id)
        putStr16(messages.objectives.text)
        putStr16(messages.hints.text)
        putStr16(messages.victory.text)
        putStr16(messages.loss.text)
        putStr16(messages.history.text)
        putStr16(messages.scouts.text)

        putStr16(scenario.cinematics.intro)
        putStr16(scenario.cinematics.defeat)
        putStr16(scenario.cinematics.victory)

        putStr16(scenario.background.filename)

        putInt32(scenario.background.included)
        putInt32(scenario.background.width)
        putInt32(scenario.background.height)
        putInt16(scenario.background.include)

        if (scenario.background.include == - 1 or scenario.background.include == 2):
            putUInt32(scenario.size)
            putInt32(scenario.width)
            putInt32(scenario.height)
            putInt16(scenario.planes)
            putInt16(scenario.bitCount)
            putInt32(scenario.compression)
            putInt32(scenario.sizeImage)
            putInt32(scenario.xPels)
            putInt32(scenario.yPels)
            putUInt32(scenario.colors)
            putInt32(scenario.iColors)
            putBytes(scenario.colorTable)
            putBytes(scenario.rawData)

        for i in range(16):
            putStr16('')
            putStr16('')

        for i in range(8):
            putStr16(players[i+1].ai.name)
        for i in range(8):
            putStr16('RandomGame')  # unused 8 Players

        for i in range(8):
            putInt32(0)
            putInt32(0)
            putStr32(players[i+1].ai.source)
        for i in range(8):  # for unused Players
            putInt32(0)
            putInt32(0)
            putStr32('')

        for i in range(8):
            putInt8(players[i+1].ai.type)
        for i in range(8):  # for unused Players
            putInt8(0)

        putUInt32(4294967197)  # Separator 0xFFFFFF9D
        for i in range(8):
            putUInt32(int(players[i+1].resource.gold))
            putUInt32(int(players[i+1].resource.wood))
            putUInt32(int(players[i+1].resource.food))
            putUInt32(int(players[i+1].resource.stone))
            putUInt32(int(players[i+1].resource.ore))
            putUInt32(0)  # pading
        for i in range(6*8):
            putUInt32(0)
        putUInt32(4294967197)  # Separator, again 0xFFFFFF9D

        putInt32(scenario.goals.conquest)
        putInt32(scenario.goals.unknown1)
        putInt32(scenario.goals.relics)
        putInt32(scenario.goals.unknown2)
        putInt32(scenario.goals.exploration)
        putInt32(scenario.goals.unknown3)
        putInt32(scenario.goals.all)
        putInt32(scenario.goals.mode)
        putInt32(scenario.goals.score)
        putInt32(scenario.goals.time)

        for i in range(8):
            for j in range(8):
                putInt32(players[i].diplomacy[j])
            for x in range(8):  # unused Players
                putInt32(0)
        for x in range(8*16):  # unused Players
            putInt32(0)

        putAscii('\x00' * 11520)  # unused space
        putUInt32(4294967197)  # separator

        # todo: finished allied victory
        for i in range(16):  # allied victory, ignored
            putInt32(0)

        # todo: tech counts doesn't work
        for i in range(8):  # tech count
            putInt32(0)
        for i in range(8):  # unused Players
            putInt32(-1)
        for i in range(16):  # techs
            for j in range(30):
                putInt32(-1)

        for i in range(8):  # unit count
            putInt32(0)
        for i in range(8):  # unused Players
            putInt32(-1)
        for i in range(16):  # units
            for j in range(30):
                putInt32(-1)

        for i in range(8):  # building count
            putInt32(0)
        for i in range(8):  # unused Players
            putInt32(-1)
        for i in range(16):  # buildings
            for j in range(20):
                putInt32(-1)

        putUInt32(0)
        putUInt32(0)
        putUInt32(0)  # todo: All techs

        for i in range(8):
            putInt32(players[i+1].age)
        print(players[0].age)
        putUInt32(players[0].age)  # for gaia player
        for i in range(7):  # unused Players
            putInt32(-1)
        putUInt32(4294967197)
        putInt32(scenario.map.camera[0])  # warning: doesn't match
        putInt32(scenario.map.camera[1])  # warning: doesn't match
        putUInt32(scenario.map.aiType)
        putInt32(scenario.tiles.size()[0])
        putInt32(scenario.tiles.size()[1])

        # warning: not sure about this
        for tile in scenario.tiles:
            putInt8(tile.type)
            putInt8(tile.elevation)
            putInt8(tile.unknown)

        putUInt32(9)  # number of units section

        for i in range(8):
            putFloat(players[i+1].resource.food)
            putFloat(players[i+1].resource.wood)
            putFloat(players[i+1].resource.gold)
            putFloat(players[i+1].resource.stone)
            putFloat(players[i+1].resource.ore)
            putFloat(0)
            if version >= 1.21:
                putFloat(players[i+1].population)

        for i in range(9):
            # warning: maybe not correct value
            putUInt32(len(players[i].units))
            for unit in players[i].units:
                putFloat(unit.x)
                putFloat(unit.y)
                putFloat(unit.unknown1)
                putUInt32(unit.id)
                putUInt16(unit.type)
                putInt8(unit.unknown2)
                putFloat(unit.angle)
                putUInt16(unit.frame)
                putInt32(unit.inId)

        putUInt32(9)  # number of playable players
        for i in range(1, 9):
            putStr16(players[i].constName)
            putFloat(players[i].camera.x)
            putFloat(players[i].camera.y)
            putInt16(players[i].camera.unknown1)
            putInt16(players[i].camera.unknown2)
            putInt8(players[i].allyVictory)
            putUInt16(9)  # players for diplomacy
            for j in range(8):
                putInt8(players[i].diplomacy[j])
            putInt8(0)  # gaia player
            for j in range(9):  # for gaia
                putInt32(players[i].diplomacy.gaia[j])
            putUInt32(players[i].color)
            putFloat(2.0)
            putUInt16(0)
            for j in range(8):
                putInt8(0)
            for j in range(7):
                putInt8(0)
            putInt32(-1)
        putUInt32(2576980378)
        putUInt32(1073322393)
        putInt8(0)
        putInt32(len(triggers))

        for trigger in triggers:
            putUInt32(trigger.enable)
            putUInt32(trigger.loop)
            putInt8(trigger.unknown1)
            putInt8(trigger.objective)
            putUInt32(trigger.objectiveOrder)
            putUInt32(trigger.unknown2)
            putStr32(trigger.text)
            putStr32(trigger.name)
            putInt32(len(trigger.effects))
            for e in range(len(trigger.effects)):
                effect = trigger.effects[e]
                putInt32(effect.type)
                putInt32(effect.check)
                putInt32(effect.aiGoal)
                putInt32(effect.amount)
                putInt32(effect.resource)
                putInt32(effect.state)
                putInt32(effect.selectedCount)
                putInt32(effect.unitId)
                putInt32(effect.unitName)
                putInt32(effect.sourcePlayer)
                putInt32(effect.targetPlayer)
                putInt32(effect.tech)
                putInt32(effect.stringId)
                putInt32(effect.unknown1)
                putInt32(effect.time)
                putInt32(effect.triggerId)
                putInt32(effect.x)
                putInt32(effect.y)
                putInt32(effect.x1)
                putInt32(effect.y1)
                putInt32(effect.x2)
                putInt32(effect.y2)
                putInt32(effect.unitGroup)
                putInt32(effect.unitType)
                putInt32(effect.instructionId)
                putStr32(effect.text)
                putStr32(effect.filename)
                for id in effect.unitIds:
                    putInt32(id)
            for i in range(len(trigger.effects)):
                putInt32(i)
            putInt32(len(trigger.conditions))
            for c in range(len(trigger.conditions)):
                condition = trigger.conditions[c]
                putUInt32(condition.type)
                putInt32(condition.check)
                putInt32(condition.amount)
                putInt32(condition.resource)
                putInt32(condition.unitObject)
                putInt32(condition.unitId)
                putInt32(condition.unitName)
                putInt32(condition.sourcePlayer)
                putInt32(condition.tech)
                putInt32(condition.timer)
                putInt32(condition.unknown1)
                putInt32(condition.x1)
                putInt32(condition.y1)
                putInt32(condition.x2)
                putInt32(condition.y2)
                putInt32(condition.unitGroup)
                putInt32(condition.unitType)
                putInt32(condition.aiSignal)
            for i in range(len(trigger.conditions)):
                putInt32(i)
        for i in range(len(triggers)):
            putInt32(i)
        putUInt32(0)
        putUInt32(0)

# = open('')
if __name__ == "__main__":
    pass
