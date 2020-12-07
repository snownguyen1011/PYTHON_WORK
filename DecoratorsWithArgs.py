def add(increment, dict = {"cnt": 0, "x": 0}):
    # print("increment value", increment)

    def decorator(func):
        # print("dictionary outside wrapper", dict.values())
        count = 0
        def wrapper(*args, **kwargs):
            # dict = {"cnt": 0, "x": 0}
            # count = 0
            nonlocal count
            print (args)
            count += 1
            dict["cnt"] += 1
            dict["x"] += int(args[0])
            print ("Count inside wrapper:", count)
            print ("dictionary inside wrapper", dict.values ())
            print ("increment value", increment)
            return func(*args, **kwargs) + increment
        return wrapper
        # wrapper.count = count
        # wrapper.dict = dict
    return decorator

@add(3)
def addition(x):
    print("Before applying wrapper:", x)
    x+=1
    print("After applying wrapper:", x)
    return x

# print(add(2)(addition(2)))
result = addition(2)
print(result)

result = addition(4)
print(result)


# print(add(2)(addition)(2))
# addition = add(2)(addition)
# print(addition.__code__)