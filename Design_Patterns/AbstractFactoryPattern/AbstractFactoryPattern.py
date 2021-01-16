from abc import ABCMeta, abstractmethod
from FactoryPattern import ChairFactory


class IFurnitureFactory(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_furniture(furnituretype):
        """This is a static furniture factory interface method """

class FurnitureFactory(IFurnitureFactory):

    # @staticmethod
    # @abstractmethod
    def get_furniture(furnituretype):
        try:
            if furnituretype in ["BigChair","MediumChair","SmallChair"]:
                return ChairFactory.get_chair(furnituretype)
            raise AssertionError("Can't find Chair Type")
        except AssertionError as _e:
            print(_e)
        return None


Furniture = FurnitureFactory.get_furniture("SmallChair")
print(Furniture.get_dimensions())

