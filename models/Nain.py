from models.Heros import Heros


class Nain(Heros):

    def __init__(self, nom):
        super().__init__(nom)

    @property
    def endurance(self):
        return super().endurance + 2