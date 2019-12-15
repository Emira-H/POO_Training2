class Clio:
    doors = [3, 5]
    colors = {"yellow":"126736", "red":"267679", "blue": "7829729", "black":"791797", "white":"7979702"}

    def __init__(self, number_doors, color_number, color, price):
        self.number_doors = number_doors
        self.color = color
        self.color_number = color_number
        self.price = price

    @property
    def number_doors(self):
        return self.__number_doors

    @number_doors.setter
    def number_doors(self, number_doors):
        if number_doors in Clio.doors:
            self.__number_doors = number_doors
        else:
            raise ValueError("This model exists only in 3 or 5 doors!")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color in Clio.colors.keys:
            self.__color = color
        else:
            raise ValueError("This color is not avalaible")
