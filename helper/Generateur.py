from models.De import De


class Generateur:

    @staticmethod
    def get_carac():
        de = De(6)
        stats = []

        i = 0
        while i < 4:
            stats.append(de.lancer())
            i += 1

        stats.sort()
        stats.remove(stats[0])

        return sum(stats)

    @staticmethod
    def get_modificateur(carac):
        if carac < 5:
            modif = -1
        elif carac < 10:
            modif = 0
        elif carac < 15:
            modif = 1
        else:
            modif = 2

        return modif

if __name__ == "__main__":
    print(Generateur.get_modificateur(9))