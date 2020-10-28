# Add a single item 'yellow' to a set
S = {'red', 'green', 'blue'}
S.add('yellow')
print(S)
# {'green', 'blue', 'red', 'yellow'}

###  INSERTING EXISTED VALUE
S = {'red', 'green', 'blue'}
S.add('red')
print(S)


# A tuple can be added in a set
S = {'red', 'green', 'blue'}
S.add((1, 2))
print(S)
# Prints {'blue', (1, 2), 'green', 'red'}

# But list can’t be a set item
S = {'red', 'green', 'blue'}
# S.add([1, 2])
# Triggers TypeError: unhashable type: 'list'