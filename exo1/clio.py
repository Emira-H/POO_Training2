"""
Class which create a car Clio with attributs of instances: number_doors,
color, color_number and attributs of class: price

"""
class Clio:
    doors = [3, 5]
    colors = {
    "yellow":"126736",
    "red":"267679",
    "blue": "7829729",
    "black":"791797",
    "white":"7979702"
     }
    prices = [8000, 30000]
    price = 40000
#constructor with the 3 attributs
    def __init__(self, number_doors,color, color_number):
        self.number_doors = number_doors
        self.color = color
        self.color_number = color_number
#Encapsulation with getter number_doors which privates the attribut number_doors
    @property
    def number_doors(self):
        return self.__number_doors
#setter number_doors which must be in doors the attribut of class. If note we
#raise an exception with a message
    @number_doors.setter
    def number_doors(self, number_doors):
        if number_doors in Clio.doors:
            self.__number_doors = number_doors
        else:
            raise ValueError("This model exists only in 3 or 5 doors!")
#decorator for color and check if the instance is called with a value of attribut
#which in {}
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        if color in Clio.colors.keys():
            self.__color = color
        else:
            raise ValueError("This color is not avalaible")
#method of class for checking if price which is an attribut of class is allowed
    @classmethod
    def check_price(cls):
        if cls.price in range(Clio.prices[0], Clio.prices[1]):
            return cls.price
        else:
            raise ValueError("the price should be between 8000€ and 30000€")
