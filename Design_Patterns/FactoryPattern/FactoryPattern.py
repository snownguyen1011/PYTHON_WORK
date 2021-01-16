from abc import ABCMeta, abstractstaticmethod

class Ichair(metaclass=ABCMeta):
    @abstractstaticmethod
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

CHAIR = ChairFactory.get_chair("BigChair")
print(CHAIR.get_dimensions())

CHAIR1 = ChairFactory.get_chair("MediumChair")
print(CHAIR1.get_dimensions())

CHAIR2 = ChairFactory.get_chair("SmallChair")
print(CHAIR2.get_dimensions())

CHAIR3 = ChairFactory.get_chair("Chair")
print(CHAIR3.get_dimensions())