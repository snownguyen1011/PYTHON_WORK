# The Command Design Pattern in Python
# The command pattern is a behavioural design pattern,
# in which an abstraction exists between an object that invokes a command, and the object that performs it.
#
# The components if the Command Design Pattern are,
# The Receiver - The Object that will receive and execute the command
# The Invoker - Which will send the command to the receiver
# The Command Object - Itself, which implements an execute, or action method,
# and contains all required information or module which is aware of
# the Receiver, Invoker and Commands
#
# Eg, a button, will call the Invoker, which will call a pre registered Commands execute method,
# which will perform the action on the Receiver.
#
# Notes:
# The receiver object should manages it's own state, not the command object
# There can be one or more invokers which can execute the command at a later date.

from abc import ABCMeta, abstractmethod
import time

# Command Interface
class ICommand(metaclass=ABCMeta):
    """A Static Interface Method"""
    @staticmethod
    @abstractmethod
    def execute():
        pass

# Command1
class SwitchOnCommand(ICommand):
    def __init__(self, light):
        self._light =light
    def execute(self):
        self._light.Switch_On()

# Command2
class SwitchOffCommand(ICommand):
    def __init__(self, light):
        self._light =light
    def execute(self):
        self._light.Switch_Off()

# Receiver
class Light:
    def Switch_On(self):
        print("Light is ON")

    def Switch_Off(self):
        print("Light is OFF")


# Invoker
class Switch:
    """Invoker class"""
    def __init__(self):
        self._commands = {}
        self._history = []

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self,command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append({time.time():command_name})
        else:
            raise KeyError(command_name," is not available on SWITCH :(")
            # print(self._commands[command_name]," : Command Not Found")

    @property
    def history(self):
        return self._history

# Client
if __name__ == "__main__":

    # Receiver
    LIGHT = Light()     ## CREATED LIGHT OBJECT

    # Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)      ## CREATED SWITCH_ON OBJECT
    SWITCH_OFF = SwitchOffCommand(LIGHT)    ## CREATED SWITCH_OFF OBJECT

    # Invoker
    SWITCH = Switch()   ## CREATED SWITCH OBJECT   ... THERE IS AN INTERFACE FOR SWITCH WHERE SWITCH COMMANDS WILL BE IMPLEMENTED

    # Register commands in the invoker
    SWITCH.register(command_name="ON", command=SWITCH_ON)
    SWITCH.register(command_name="OFF", command=SWITCH_OFF)

    SWITCH.execute(command_name="ON")
    SWITCH.execute (command_name="OFF")
    SWITCH.execute (command_name="OFF")
    # SWITCH.execute (command_name="OFFF")    #### UNAVAILABLE SWITCH COMMAND (ERROR INPUT)


    print(SWITCH.history)

