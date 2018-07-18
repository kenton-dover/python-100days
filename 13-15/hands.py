

class Rolls:
    def __init__(self, name, rollsThatWin, rollsThatDefeat):
        self.name = name
        self.rollsThatWin = rollsThatWin
        self.rollsThatDefeat = rollsThatDefeat

    def can_defeat(self, Roll):
        if Roll.name in self.rollsThatDefeat:
            return False
        elif Roll.name in self.rollsThatWin:
            return True
        else:
            return None
