from vehicule import Vehicule

'''class daughter from class vehicule'''

class Voiture(Vehicule):
    number_doors = (3, 5)
    def __init__(self, immatriculation, color, number_doors):
        Vehicule.__init__(self, immatriculation, color)
        self.number_doors = number_doors
