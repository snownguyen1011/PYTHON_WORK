def outer_func():
    x= 'hello'    ## Level 1
    print ("Outer func x is:", x)
    def inner1():
        nonlocal x
        x = "world"
        print("Inner1 x is:", x)   ## Level 2
        def inner2():
            nonlocal x
            x = "Oops"
            print("Inner2 x is:", x)  ## Level 3
            return x
        inner2()
        return x
    inner1()
    return x

print(outer_func())
