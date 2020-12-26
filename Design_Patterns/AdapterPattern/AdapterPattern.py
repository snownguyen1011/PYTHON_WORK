"""
Adapter Design Pattern
"""
from abc import ABCMeta, abstractmethod

class InterfaceA(metaclass=ABCMeta):
    """Interface for Class A"""
    @staticmethod
    @abstractmethod
    def method_a(self):
        """An abstract Method A"""

class InterfaceB(metaclass=ABCMeta):
    """Interface for Class B"""
    @staticmethod
    @abstractmethod
    def method_b(self):
        """An abstract Method B"""

class A(InterfaceA):
    def __init__(self):
        print("Class A initialized")
        self.A = "Comes from initialized Class A method_A()"

    def method_a(self):
        print(self.A)


class B(InterfaceB):
    def __init__(self):
        print ("Class B initialized")
        self.B = "Comes from initialized Class B method_b()"

    def method_b(self):
        print (self.B)


###   Class A  needs to talk with Class B.
###   Since both Class A and Class B are has own interfaces can't call each other.
###   Here we need to implement An adapter pattern.

class AdapterB(InterfaceA):
    def __init__(self):
        print("AdapterB initialized")
        self.AdapterB = B()

    def method_a(self):
        """We are calling method_a from Class B using an adapter """
        return self.AdapterB.method_b()

# var = AdapterB()
# # print(var.__dict__)
# var.method_a()
print("Calling method_a() from AdapterB")
AdapterB().method_a()