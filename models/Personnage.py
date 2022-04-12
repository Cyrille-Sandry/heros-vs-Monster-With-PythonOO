from models.De import De
from helper.Generateur import Generateur

class Personnage:

    def __init__(self):
        self.__endurance = Generateur.get_carac()
        self.__force = Generateur.get_carac()
        self.__pdv = self.pdv_max
        self.__d4 = De(4)
        self.__d6 = De(6)

    @property
    def endurance(self):
        return self.__endurance

    @property
    def force(self):
        return self.__force

    @property
    def pdv(self):
        return self.__pdv

    @pdv.setter
    def pdv(self, value):
        if value < self.pdv_max:
            self.__pdv = value
        else:
            self.__pdv = self.pdv_max

    @property
    def d4(self):
        return self.__d4

    @property
    def d6(self):
        return self.__d6

    @property
    def pdv_max(self):
        return self.__endurance + Generateur.get_modificateur(self.__endurance)

    @property
    def race(self):
        return self.__class__.__name__

    # Méthodes
    def est_mort(self):
        return self.pdv <= 0

    def frappe(self, p):
        if not isinstance(p, Personnage):
            raise NameError("Tu ne peux taper que des personnages")

        degat = self.d4.lancer() + Generateur.get_modificateur(self.force)
        p.pdv = p.pdv - degat

if __name__ == "__main__":
    personnage = Personnage()
    print(personnage.race)