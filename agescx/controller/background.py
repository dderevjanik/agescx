class Background:

    """pre-game background image

    Attributes:
        filename (str): image filename
        included (int): is image included ?

    Todo:
        load() -load image from a file
        save() -save image to a file
    """

    def __init__(self, filename="", included=0,  size=0,
                 width=0, height=0, include=0, planes=0,
                 bitCount=0, compression=0, sizeImage=0,
                 xPels=0, yPels=0, colors=0, iColors=0,
                 colorTable=[], rawData=[]):
        self.filename = filename
        self.included = included
        self.width = width
        self.height = height
        self.include = include
        self.size = size
        self.planes, self.bitCount = planes, bitCount
        self.compression, self.sizeImage = compression, sizeImage
        self.xPels, self.yPels, self.colors = xPels, yPels, colors
        self.iColors, self.colorTable, self.rawData = iColors, colorTable, rawData

    def __len__(self):
        """
        Todo:
            Finish, return size of image in bytes
        """
        pass

    def __repr__(self):
        name = "Background: \n"
        fname = "\tfilename: {}\n".format(self.filename)
        size = "\tsize: {}\n".format(self.size)
        prop = "\twidth: {}\n\theight: {}\n".format(self.width, self.height)
        return name + fname + size + prop

    def size(self):
        """size of Background

        Return:
            (tuple): width and height
        """
        pass
