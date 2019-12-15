class Clio:
    doors = [3, 5]
    colors = {"yellow":"126736", "red":"267679", "blue": "7829729"}
    def __init__(self, number_doors,color_number, color, price):
        self.number_doors = number_doors
        self.color = color
        self.color_number = color_number
        self.price = price

    def check_number_doors(self):
        if self.number_doors in Clio.doors:
            return self.number_doors
        else:
            raise ValueError
