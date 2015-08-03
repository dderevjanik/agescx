import struct


class Decoder:

    """Decoder create support dynamical reading and converting from a file"""

    def __init__(self, binaries):
        self.__pntr = 0
        self.__data = binaries

    """
        Todo:
            finish descriptions
    """

    def getStr32(self):
        self.__pntr += 4
        temp = struct.unpack('i', self.__data[self.__pntr - 4:self.__pntr])[0]
        self.__pntr += temp
        return self.__data[self.__pntr - temp:self.__pntr].decode('utf-8')

    def getStr16(self):
        self.__pntr += 2
        temp = struct.unpack('h', self.__data[self.__pntr - 2:self.__pntr])[0]
        self.__pntr += temp
        return self.__data[self.__pntr - temp:self.__pntr].decode('utf-8')

    def getDouble(self):
        self.__pntr += 8
        return struct.unpack('d', self.__data[self.__pntr - 8:self.__pntr])

    def getInt32(self):
        self.__pntr += 4
        return struct.unpack('i', self.__data[self.__pntr - 4:self.__pntr])[0]

    def getUInt32(self):
        self.__pntr += 4
        return struct.unpack('I', self.__data[self.__pntr - 4:self.__pntr])[0]

    def getInt16(self):
        self.__pntr += 2
        return struct.unpack('h', self.__data[self.__pntr - 2:self.__pntr])[0]

    def getUInt16(self):
        self.__pntr += 2
        return struct.unpack('H', self.__data[self.__pntr - 2:self.__pntr])[0]

    def getFloat(self):
        self.__pntr += 4
        return struct.unpack('f', self.__data[self.__pntr - 4:self.__pntr])[0]

    def getInt8(self):
        self.__pntr += 1
        return ord(self.__data[self.__pntr - 1:self.__pntr])

    def getAscii(self, length):
        self.__pntr += length
        return self.__data[self.__pntr - length:self.__pntr].decode('utf-8').replace('\x00', ' ')

    def getBytes(self, length):
        self.__pntr += length
        return self.__data[self.__pntr - length:self.__pntr]

    def unpack(self, datatype):
        """Unpack datatypes from binarie file

        Args:
            datatype (str): datatype(s)

        Return:
            (tuple): converted datatypes
        """
        size = struct.calcsize(datatype)
        ret = struct.unpack(
            datatype, self.__data[self.__pntr:self.__pntr + size])
        self.__pntr += size
        return ret

    def offset(self):
        """Get decode position

        Return:
            (int): current position in file
        """
        return self.__pntr

    def decode(self, datatype):
        """Unpack datatypes from binarie file

        Args:
            datatype (str): datatype(s)

        Return:
            (tuple): converted datatypes
        """
        unpack = struct.unpack
        pntr = self.__pntr
        data = self.__data

        value = None
        temp = None

        datatypes = datatype.split('-')
        if len(datatypes) > 1:
            ret = tuple()
            for d in datatypes:
                ret += (self.decode(d),)
            return ret
        else:
            if 'ascii' in datatype:
                value = datatype.split()[1]
                self.__pntr += int(value)
                return data[self.__pntr - int(value):self.__pntr]
            if 'str' in datatype:
                if '32' in datatype:
                    value = self.decode('i')
                else:  # 16bit string
                    value = self.decode('h')
                temp = data[self.__pntr:self.__pntr + int(value)]
                self.__pntr += len(temp)
                return temp.decode('utf-8')
            if datatype == 'i':  # integer
                value = unpack(datatype, data[pntr:pntr + 4])
                self.__pntr += 4
                return value[0]
            elif datatype == 'I':  # unsigned integer
                value = unpack(datatype, data[pntr:pntr + 4])
                self.__pntr += 4
                return value[0]
            elif datatype == 'h':  # short
                value = unpack(
                    datatype, self.__data[self.__pntr:self.__pntr + 2])
                self.__pntr += 2
                return value[0]
            elif datatype == 'H':  # unsigned short
                value = unpack(datatype, data[pntr:pntr + 2])
                self.__pntr += 2
                return value[0]
            elif datatype == 'f':  # 32b float
                value = unpack(datatype, data[pntr:pntr + 4])
                self.__pntr += 4
                return value[0]
            elif datatype == 'd':  # double
                value = unpack(datatype, data[pntr:pntr + 8])
                self.__pntr += 8
                return value[0]
            elif datatype == 'b':
                value = unpack(datatype, data[pntr:pntr + 1])
                self.__pntr += 1
                return value[0]

    def skip(self, size):
        """skip bytest in file

        Args:
            size (int): how many bytes to skip
        """
        self.__pntr += size
