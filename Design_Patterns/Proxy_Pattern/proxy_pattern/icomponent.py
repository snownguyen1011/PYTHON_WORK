from abc import ABCMeta, abstractmethod


class IComponent (metaclass=ABCMeta) :
    """ Interface Component"""

    @staticmethod
    @abstractmethod
    def method() :
        """ This method need to be implemented on Component & Proxy Component """
        pass
