from voiture import Voiture
from bus import Bus

if __name__ == '__main__':

    """ create an instance of class voiture"""
    voiture1 = Voiture("BG-564-NB", "white", 5)
    print("My car is {} , has {} doors and my matricule is {}".format(voiture1.color, voiture1.number_doors, voiture1.immatriculation))

    """create an instance of class bus"""
    bus1 = Bus("XX-111-XXX", "blue", 2)
    print("this bus is {} , has {} floors and its matricule is {}".format(bus1.color, bus1.number_floors, bus1.immatriculation))


    voiture2 = Voiture("BG-564-NB", "white", 3)
    print(voiture2.immatriculation, voiture2.color, voiture2.number_doors)
    bus2 = Bus("XX-000-ZZ", "blue", 2)
    print(bus2.immatriculation, bus2.color, bus2.number_floors)
