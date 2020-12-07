class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    @fullname.setter
    def fullname(self, value):
            self.firstname, self.lastname = value.split(" ", 1)

    @fullname.deleter
    def fullname(self):
        self.firstname = ""
        self.lastname = ""

print("*** Person Class instance initiated using var: A ***")
A = Person("Ravi", "Raja")
print("What is A:", A)

print(A.firstname)
print(A.lastname)
print(A.fullname)

print("Updating first & lastname")
A.firstname = "Ravi Raja"
A.lastname = "Koineni"

print(A.fullname)
A.fullname = "Ravi Raja K"
print(A.fullname)
del A.fullname
print("Called deleter fullname:", A.fullname)
print("=====END=======")

# In Python, prefixing a member variable by a single underscore signals the variable is non-public,
# i.e. it should only be accessed internally, inside methods of that class, or its subclasses.[1]
# What this pattern says is "you can access this variable, but not change it".

class Ticket:
    def __init__(self, price):    #### Default Constructor
        if price < 0:
            raise ValueError("Use Valid Positive Value to Price", price)
        self.price = price

    @property
    def price(self):
        return self._price    ### prefixing a member variable by a single underscore signals the variable is non-public

    @price.setter
    def price(self, price):
        # Only allow positive prices.
        print("new_price is", price)
        if price < 0:
            raise ValueError("Use Valid Positive Value to Price", price)
        self._price = price

    def update_price(self, new_price):
        # Only allow positive prices.
        print("Price Changed: -> ", new_price)
        if new_price < 0:
            raise ValueError("Use Valid Positive Value to Price", new_price)
        self._price = new_price


t = Ticket(30)
print("Property of Ticket Class", t.price)
print("Instance attribute of t", t._price)

t1 = Ticket(24)
print("t1 price:",t1.price)

print("========")
t1.update_price(26)
print("New Price:", t1.price)

print(callable(t1.price))
print(callable(t1.update_price))