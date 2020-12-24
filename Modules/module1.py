#### START:  This is a function ######

def call():
    def inner():
        x = 100
        print ("Added a variable x as 100")
        inner.x = x

    return inner


#### END:  This is a function #########

#### START:  This is a function ######

# def call(msg):
#     x = 100
#     def inner():
#         print("Outer variable:",msg)
#         print("module1 called", x)
#     return inner

#### END:  This is a function #########

##### START:  This is a closure ######

def closure_call():
    x = [1, 2, 3]

    def inner():
        print ("ID of x:", id (x))
        print ("Type of x is:", type (x))
        x.append (4)
        print ("X: ", x)
    return inner
