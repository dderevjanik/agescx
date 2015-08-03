class Cinematics:

    """Cinematics

    Attributes:
        intro (str): intro video filename
        defeat (str): defeat video filename
        victory (str): victory video filename

    Todo:
        add more functions
    """

    def __init__(self):
        """Initialize cinematics section"""
        self.intro = ""
        self.defeat = ""
        self.victory = ""

    def __repr__(self):
        name = "Cinematics: \n"
        intro = "\tintro: {}\n".format(self.intro)
        defeat = "\tdefeat: {}\n".format(self.defeat)
        vict = "\tvictory: {}\n".format(self.victory)
        return name + intro + defeat + vict
