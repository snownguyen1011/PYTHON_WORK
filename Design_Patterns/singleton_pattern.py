""" Single Design Pattern """

class OneOnly: # pylint: disable=too-few-public-methods
    """This is a Singleton Pattern Class"""
    _singleton = None

    def __new__(cls, *args, **kwargs):
        """ Creating new instance of Singleton class OneOnly """
        if not cls._singleton:
            cls._singleton = super (OneOnly, cls).__new__ (cls, *args, **kwargs)
        return cls._singleton


instance1 = OneOnly ()
instance2 = OneOnly ()

print (OneOnly.__dict__)
print (OneOnly.__instancecheck__(instance2))

print (instance2 == instance1)
print (instance2 is instance1)

print (id (instance2), id (instance1))
