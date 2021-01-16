#################################################################################
############ LEARNING PURPOSE BELOW INFO ########################################
###  * If abstract class contains only abstract methods then it is an "interface"
###  * "Abstract class" can contain both abstract methods and concrete methods

# A facade is, in many ways, like an adapter. The primary difference is that
# a facade tries to abstract a simpler interface out of a complex one,
# while an adapter only tries to map one existing interface to another.
#################################################################################

from abc import ABCMeta, abstractmethod
"""Facade Pattern: -> """
#####   ADDING INTERFACES TO CUTTER, BOILER, REFRIGIRATOR
class CutterInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def cutVegetables(self):
        """It's a Static and Abstract"""

class BoilerInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def boilVegetables(self):
        """It's a Static and Abstract"""

class RefrigiratorInterface(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def inventoryVegetables(self):
        """It's a Static and Abstract"""


####  FACADE CLASS -> Restaurant
class Restaurant:
    """Facade Class: This Provides an easy interface to Client to access different systems like Cutter, Boiler,
    Refrigirator etc. """
    def prepareDish(self):
        self._cutter = Cutter()
        self._cutter.cutVegetables()

        self._boiler = Boiler()
        self._boiler.boilVegetables()

        self._refrigirator = Refrigirator()
        self._refrigirator.inventoryVegetables()

##### SYSTEM CLASSES ->  CUTTER, BOILER, REFRIGIRATOR
class Cutter(CutterInterface):
    """System Class: Cutter
    Desc: Provides feature of Cutting Vegetables"""
    def cutVegetables(self):
        print("Cutting Vegetables")

class Boiler(BoilerInterface):
    """System Class: Boiler
    Desc: Provides feature of Boiling Vegetables"""
    def boilVegetables(self):
        print("Boiling Vegetables")

class Refrigirator(RefrigiratorInterface):
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