from vehicule import Vehicule
'''class daughter from class vehicule'''

class Bus(Vehicule):
    number_floors = (1,2)
    def __init__(self, immatriculation, color, number_floors):
        super().__init__(immatriculation, color)
        self.number_floors = number_floors
