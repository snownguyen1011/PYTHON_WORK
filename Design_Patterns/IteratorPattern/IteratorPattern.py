from abc import ABCMeta, abstractmethod

class IIterator(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def has_next():
        """Returns Boolean value whether at the end of collection or not"""

    @staticmethod
    @abstractmethod
    def next():
        """Returns Next object from collection / Iterable"""

class Iterable(IIterator):

    def __init__(self):
        self.index =0
        self.max = 8

    def next(self):
        if self.index <= self.max:
            x = self.index
            self.index += 1
            return x
        else:
            raise Exception("AtEndOfIteratorException", "At End")

    def has_next(self):
        return self.index <= self.max


ITERABLE = Iterable()

while ITERABLE.has_next():
    print(ITERABLE.next())
