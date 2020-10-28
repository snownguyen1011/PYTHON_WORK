# Create a dictionary and set default value 'Developer' for all keys
D = dict.fromkeys(['Bob', 'Sam'], 'Developer')
print(D)
# Prints {'Bob': 'Developer', 'Sam': 'Developer'}

D = dict.fromkeys(['Bob', 'Sam'])
print(D)
# Prints {'Bob': None, 'Sam': None}


D1 = {'name': 'Bob', 'age': 25}
D2 = {'job': 'Dev', 'age': 30}
D1.update(D2)
print(D1)
# Prints {'job': 'Dev', 'age': 30, 'name': 'Bob'}


D3 = {'name': 'Bob', 'age': 25}
D4 = {'job': 'Dev', 'age': 30}
D4.update(D3)
print(D4)
# Prints {'job': 'Dev', 'age': 25, 'name': 'Bob'}