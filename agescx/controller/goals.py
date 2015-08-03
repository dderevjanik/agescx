class Goals:

    """Represents scenario goals

    Attributes:
        conquest (int): 1 conquest
        unknown1 (int): unknown
        relics (int): number of relics required
        unknown2 (int): unknown
        exploration (int): map exploratino required in %
        all (int): all conditions
        mode (int): ?
        score (int): number of score required
        time (int): time required (100 = 10yr)
    """

    def __init__(self, conquest=0, unknown1=0,
                 relics=0, unknown2=0,
                 exploration=0, unknown3=0,
                 all=0, mode=0, score=0, time=0):
        """Initialize scenario goals

        Args:
            conquest (int): 1 conquest
            unknown1 (int): unknown
            relics (int): number of relics required
            unknown2 (int): unknown
            exploration (int): map exploratino required in %
            all (int): all conditions
            mode (int): ?
            score (int): number of score required
            time (int): time required (100 = 10yr)

        Todo:
            describe mode param
        """
        self.conquest = conquest
        self.unknown1 = unknown2
        self.relics = relics
        self.unknown2 = unknown2
        self.exploration = exploration
        self.unknown3 = unknown3
        self.all = all
        self.mode = mode
        self.score = score
        self.time = time

    def __repr__(self):
        name = "Goals: \n"
        part1 = "\tConquest: {}\n\tRelics: {}\n".format(
            self.conquest, self.relics)
        part2 = "\tExploration: {}\n\tAllModes: {}\n".format(
            self.exploration, self.all)
        part3 = "\tCustomMode: {}\n\tScore: {}\n".format(self.mode, self.time)
        part4 = "\tTime: {}\n".format(self.time)

        return name + part1 + part2 + part3 + part4
