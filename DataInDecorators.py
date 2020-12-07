# collectstats is much like running_average, but lets # you access the data dictionary directly, instead
# of printing it out.
def collectstats(func):
    data = {"total" : 0, "count" : 0}
    print(type(data))
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        # nonlocal data
        data["total"] += val
        data["count"] += 1
        return func(*args, **kwargs)
    wrapper.data = data
    return wrapper

@collectstats
def foo(x):
    return x + 2

@collectstats
def bar(x):
    return x * 2
print(foo.__closure__)
print(foo.__code__.co_freevars)
print(foo.data)
print(foo(1))
print(foo.data)
print(foo(3))
print(foo.data)
print(bar.__closure__)
print(bar.__code__.co_freevars)
print(bar.data)
print(bar(2))
print(bar.data)