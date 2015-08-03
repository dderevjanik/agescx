class Message:

    """Messsage contains ID and Text

    Attributes:
        id (int): string ID
        text (str): text
    """

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __init__(self, text="", id=0):
        self._id = id
        self._text = text


class Messages:

    """Messages in objective menu

    Attributes:
        briefing (Message): briefing text
        objectives (Message): objectives text
        hints (Message): hints text
        victory (Message): victory text
        loss (Message): loss text
        history (Message): history text
        scouts (Message): scouts text
    """

    @property
    def briefing(self):
        return self._briefing

    @property
    def objectives(self):
        return self._objectives

    @property
    def hints(self):
        return self._hints

    @property
    def victory(self):
        return self._victory

    @property
    def loss(self):
        return self._loss

    @property
    def history(self):
        return self._history

    @property
    def scouts(self):
        return self._scouts

    def __init__(self):
        self._briefing = Message()
        self._objectives = Message()
        self._hints = Message()
        self._victory = Message()
        self._loss = Message()
        self._history = Message()
        self._scouts = Message()

    def __len__(self):
        """Number of characters occured in all messages

        Return:
            (int): character count
        """
        l1 = len(self.briefing) + len(self.objectives)
        l2 = len(self.victory) + len(self.loss)
        l3 = len(self.history) + len(self.scouts)
        return l1 + l2 + l3

    def __repr__(self):
        name = "Messages: \n"
        brief = "\tbriefing: {}\n".format(self.briefing)
        instr = "\tobjectives ({}): {}\n".format(
            self.objectivesID, self.objectives)
        vict = "\tvictory ({}): {}\n".format(self.victoryID, self.victory)
        loss = "\tloss ({}): {}\n".format(self.lossID, self.loss)
        hist = "\thistory ({}): {}\n".format(self.historyID, self.history)
        scout = "\tscout ({}): {} \n".format(self.scoutsID, self.scouts)
        return name + brief + instr + vict + loss + hist + scout
