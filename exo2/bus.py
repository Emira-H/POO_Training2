from vehicule import Vehicule
'''class daughter from class vehicule'''

class Bus(Vehicule):
    floors = (1,2)
    def __init__(self, immatriculation, color, number_floors):
        super().__init__(immatriculation, color)
        self.number_floors = number_floors

    @property
    def number_floors(self):
        return self.__number_floors

    @number_floors.setter
    def number_floors(self, number_floors):
        if number_floors in Bus.floors:
            self.__number_floors= number_floors
        else:
            raise ValueError("this number of floors is not available!")
