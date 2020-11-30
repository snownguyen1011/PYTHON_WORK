######   DECORATOR EXAMPLE 1 DECLARATION #####
def printlog(func):
    def wrapper(*args, **kwargs):
        print('CALLING: {}'.format(func.__name__))
        print(type(args))
        print(args)
        if(type(args[0])== str):
            print("args is a String")
        elif(type(args[0]) == int):
            print("args is an integer")
        return func(*args,**kwargs)
    return wrapper
######   TEST BLOCK 1 - STARTS #######
@printlog
def add(x):
    print(x)
    # return x
print("*** Start: Calling add with a string")
add("Hello")
print("*** End: Calling add with a string\n")
print("*** Start: Calling add with an int")
add(3)
print("*** End: Calling add with an int\n")
######   TEST BLOCK 1 - ENDS #########
######   END:  DECORATOR EXAMPLE 1 DECLARATION #####


######   START:  DECORATOR EXAMPLE 2 DECLARATION #####
def printlog1(func):
    def wrapper(a,b):
        print('CALLING: {}'.format(func.__name__))
        print(type(a),type(b))
        a,b = a*2, b*2
        print(a,b)
        return func(a,b)
    return wrapper
######   TEST BLOCK 1 - STARTS #######
@printlog1
def add(x,y):
    print(x+y)
    # return x+y

print("*** Start: Calling add with an int")
add(2,2)
print("*** End: Calling add with an int\n")
print("*** Start: Calling add with a string")
add("2","2")
print("*** End: Calling add with a string\n")
######   TEST BLOCK  - ENDS #########
######   END:  DECORATOR EXAMPLE 2 DECLARATION #####

from functools import wraps
from datetime import date
from datetime import datetime

def order_log(func):
    import logging
    import json
    logging.basicConfig(filename='{}.log'.format(func.__name__),level=logging.INFO)

    @wraps(wrapped=func)
    def order_logger(*args, **kwargs):
        # print(args)
        print(kwargs)
        # print("Type of Arguments Object: ", type(kwargs))    ####  Dictionary
        # print ("Dictionary length:", len(kwargs))
        # print ("Unit Cost:",kwargs['cost'])
        kwargs['unit_cost'] = kwargs['cost']
        # kwargs['date'] = str(datetime.now ())
        print(kwargs)
        ### Determining Total Cost ###
        if(kwargs['coupon'] == "50OFF"):
            kwargs['cost'] = kwargs['quantity'] * kwargs['cost'] * 0.5
        else:
            kwargs['cost'] = kwargs['quantity'] * kwargs['cost']
        print("Total Cost:", kwargs['cost'])
        logging.info(json.dumps(kwargs, indent=len(kwargs)))
        return func(*args, **kwargs)
    return order_logger


def time_log(func):
    @wraps (wrapped=func)
    def time_logger(*args, **kwargs):
        kwargs['date'] = str(datetime.now ())
        return func(*args, **kwargs)
    return time_logger


@time_log
@order_log
def order(product_id, product_name, quantity, cost, user, unit_cost, date, coupon):
    print("Product ID:", product_id)
    print("Product Name:", product_name)
    print ("Quantity:", quantity)
    print("Cost:", cost)
    print("Unit Cost:", unit_cost)
    print("Customer Name:", user)

call1 = order(product_id=100, product_name="Test_Product", quantity= 2, cost=10, user="Ravi", coupon="50OFF")

# call2 = order(product_id=100, product_name="Test_Product", quantity= 2, cost=10, user="Ravi", coupon="")