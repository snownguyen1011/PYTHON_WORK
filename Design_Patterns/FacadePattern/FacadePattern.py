#################################################################################
############ LEARNING PURPOSE BELOW INFO ########################################
###  * If abstract class contains only abstract methods then it is an "interface"
###  * "Abstract class" can contain both abstract methods and concrete methods
#################################################################################


"""Facade Pattern: -> """
####  FACADE CLASS -> Restaurant
class Restaurant:
    """Facade Class: This Provides an easy interface to Client to access different systems like Cutter, Boiler,
    Refrigirator etc. """
    def __init__(self):
        self._cutter = Cutter ()
        self._boiler = Boiler ()
        self._refrigirator = Refrigirator ()

    def prepareDish(self):
        self._cutter.cutVegetables()
        self._boiler.boilVegetables()
        self._refrigirator.inventoryVegetables()

##### SYSTEM CLASSES ->  CUTTER, BOILER, REFRIGIRATOR
class Cutter:
    """System Class: Cutter
    Desc: Provides feature of Cutting Vegetables"""
    def cutVegetables(self):
        print("Cutting Vegetables")

class Boiler:
    """System Class: Boiler
    Desc: Provides feature of Boiling Vegetables"""
    def boilVegetables(self):
        print("Boiling Vegetables")

class Refrigirator:
    """System Class: Refrigirator
    Desc: Provides feature of Inventory Vegetables"""
    def inventoryVegetables(self):
        print("Inventory Vegetables")


#### CLIENT CLASS

class Client(Restaurant):
    def __init__(self):
        print("Client Initialized")
        self._restaurant = Restaurant()
        self._restaurant.prepareDish()


print("Initiating Client ")
Client()