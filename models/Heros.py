from models.Personnage import Personnage
from interfaces.IOr import IOr
from interfaces.ICuir import ICuir


class Heros(Personnage, IOr, ICuir):

    def __init__(self, nom):
        super().__init__()
        self.__nom = nom
        self.__cuir = 0
        self.__piece_or = 0

    @property
    def nom(self):
        return self.__nom

    @property
    def piece_or(self):
        return self.__piece_or

    @property
    def cuir(self):
        return self.__cuir

    # Méthode
    def loot(self, monstre):
        if isinstance(monstre, IOr):
            self.__piece_or += monstre.piece_or

        if isinstance(monstre, ICuir):
            self.__cuir += monstre.cuir

    def se_reposer(self):
        self.pdv = self.pdv_max
