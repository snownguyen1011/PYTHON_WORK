
########################################################################
####### A generator function looks a lot like a regular function.
####### But instead of saying return, it uses a new and different keyword: yield.
########################################################################


# fill in this function
def fib():  # fib() is a generator function
    a=1
    b=1
    while a>=1:
        # a, b = b, a + b
        # yield a,b
        yield a             ##  Eachyield statement simultaneously defines an exit point, and a re-entry point.
        a, b = b, a + b     ## Re-entry point of Coroutine
    # pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

genobj = fib()
print(type(fib()))
print(type(genobj))


def gen_nums():
        n=0
        while n < 4:
            yield n
        n += 1

sequence = gen_nums()

print(type(gen_nums()))
print(type(sequence))

print(gen_nums())
print(sequence)


def gensquares(num):
    for n in range(num):
        yield n ** 2
    print(num**2)

squares = gensquares(5)
print("Type of gensquares() is:", type(gensquares(5)))
print("Type of squares is:", type(squares))
for n in squares:
    print(n)

print(squares.)