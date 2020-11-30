###############################################
# http://zetcode.com/python/python-closures/
# Python closures
# A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution. Three characteristics of a Python closure are:
#
# it is a nested function
# it has access to a free variable in outer scope
# it is returned from the enclosing function
# A free variable is a variable that is not bound in the local scope. In order for closures to work with immutable variables such as numbers and strings, we have to use the nonlocal keyword.
#
# Python closures help avoiding the usage of global values and provide some form of data hiding. They are used in Python decorators.
###############################################
####   CLOSURE EXAMPLE 1 : START   ####
def make_printer(msg):
    msg1 = "hi there"
    def printer():
        print(msg)
        print (msg1)
    return printer

myprinter = make_printer("Hello there")
myprinter()
####   CLOSURE EXAMPLE 1 : END   ####


def outer():
    x = 'python'
    y = [1, 2, 3]
    z = 'python'
    print (hex (id (y)))
    def inner():
        w = y
        # y = [1, 2, 3]
        print (x)
        print (y)
        print (z)
        print(hex(id(w)))
        print (hex (id (y)))
        return y
    return inner

fn = outer ()
print (fn)
print (fn())
print (fn.__call__)
# print (fn.__call__())
print (fn.__closure__)
# print(fn.__code__.co_freevars)

# print(fn.__code__.co_cellvars)
# print(fn.__code__.co_varnames)
# print(fn.__code__.co_consts)


