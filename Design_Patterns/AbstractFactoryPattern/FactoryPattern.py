from abc import ABCMeta, abstractmethod

class Ichair(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        """This is a chair interface"""

class BigChair(Ichair):

    def __init__(self):
        self.height = 80
        self.width = 80
        self. depth =80

    def get_dimensions(self):
        return {"height": self.height, "width":self.width, "depth": self.depth}

class MediumChair(Ichair):

    def __init__(self):
        self.height = 50
        self.width = 50
        self. depth =50

    def get_dimensions(self):
        return {"height": self.height, "width":self.width, "depth": self.depth}

class SmallChair(Ichair):

    def __init__(self):
        self.height = 50
        self.width = 50
        self. depth =50

    def get_dimensions(self):
        return {"height": self.height, "width":self.width, "depth": self.depth}

class ChairFactory():

    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype == "BigChair":
                return BigChair()
            elif chairtype == "MediumChair":
                return MediumChair()
            elif chairtype == "SmallChair":
                return SmallChair()
            else:
                raise AssertionError("Chair Not Found !!!")
        except AssertionError as _e:
            print(_e)

