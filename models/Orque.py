from models.Monstre import Monstre
from interfaces.IOr import IOr


class Orque(Monstre, IOr):

    def __init__(self):
        super().__init__()
        self.__piece_or = self.d6.lancer()

    @property
    def force(self):
        return super().force + 1

    @property
    def piece_or(self):
        return self.__piece_or
