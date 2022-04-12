from models.Heros import Heros


class Humain(Heros):

    def __init__(self, nom):
        super().__init__(nom)

    @property
    def endurance(self):
        return super().endurance + 1

    @property
    def force(self):
        return super().force + 1
