"""   FLYWEIGHT DESIGN PATTERN - STRUCTURAL DESIGN  """

###  NOT COMPLETED ###
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods

# import weakref
from typing import Dict


########################################
####  FLYWEIGHT FACTORY [CarModel] #####
########################################
class CarModel :
    """ This is a Flyweight Factory class"""
    # _models = weakref.WeakValueDictionary()
    _models: Dict[str, str] = {"model_name" : "model"}

    def __new__(cls, model_name):
        model = cls._models.get (model_name)
        if not model:
            model = super ().__new__ (cls)
            cls._models[model_name] = model
        else:
            print ("Model Already Existed")
        return model

    def __init__(
            self,
            model_name,
            air=False,
            tilt=False,
            cruise_control=False,
            power_locks=False,
            alloy_wheels=False,
            usb_charger=False,
    ):
        if not hasattr (self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted = True

    def check_serial(self, serial_number):
        print (
            "Sorry, we are unable to check "
            "the serial number {0} on the {1} "
            "at this time".format (serial_number, self.model_name)
        )

    @property
    def models(self) :
        return self._models

    @property.getter
    def __getitem__(self, item):
        return self[item]


###########################
####  FLYWEIGHT [Car] #####
###########################
class Car:
    """ This is a Flyweight Object Class """
    def __init__(self, model, color: str, serial: int):
        if CarModel.models[model] == model:
            self.model = model
            self.color = color
            self.serial = serial

    def check_serial(self):
        return self.model.check_serial (self.serial)


Toyota = CarModel ("Toyota_Camry")
Toyota1 = CarModel ("Toyota_Camry_LE")

print(Toyota._models)
print(Toyota1._models)

Toyota = Car("Toyota", "Red", 124)
Toyota.check_serial()
##### Need to check relation between Car and CarModel ######


# print(Toyota.check_serial("124"))
#
# Car("Toyota Camry LE", "Silver", "123")
# print(Toyota.check_serial("123"))
#
# Car("Toyota Camry", "Red", "111")
# print(Toyota.check_serial("111"))
