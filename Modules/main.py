import module1
var = module1.call()

print("Type of var", type(var))
print("Free vars --> ", var.__code__.co_freevars)
print("Calling a function var:")
var()
print(var.__qualname__)
print(var.__closure__)
print("Inner Argument x value is:", var.x,"\n")


var1 = module1.closure_call()
print(type(var1))
var1()
print("Free variables: ", var1.__code__.co_freevars)
print(var1.__closure__)
print(var1.__closure__[0].cell_contents)


######################################################
import sys
print(sys)

import collections
print(collections)

import importlib
print(importlib)

print('math' in sys.modules)
print('math' in globals())

importlib.import_module('math')
print('math' in sys.modules)
print('math' in globals())

### BELOW THREE CODE LINES ARE EQUIVALENT ###
math = sys.modules['math']
# import math
# math = importlib.import_module('math')

print('math' in globals())

math2 = importlib.import_module('math')
print(math2.sqrt(4))


#####  FINDERS
#####  LOADERS
#####  FINDERS + LOADERS == IMPORTER
print(math.__spec__)
print("All importers:", sys.meta_path)

print('fractions' in globals())
print(importlib.__import__('fractions',globals=sys))
print('fractions' in globals())
import os
print("Printing ENV", os.environ['PATH'])
print("Current working dir:", os.getcwd())