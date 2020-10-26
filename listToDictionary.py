#####  COUNTING NUMBER OF OCCURANCES OF DICTIONARY VALUES #####

#######   METHOD 1 - START  #########
print("<--- COUNTING NUMBER OF OCCURANCES OF DICTIONARY VALUES - METHOD 1 --->")
dragonLoot1 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dragonLoot_dict = {i: dragonLoot1.count(i) for i in dragonLoot1}
print(dragonLoot_dict)
print(type(dragonLoot_dict))
# dragon = {'gold coin': 7, 'dagger': 9}
#######   METHOD 1 - END  ###########


#######   METHOD 2 - START  #########
print("<--- COUNTING NUMBER OF OCCURANCES OF DICTIONARY VALUES - METHOD 2 --->")
from collections import Counter
dragonLoot2 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print("USING COUNTER: ", Counter(dragonLoot2))
print(type(Counter(dragonLoot2)))
#######   METHOD 2 - END  ###########


#######   METHOD 3 - START  #########
print("<--- COUNTING NUMBER OF OCCURANCES OF DICTIONARY VALUES - METHOD 3 --->")
dragonLoot3 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
temp=set(dragonLoot3)
result={}
for i in temp:
    result[i]=dragonLoot3.count(i)
print(result)
print(type(result))
#######   METHOD 3 - END  ###########


dragonLoot3 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



