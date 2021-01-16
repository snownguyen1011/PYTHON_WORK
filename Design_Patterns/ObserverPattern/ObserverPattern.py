class ObserverInterface:
    def __call__(self, *args, **kwargs):
        """Print Product and Quantity"""
        pass

# TODO: Implement Interface for Observers
class CoreInventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append (observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers ()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver(ObserverInterface):
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print (self.inventory.product)
        print (self.inventory.quantity)


i = CoreInventory()     ### CORE CLASS
c1 = ConsoleObserver(i)  ### OBSERVER1
c2 = ConsoleObserver(i)  ### OBSERVER2

i.attach(c1)
i.attach(c2)

i.product = "Fountain"
i.quantity = 1

