from voiture import Voiture
from bus import Bus

voiture1 = Voiture("BG-564-NB", "white", 5)
print("My car is {} , has {} doors and my matricule is {}".format(voiture1.color, voiture1.number_doors, voiture1.immatriculation))

bus1 = Bus("XX-111-XXX", "blue", 2)
print("this bus is {} , has {} floors and its matricule is {}".format(bus1.color, bus1.number_floors, bus1.immatriculation))
