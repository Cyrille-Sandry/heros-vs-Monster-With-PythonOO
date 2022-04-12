from models.Humain import *
from models.Nain import *
from models.Loup import *
from models.Orque import *
from models.Dragonnet import *
from models.De import *

joueur = input("Quel est le nom de votre héros ? ")

race = None
while race is None:
    choix = input("Humain (1) ou Nain (2) ?")
    if choix.isdigit():
        choix_int = int(choix)
        if choix_int == 1 or choix_int == 2:
            race = choix_int
        else:
            print("Choix incorrect")
    else:
        print("Vous devez choisir 1 ou 2")

hero = Humain(joueur) if race == 1 else Nain(joueur)

print("Votre", hero.race, "- force :", hero.force, " / endurance :", hero.endurance, " / pdv:", hero.pdv)
print()

d2 = De(2)
d3 = De(3)

while not hero.est_mort():

    choix_monstre = d3.lancer()
    if choix_monstre == 1:
        creature = Loup()
    elif choix_monstre == 2:
        creature = Orque()
    else:
        creature = Dragonnet()

    print("Votre hero rencontre un", creature.race,"!")

    initiative = d2.lancer() == 1
    while not hero.est_mort() and not creature.est_mort():
        if initiative:
            hero.frappe(creature)
            print("Le hero attaque")
        else:
            creature.frappe(hero)
            print("La créature attaque")

        initiative = not initiative

    if not hero.est_mort():
        print(hero.nom,"a vaincu le", creature.race)
        hero.loot(creature)
        hero.se_reposer()

    print()

print("Le héro est mort")
print("Burtin :", hero.piece_or, " pieces d'or,",hero.cuir, "cuirs")