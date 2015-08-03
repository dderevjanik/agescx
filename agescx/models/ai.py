class AI:

    """Player defined AI

    Attributes:
        name (str): AI name
        source (str): source code or .PER file
        type (int): AI type
        unknown1 (int): unknown1
        unknown2 (int): unknown2
    """

    def __init__(self, name="", source="", type=0,
                 unknown1=0, unknown2=0):
        """Create player defined AI

        Args:
            name (str, optional): name of AI, ""
            source (str, optional): source code of AI, ""
            type (int, optional): AI type
            unknown1 (int, optional): unknown, 0
            unknown2 (int, optional): unknown, 0
        """
        self.name = name
        self.type = type
        self.source = source
        self.unknown1 = unknown1
        self.unknown2 = unknown2

    def __repr__(self):
        name = "AI:\n"
        info = "\tname: {}\n\tsource length: {}\n".format(
            self.name, len(self.source))

        t = ""
        if self.type == 0:
            t = "0 (Custom)"
        elif self.type == 1:
            t = "1 (Standard)"
        elif self.type == 2:
            t = "2 (None)"

        info2 = "\ttype: {}\n".format(t)
        info3 = "\tunknown1: {}\n\tunknown2: {}\n".format(
            self.unknown1, self.unknown2)

        return name + info + info2 + info3

    def toJSON(self):
        """return JSON"""
        data = dict()
        data['name'] = self.name
        data['type'] = self.type
        data['source'] = self.source
        return data

    def readSource(self, filename):
        """Load source code from file

        Args:
            filename (str): file, from which AI will be loaded

        Return:
            (int): number of characters readed
        """
        f = open(filename, 'r', encoding='utf-8')
        self.source = f.read()
        f.close()

        return len(self.source)

    def saveSource(self, filename):
        """Save source code from AI to a file

        Args:
            filename (str): file, in which AI will be written
        """
        f = open(filename, 'w')
        f.write(self.source)
        f.close()

    def clear(self):
        """Remove AI

        Todo:
            not sure with TYPE
        """
        self.name = ""
        self.source = ""
        self.type = 0
