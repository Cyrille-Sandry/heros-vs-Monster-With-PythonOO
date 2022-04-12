import random

class De:

    def __init__(self, maximum):
        self.__minimum = 1
        self.__maximum = maximum

    @property
    def minimum(self):
        return self.__minimum

    @property
    def maximum(self):
        return  self.__maximum

    #Méthode
    def lancer(self):
        return random.randint(self.minimum, self.maximum)

if __name__ == "__main__":
    de = De(4)
    print(de.lancer())