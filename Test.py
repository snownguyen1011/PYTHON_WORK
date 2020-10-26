#############   Testing list Conversions   #########
# number1 = ['1','2','3']
# number2 = ['4','5','6']
# number3 = ['1','2','3']
# print((number1,number2))
# print([number1,number2])
#
#    # print({number1:number2})  # TypeError: unhashable type: 'list'
#####################################################


# fruits = ["Apple", "Pear", "Peach", "Banana"]
# list = ['A','B','C','D']
# dictionary = dict(zip(list,fruits))
# print(dictionary)
#
# fruit_dictionary = {1:'Plum', 2:'Guava'}
#
#
# print(fruit_dictionary.keys())
# print(fruit_dictionary.values())
# print(fruit_dictionary.items())
#
# print(fruit_dictionary.__getitem__(1))
# print(fruit_dictionary.get(1))
#
# print(dictionary.pop('D'))
# print(dictionary)
# print(dictionary.popitem())
# print(dictionary)
#
# fruit_dictionary.update(dictionary)
# print(fruit_dictionary)
# ######   DICT COPY
# original = {1:'one', 2:'two'}
# new = original
# new.clear()
# print('Orignal: ', original)
# print('New: ', new)
#
# original = {1:'one', 2:'two'}
# new = original.copy()
# new.clear()
# print('Orignal: ', original)
# print('New: ', new)
#
# fruits1 = ["Apple", "Pear", "Peach", "Banana"]
# ####  Below 2 methods results same
#     # fruit_dict = { fruit : "In stock" for fruit in fruits1 }
# fruit_dict = dict.fromkeys(fruits1, "In stock")
#
# print(fruit_dict)
#
# # Python3 code to demonstrate working of
# # Convert Tuple Matrix to Tuple List
# # Using list comprehension + zip()
# from itertools import chain
# # initializing list
# test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
#
# # printing original list
# print ("The original list is : " + str (test_list))
#
# # # flattening
# temp = [ele for sub in test_list for ele in sub]
#
# # joining to form column pairs
# res = [zip(*temp)]
#
# print("Printing res", res)
#
# # joining to form column pairs
# res1 = [zip(*chain.from_iterable(test_list))]
#
# # printing result
# print ("The converted tuple list : ", dict(res1))
# print("Flattened  list : ", temp)
# print ("The converted tuple list : ", dict(res))
#
#
#
# print ("""Generates the characters from `a` to `z`, inclusive.""")
# def character_range(char1, char2):
#     print(ord(char1))
#     print (ord (char2))
#     for char in range(ord(char1), ord(char2)+1):
#         yield (char)
#
# for letter in character_range('a', 'z'):
#     print( chr(letter), end=", " )


######## New Program
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dragonLoot_dict = {i: dragonLoot.count(i) for i in dragonLoot}

print(dragonLoot_dict)











# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# print(inv.values())
# print(inv.keys())
# print(inv.items())
# print(type(inv.items()))


# def addToInventory(inventory, addedItems):  # your code goes here
#
#
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)