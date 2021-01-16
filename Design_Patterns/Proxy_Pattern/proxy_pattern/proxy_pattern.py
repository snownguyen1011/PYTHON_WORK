"""Proxy Pattern Example
There are 3 types 1. Remote 2. Virtual 3. Protected - Need to Explore more """

from datetime import datetime
from Design_Patterns.Proxy_Pattern.proxy_pattern import component, icomponent

##### Moved out in this Package #####
# class IComponent(metaclass=ABCMeta):
#     """ Interface Component"""
#
#     @staticmethod
#     @abstractmethod
#     def method():
#         """ This method need to be implemented on Component & Proxy Component """
#         pass

# class Component(IComponent):
#     """ Component Class implements IComponent """
#
#     def __init__(self):
#         self.name = self.__class__.__name__
#
#     def method(self):
#         # print (self.name, " Initialized")
#         return f'{self.name} initialized at {datetime.now()}'
##### Moved out in this Package #####

class ProxyComponent (icomponent.IComponent) :
    """ Proxy Component Class which implements IComponent """

    def __init__(self) :
        self.component = component.Component ()

    def method(self) :
        print ("This is Proxy Component Area -> Before calling Original Component")
        print ("{} method was proxied at {}".format (self.component.name, datetime.now ()))
        print ("This is Proxy Component Area -> After calling Original Component")
        return self.component.method ()



Object2 = ProxyComponent ()
print (Object2.method ())
print (Object2.component.__dict__)
