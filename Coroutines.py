def tally():
    score = 0
    while True:
        increment = yield score
        score += increment


white_sox = tally()
blue_jays = tally()

print(next(white_sox))
print(next(blue_jays))
print(white_sox.send(3))
print(blue_jays.send(2))

# Unlike with generators, this yield function looks like it's supposed to return a value and assign it to a variable.
# 'In fact, this is exactly what's happening. The coroutine is still paused at the yield statement and waiting to be
# activated again by another call to next().


# The thing that is really confusing for many people is the order in which this happens:
# 1. yield occurs and the generator pauses
# 2. send() occurs from outside the function and the generator wakes up
# 3. The value sent in is assigned to the left side of the yield statement
# 4. The generator continues processing until it encounters another yield statement
#
# So, in this particular example, after we construct the coroutine and advance it to the yield statement with a
# single call to next(), each successive call to send() passes a value into the coroutine. We add this value to its score.
# Then we go back to the top of the while loop, and keep processing until we hit the yield statement.
# The yield statement returns a value, which becomes the return value of our most recent call to send.
# Don't miss that: like next(), the send() method does not just submit a value to the generator, it also returns
# the value from the upcoming yield statement. This is how we define the difference between a generator and
# a coroutine: a generator only produces values, while a coroutine can also consume them.