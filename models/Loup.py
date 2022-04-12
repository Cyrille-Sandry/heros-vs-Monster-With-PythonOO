from models.Monstre import Monstre
from interfaces.ICuir import ICuir


class Loup(Monstre, ICuir):

    def __init__(self):
        super().__init__()
        self.__cuir = self.d4.lancer()

    @property
    def cuir(self):
        return self.__cuir
