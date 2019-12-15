from person import Person
from product import Product

class Customer(Person):
    def __init__(self, name, first_name, status):
        super().__init__(name, first_name, age)
        self.basket = list()
        self.amount = 0

    
