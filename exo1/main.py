from clio import Clio

#clio = Clio( 3, "red","126736")
print(Clio.colors["yellow"])
print(range(Clio.prices[0],Clio.prices[1]))
clio = Clio(3,"white","19020")
clio = Clio(5,"black","898989")
#clio = Clio(6,"green","898989")
clio.check_price()
