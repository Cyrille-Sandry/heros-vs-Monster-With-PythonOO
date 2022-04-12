from models.Monstre import Monstre
from interfaces.ICuir import ICuir
from interfaces.IOr import IOr


class Dragonnet(Monstre, IOr, ICuir):

    def __init__(self):
        super().__init__()
        self.__cuir = self.d4.lancer()
        self.__piece_or = self.d6.lancer()

    @property
    def endurance(self):
        return super().endurance + 1

    @property
    def piece_or(self):
        return self.__piece_or

    @property
    def cuir(self):
        return self.__cuir
