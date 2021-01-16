from Design_Patterns.Proxy_Pattern.proxy_pattern import icomponent

from datetime import datetime


class Component (icomponent.IComponent) :
    """ Component Class implements IComponent """

    def __init__(self) :
        self.name = self.__class__.__name__

    def method(self) :
        # print (self.name, " Initialized")
        return f'{self.name} initialized at {datetime.now ()}'


Object1 = Component()
print("Accessing Component Directly",Object1.method())
