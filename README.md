# Heroes Vs Monsters

                   
Bienvenue dans la forêt de « Shorewood », forêt enchantée du pays de « Stormwall ».
Dans cette forêt, se livre un combat acharné entre les héros d’une part et les monstres d’autre part.
Notre rôle est de donner vie à cette forêt au travers d’un programme écrit en console reprenant tous les concepts orientés objets vu au cours.

Décrivons, un peu ce monde, nous retrouvons deux familles de personnages, les héros : Humain ou nain et les monstres : Loup, Orque ou dragonnet.
Chaque personnage possède différentes caractéristiques :

- Endurance (End),

- Force (For),

-  Points de vie (PV)

La force et l’endurance sont calculées à la création du personnage en lançant, pour chacune d’elles, quatre dé 6 faces et en n’en reprenant que les 3 meilleurs.

Les points de vie sont déterminés par l’endurance additionnée avec le modificateur1 basé sur l’endurance.
Les personnages ont une action Frappe. Lorsqu’un personnage frappe sur un autre, les dégâts sont déterminés par le jet d’un dé à 4 faces auquel on ajoute un modificateur1 basé sur la caractéristique de Force. Une fois calculé, les dégâts sont retirés des points de vies de la cible.

Les héros en tuant les monstres vont les dépouiller de leur richesse (Or et/ou Cuir) 2, qu’ils vont stocker sans limite.
Après chaque combat les héros se reposent et restaurent leurs points de vie et affronte le monstre suivant jusqu’à leur mort3.

Nous avons deux types de héros, les humains qui ont +1 aux caractéristiques de Force et d’Endurance et les nains qui ont plus 2 en Endurance.

Ensuite nous avons les monstres :

- Les loups :

o Ils peuvent être dépecés (donne du cuir).

- Les orques :

o Ils ont +1 en force
o Ils ont de l’or 

-  Les dragonnets :

o Ils ont +1 en endurance
o Ils ont de l’or
o Ils peuvent être dépecés (donne du cuir).



1. Le modificateur se base sur le score de la caractéristique pour ajouter un bonus ou un malus sur base des tests suivants : si la caractéristique est inférieure à 5 on ajoute -1, sinon si elle est inférieure à 10 alors on ajoute 0, sinon si elle est inférieure à 15 alors on ajoute +1, sinon on ajoute +2.
2. L’or et le cuir sont calculé à la création du monstre en sachant que l’or est calculé sur base d’un dé 6 faces tandis que le cuir est calculé sur base d’un dé 4 face.
3. Tout personnage meurt lorsque ses points de vies sont <= à 0.
4. La classe « Random » devrait vous aider.

Contraintes :

-  La force et l’endurance sont des propriétés en lecture seule.
-  La propriété PV est 
(Si les délégués ont été vu)
« private » aussi bien en lecture et en écriture.
(sinon)
en lecture seule.

-  Les bonus d’endurance et de force offerts par les classes (Humain, Nain, Orque et Dragonnet) ne doivent pas modifier la caractéristique de base du personnage.
-  La classe dé contient deux propriétés en lecture seule Minimum et Maximum ainsi qu’une méthode Lance qui retourne un entier aléatoire4.

