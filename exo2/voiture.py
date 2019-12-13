from vehicule import Vehicule

'''class daughter from class vehicule'''

class Voiture(Vehicule):
    doors = (3, 5)
    def __init__(self, immatriculation, color, number_doors):
        Vehicule.__init__(self, immatriculation, color)
        self.number_doors = number_doors

    @property
    def number_doors(self):
        return self.__number_doors

    @number_doors.setter
    def number_doors(self, number_doors):
        if number_doors in Voiture.doors:
            self.__number_doors = number_doors
        else:
            raise ValueError("this number of doors is not available!")
