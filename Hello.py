# # import sys
# names = []
# sys.getrefcount(names)
# print(type(names))
# testvar = sys.getrefcount(names)
# print(testvar)

##############################################################################
# EXCERCISE 1 -  INITIALIZATION VARS AND DISPLAY TYPE & VALUES

# Create a variable, pi, that points to an approximation for the value of pi. Create a variable,
# r, for the radius of a circle that has a value of 10.
# Calculate the area of the circle (pi times the radius squared).
# You can do multiplication with * and you can square numbers using **. For example, 3**2 is 9.

# Calculating square is a basic operation in mathematics;
# here we are calculating the square of a given number by using 3 methods.
# By multiplying numbers two times: (number*number)
# By using Exponent Operator (**): (number**2)
# By using math.pow() method: (math.pow(number,2)
############ START PROGRAM ##########
# import math
#
# pi = 3.14
# radius = int(10)
#         # result = pi * (radius**2)
#         # result = pi * (radius*radius)
# result = pi * (math.pow(radius,2))
# print(type(pi))
# print(type(result))
# print(type(radius))
# print(id(radius))
# print(result)
# print("Value of PI", pi)
########### END PROGRAM #############
##############################################################################
# EXCERCISE 2
# Create a variable, b, that points to the base of a rectangle with a value of 10.
# Create a variable, h, that points to the height of a rectangle with a value of 2.
# Calculate the perimeter. Change the base to 6 and calculate the perimeter again.

############ START PROGRAM ##########
# b = int(10)
# h = int(2)
# perimeter = 2*(b*h)
# print("Perimeter is", perimeter)
# b= int(6)
# perimeter = 2*(b*h)
# print("Perimeter is (with base changed to 6)", perimeter)

########### END PROGRAM #############
##############################################################################
############ START PROGRAM ##########
# name = "Matt"
# first = name
# age = 1000
# print(id(age))
# age = age + 1
# print(id(age))# ID will change
# names = []
# print(id(names))
# names.append("Fred")
# print(id(names))# ID won't change
########### END PROGRAM #############
##############################################################################
# EXCERCISE 3
# Create a variable that points to a floating point number.
# Examine the id, type, and value of that number. Update the variable by adding 20 to it.
# Re-examine the id, type, and value. Did the id change? Did the value change?
############ START PROGRAM ##########
# var = 2.3
# print("ID of var", id(var))
# print("type of var", type(var))
# print("Value of var", var)
# var = 20
# print("ID of var", id(var))
# print("type of var", type(var))
# print("Value of var", var)

## ID & VALUE WILL Change
########### END PROGRAM #############
##############################################################################
# EXCERCISE 4
# Create a variable pointing to an empty list. Examine the id, type, and value of the list.
# Append the number 300 to the list.
# Re-examine the id, type, and value. Did the id change? Did the value change?
############ START PROGRAM ##########
# A = []
# print("ID of A", id(A))
# print("type of A", type(A))
# print("Value of A", A)
#
# A.append(300)
# print("After appending 300 to A List")
# print("ID of A", id(A))
# print("type of A", type(A))
# print("Value of A", A)
## ID DIDN'T CHANGE
## VALUE CHANGED
########### END PROGRAM #############
##############################################################################
# EXCERCISE 5
# You slept for 6.2, 7, 8, 5, 6.5, 7.1, and 8.5 hours this week.
# Calculate the average number of hours slept.?
############ START PROGRAM ##########
# A = [6.2, 7, 8, 5, 6.5, 7.1, 8.5 ]
# avg = sum(A)/len(A)
# print(avg)
# total = len(A)
# print(len(A))
# sum = 0
# for x in A:
#     sum=sum+x
# print(sum)
# avg = sum/total
# print("Average is:", avg)

##### USING METHOD #######
# # Python program to get average of a list
# def Average(lst):
#     return sum(lst) / len(lst)
#
# # Driver Code
# lst = [15, 9, 55, 41, 35, 20, 62, 49]
# average = Average(lst)
#
# # Printing average of the list
# print("Average of the list =", round(average, 2))
##########################
########### END PROGRAM #############
##############################################################################
# EXCERCISE 6
# ?Is 297 divisible by 3??
############ START PROGRAM ##########
# A = 297/3
# print(A)
#
# if 297 % 3  == 0:
#     print("297 is divisible by 3")
########### END PROGRAM #############
##############################################################################
# EXCERCISE 7
# Create a variable, name, pointing to your name.
# Create another variable, age, holding an integer value for your age.
# Print out a string formatted with both values.
# If your name was Fred and age was 23 it would print:
# Fred is 23
############ START PROGRAM ##########
# name = 'ravi raja'
# age = int(33)
# # print(name ,"is", age)
# print(f'{name} is {age}') # f-String
########### END PROGRAM #############
# ##################
# F-Strings
# Python 3.6 introduced a new type of string, called f-string. If you precede a string with an f, it will allow you to include code inside of the placeholders. Here is a basic example:
# >>> name = 'matt'
# >>> f'My name is {name}'
# My name is matt
# ##################
##############################################################################
# EXCERCISE 8
# Create a variable, paragraph, that has the following content:
# Python is a great language!", said Fred. "I don't ever remember having this much fun before.
############ START PROGRAM ##########
# paragraph = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before.?'''
# print(paragraph)
# import pdb; pdb.set_trace()
########### END PROGRAM #############
##############################################################################
# EXCERCISE 9
#     :[[fill]align][sign][#][0][width][grouping_option][.precision][type]
# Field	Meaning
# fill	Character used to fill in align (default is space)
# align	Alight output < (left align), > (right align), ^ (center align), or = (put padding after sign)
# sign	For numbers + (show sign on both positive and negative numbers, - (default, only on negative), or space (leading space for positive, sign on negative)
# #	Prefix integers. 0b (binary), 0o (octal), or 0x (hex)
# 0	Enable zero padding
# width	Minimum field width
# grouping_option	Number separator , (use comma for thousands separator), _ (Use underscore for thousands separator)
# .precision	For floats (digits after period (floats), for non-numerics (max length)
# type	Number type or s (string format default) see Integer and Float charts

# print("Name: {:*^12}".format("Ringo"))
# print("Name: {:#<10}".format("Ring"))
# print("Name: {:#>10}".format("Ring"))
# print("Name: {:#^10}".format("Ring"))
# print("Percent: {:=+10.1%}".format(13499.99))
##############################################################################
# EXCERCISE 9
##### Open a REPL, and create a variable, name, with your name in it.
##### List the attributes of the string.
##### Print out the help documentation for the .find and .title methods.
############ START PROGRAM ##########
# name = "ravi raja"
# dir(str)
#    # help(str.find)
# help(str.title)
########### END PROGRAM #############
# Open a REPL, and create a variable, age, with your age in it.
# List the attributes of the integer.
# Print out the help documentation for the .numerator method.
##############################################################################
# EXCERCISE 10
# Create a variable, age, set to your age.
# Create another variable, old, that uses a condition to test whether you are older than 18.
# The value of old should be True or False.
############ START PROGRAM ##########
# age = 40
# old = True if age>18 else False
# print(old)
########### END PROGRAM #############
##############################################################################
# EXCERCISE 10
# Create a variable, name, set to your name.
# Create another variable, second_half, that tests whether the name would be classified in the second half of the alphabet?
# What do you need to compare it to?
############ START PROGRAM ##########
##### Method #1 : Using list comprehension
# name = "ravi raja"
# s_half = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
# res = [ele for ele in s_half if(ele in name)]
# print(res)

##### Method #2 : Using any()
# name = "ravi raja"
# s_half = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
# res = any(ele in name for ele in s_half)
# print(res)
########### END PROGRAM #############
##############################################################################
# xl = 'Oct2000.xls'
# print(xl.endswith('xls'))
# print(xl.startswith('Oct'))
############ START PROGRAM ##########
# Create a string, school, with the name of your elementary school.
# Examine the methods that are available on that string.
# Use the help function to view their documentation.
## UPPERCASE

# school = "Tagore School"
# print(school.upper())  #  TAGORE SCHOOL
# ## CAPITALIZE
# var1 = "tagore school"
# print(school.capitalize())  # Tagore school
# ## String adding
# var2 = "wyra"
# print(var1 +" "+ var2) # tagore school wyra
# print( ",".join((var1, var2)) )  # tagore school, wyra
# ## Center    str.center(width[, fillchar])
# var3 = "Ravi Raja"
# print(var3.center(11,'$'))
#
# print(var3.count('Ra'))  ##  count of 'Ra'  is 2
# print(var3.count('Ra',0,-1)) ## count of 'Ra'  is 2  --> Guessing -1 represents last char position
#
# print(var3.isalpha()) ## CHECKING WHETHER STRING IS ALPAHA OR NOT
# print(var3.isalnum()) ## CHECKING WHETHER STRING IS ALPAHA NUMERIC OR NOT
# print(var1.title())   ## "tagore school" --> Tagore School"
# print(len(school)) ## DISPLAYING STRING LENGTH 13
#
# filename = "hello.py"
# print(filename.endswith('.java'))
# print(filename.index('py'))
# print(filename.startswith('.java'))
########### END PROGRAM #############
##############################################################################

# Create a list, names, with the names of people in a class.
# Write code to print 'The class is empty!' or 'Class has enrollments.',
# based on whether there are values in names.
############ START PROGRAM ##########
# names = ['ravi', 'raja', 'anh']
# print(type(names))
# if len(names) > 0:
#     print("Class has enrollments")
# else:
#     print("The class is empty!")
#
# for item in names:
#     print(item)
#     print(item.isalpha())  ###  We can't concatnate Boolean result with any other String to print.
########### END PROGRAM #############
##############################################################################
# Create a variable, car, set to None.
# Write code to print 'Taxi for you!', or 'You have a car!',
# based on whether or not car is set (None is not the name of a car).
############ START PROGRAM ##########
# car = None
# print("Type of car variable is:", type(car))
# if car:
#     print("You have a car!")
# else:
#     print("Taxi for you!")
########### END PROGRAM #############
##############################################################################

# Write an if statement to determine whether a variable holding a year is a leap year.
# (See the Numbers chapter exercises for the rules for leap years).
#
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 25) then (it is a leap year)
# else if (year is not divisible by 16) then (it is a common year)
# else (it is a leap year)
#
# Every year that is exactly divisible by four is a leap year,
# except for years that are exactly divisible by 100,
# but these centurial years are leap years if they are exactly divisible by 400.
# For example, the years 1700, 1800, and 1900 are not leap years,
# but the years 1600 and 2000 are.

# if year is divisible by 400 then is_leap_year
# else if year is divisible by 100 then not_leap_year
# else if year is divisible by 4 then is_leap_year
# else not_leap_year
# There are 30 leap years between 1900 and 2020: 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020.

############ START PROGRAM ##########
# birthYear = 1906
# print(birthYear%4)
# print(birthYear%5)
# print(birthYear%16)
# if birthYear%400 == 0:
#     print("birthYear is a leap year")
# elif birthYear%100 == 0:
#     print("birthYear is not a leap year")
# elif birthYear%4 == 0:
#     print("birthYear is a leap year")
# else:
#     print("birthYear is not a leap year")
########### END PROGRAM #############
##############################################################################
# Write an if statement to determine whether a variable holding an integer is odd.
############ START PROGRAM ##########
# var = 33
# if var%2 == 0:
#     print("Variable is: ",var," even")
# else:
#     print("Variable is: ",var," odd")
########### END PROGRAM #############
##############################################################################
############ START PROGRAM ##########

# names = ['George', 'Fred']
# temp = names.sort()
# temp1 =sorted(names)
# print(temp)   ## None
# print(temp1)  ## ['Fred', 'George']
#
# things = [2, 'abc', 'Zebra', '1']
# ### print(things.sort()) ## Throws TypeError: '<' not supported between instances of 'str' and 'int'
# things.sort(key=str)
# print(things)

########### END PROGRAM #############
##############################################################################
####  LISTS  #####
# Lists, as the name implies, are used to hold a list of objects.
# In Python, a list may hold any type of item and may mix item type.

############ START PROGRAM ##########
# nums = range(5)
# print(nums)  ## range(0, 5)
# print(type(nums)) ## <class 'range'>
# print(list(nums)) ## [0, 1, 2, 3, 4]
#
# even = range(0, 11, 2)
# print(even)
# print(list(even))
#
# odd = range(1, 11, 2)
# print(odd)
# print(list(odd))
#
# print(list(even) + list(odd))
# ordered = sorted(list(even) + list(odd))
# print(ordered)
########### END PROGRAM #############
######  TUPLES  ######

# The main difference between the objects is mutability.
# Tuples are used for returning multiple items from a function.
# Tuples also serve as a hint to the developer that this type is not meant to be modified.
# Tuples also use less memory than lists.
# If you have sequences that you are not mutating, consider using tuples to conserve memory.

# ?Tuples (commonly pronounced as either ?two?-ples or ?tuh?-ples) are immutable sequences.
# You should think of them as ordered records. Once you create them, you cannot change them.
# To create a tuple using the literal syntax, use parentheses around the members and commas in between.
# There is also a tuple class that you can use to construct a new tuple from an existing sequence:?

############ START PROGRAM ##########
# row = ('George', 'Guitar')
# print(row)
#
# row1 = (['George','1'], ['Guitar', '2'])
# print(row1)
#
# p = tuple(['Steph', 'Curry', 'Guard'])
# print(p)
########### END PROGRAM #############
##############################################################################
#######   Sets   ########
# Another container type found in Python is a set.
# A set is an unordered collection that cannot contain duplicates.
# Like a tuple, it can be instantiated with a list or anything you can iterate over.
# Unlike a list or a tuple, a set does not care about order.
# Sets are particularly useful for two things, removing duplicates and checking membership.
# Because the lookup mechanism is based on the optimized hash function found in dictionaries,
# a lookup operation takes very little time, even on large sets.

# Why use a set instead of a list?
# Remember that sets are optimized for membership and removing duplicates.
# If you find yourself performing unions or differences among lists, look into using a set instead.
# Sets are also much quicker for testing membership.
# The in operator runs faster for sets than lists.
# However, this speed comes at a cost. Sets do not keep the elements in any particular order,
# whereas lists and tuples do. If the order is important for you, use a data structure that remembers the order.?


# digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(digits)
# digit_set = set(digits)
# print(digit_set)  ## Removes extra digit 1
#
# digit_set2 = {0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(digit_set2)
#
# #### To check for membership, you use the in operation:
# print("Cheking 5 in digit_set2:", 5 in digit_set2)
# print("Cheking 10 in digit_set2:", 10 in digit_set2)

###  Sets provide set operations, such as union (|), intersection (&), difference (-), and xor (^).?
# even = {0, 2, 2, 4, 4, 6, 8, 8}
# odd = {0, 1, 1, 3, 5, 7, 9, 9}
# union = even | odd
# print(union)   #  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# intersection = even & odd
# print(intersection)   #   {0}
# difference = even - odd
# print(difference)  #  {8, 2, 4, 6}
# difference1 = odd - even
# print(difference1)  #  {1, 3, 5, 7, 9}
# xor = even ^ odd
# print(xor)  #  {1, 2, 3, 4, 5, 6, 7, 8, 9}

##############################################################################


# animals = ["cat", "dog", "bird"]
# for index, value in enumerate(animals):
#     print(index, value)

########################   1   ##################
# names = ['John', 'Paul', 'George', 'Ringo']
# for name in names:
#     if name not in ['John', 'Paul']:
#         names.remove(name)
#     else:
#         continue
# print(names)
########################   2   ##################
# names = ['John', 'Paul', 'George', 'Ringo']
# names_to_remove = []
# for name in names:
#     if name not in ['John', 'Paul']:
#         names_to_remove.append(name)
# for name in names_to_remove:
#     names.remove(name)
# print(names)
########################   3   ##################
# names = ['John', 'Paul', 'George', 'Ringo']
# for name in names[:]:  ###### copy of names  ####
#     if name not in ['John', 'Paul']:
#          names.remove(name)
# print(names)

##############################################################################
##### DICTIONARY ######

# names = ['Ringo', 'Paul', 'John', 'Ringo']
# print(type(names))
# count = {}  ##  This dictionary is empty and no key --> value
# count1 = {}
# print(type(count))
# for name in names:
#     count.setdefault(name, 0)  ## Here we initialize Key and value
#     count[name] += 1
#     count1.setdefault(name, 0)
# print(count)

####### COLLECTIONS ########
############ START PROGRAM ##########
# import collections
# count = collections.Counter(['Ringo', 'Paul', 'John', 'Ringo'])
# print(count)   #  ?Counter({'Ringo': 2, 'Paul': 1, 'John': 1})
# print(count['Ringo']) # 2
# print(count['Fred'])  # 0
########### END PROGRAM #############
##############################################################################
############ START PROGRAM ##########
# band1_names = ['John', 'George', 'Paul', 'Ringo']
# band2_names = ['Paul']
# names_to_bands = {}
# for name in band1_names:
#     names_to_bands.setdefault(name,[]).append('Beatles')
# #### Due to multiple values required, we used setdefault with value as a list. Ex. (name, [])
# for name in band2_names:
#     names_to_bands.setdefault(name,[]).append('Wings')
# print(names_to_bands)
# print(names_to_bands['Paul'])
########### END PROGRAM #############
############ START PROGRAM ##########

# from collections import defaultdict
# names_to_bands = defaultdict(list)
# band1_names = ['John', 'George', 'Paul', 'Ringo']
# band2_names = ['Paul']
# for name in band1_names:
#     names_to_bands[name].append('Beatles')
# for name in band2_names:
#     names_to_bands[name].append('Wings')
# print(names_to_bands)
# print(names_to_bands['Paul'])

########### END PROGRAM #############
############ START PROGRAM ##########

# data = {'Adam': 2, 'Zeek': 5, 'Fred': 3}
# for key,value in data.items():
#     print(key, value)
#
# print(list(data.items()))
#
# for name in sorted(data.keys()):
#      print(name)
#
# for name in sorted(data.values()):
#      print(name)
# print("PRINTING DESCENDING ORDER")
# for name in sorted(data.keys(),reverse=True):
#      print(name)

########### END PROGRAM #############
##############################################################################
###########  FILE READ ##########
############ START PROGRAM ##########
# fin = open('temp.txt','r')     ## It will open ONLY existing file
# print(fin.readline())          ## It will read and print first line
# print(fin.readlines())          ## It will read each line and saves as a string in a list
# print(fin.read())            ## It will read and print entire file

# for line in fin.readlines():
#      print(line)                ##  Each line will print with a blank line "\n"

# for line in fin:        ##  fin.readlines() and fin  prints same result but fin.readlines() consumes more memory
#      print(line)
########### END PROGRAM #############
##############################################################################
###########  FILE WRITE ##########
############ START PROGRAM ##########
# fout = open('temp.txt','w')
# fout.write('This is a test line, write through python file write function')  ### This will override the file
# fout = open('temp.txt','r')
# print(fout.readlines())
# fout = open('temp.txt','a')
# fout.write('This is another test line, write through python append function')
# fout = open('temp.txt','r')
# print(fout.readlines())
# fout.close()
########### END PROGRAM #############
##############################################################################
############ START PROGRAM ##########
#### BELOW EXPLAINS REUSABLE LOGIC BY SEPERATING OPENING FILE AND ADDING SEQUENCE NUMBERS

# def add_numbers(filename):
#      with open(filename) as fin:
#         return add_nums_to_seq(fin)
#
# def add_nums_to_seq(seq):
#     results = []
#     for num, line in enumerate(seq):
#         results.append('{0}-{1}'.format(num, line))
#     print(results)      ## Prints lines with prepended line numbers.
#     return results
#
# add_numbers('temp.txt')  ## Passing filename to add_numbers function.

########### END PROGRAM #############
##############################################################################

# Write a function to write a comma separated value (CSV) file.
# It should accept a filename and a list of tuples as parameters.
# The tuples should have a name, address, and age.
# The file should create a header row followed by a row for each tuple. If the following list of tuples was passed in:
#
# [('George', '4312 Abbey Road', 22),
#  ('John', '54 Love Ave', 21)]
# it should write the following in the file:
#
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
############ START PROGRAM ##########
# list = [('George', '4312 Abbey Road', '22'),('John', '54 Love Ave', '21')]
# default = ('name', 'address', 'age')
# # print(type(list))
# # print(type(default))
#
# def create_csv(filename, list):
#     with open(filename, 'w') as fout:
#         fout.write(','.join(default)+'\n')
#         for i in list:
#             # print(type(i))
#             fout.write(','.join(i)+'\n')
#         return fout
#
# create_csv('delete.csv', list )

########### END PROGRAM #############
##############################################################################
###########  COME BACK TO THIS WHEN YOU COME TO MAPS  ##############
# initialize list
# test_list = [(1, 4), (5, 6), (8, 9), (3, 6)]
# print(type(test_list))
# list = str(test_list)
# print(type(list))
# print(list)
#
# # printing original list
# print("The original list is : " + str(test_list))
# print(map(str, test_list))
# List of tuples to String
# using map() + join()
# res = map(",".join(test_list), test_list)
# print(res)
#
# # printing result
# print("Resultant string from list of tuple : " + res)
##############################################################################

# Write a function that reads a CSV file.
# It should return a list of dictionaries, using the first row as key names,
# and each subsequent row as values for those keys.
# For the data in the previous example it would return:
#
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
#  {'name': 'John', 'address': '54 Love Ave', 'age': 21}]
############ START PROGRAM ##########
# dictionary = []
# list1 = []
#
#
# def read_csv(filename):
#     with open (filename, 'r') as fout:
#         for i in fout:
#             list1.append (i.rstrip ("\n").split (","))
#         # print(list1)
#         list_iterator = iter (list1)
#         next (list_iterator)
#         for no, item in enumerate (list1):
#             dictionary.append (dict (zip (list1[0], list1[no])))
#         print("FINAL DICTIONARY:\n", dictionary)
#         return dictionary
#
#
# read_csv ('delete.csv')
########### END PROGRAM #############

##############################################################################

class Chair:  # 1
    """ A Chair on a chairlift """  # 2
    max_occupants = 20  # 3   attributes that are constant are put inside the class definition.

    def __init__(self, id):  # 4 CONSTRUCTOR
        self.id = id  # 5
        self.count = 0  # attributes that are unique to an instance are put in the constructor
        # self.max_occupants = 4

    def load(self, number):  # 6
        self.count += number

    def unload(self, number):  # 7
        self.count -= number


A = Chair ('A1')  # Instance of a class
print ("Instance A type is:", type (A))
print ("id of A is:", A.id)
print ("Chair A1 count before load is:", A.count)
A.load (10)
print ("Chair A1 count after load is:", A.count)
A.unload (5)
print ("Chair A1 count after unload is:", A.count)
print ("Max Occupants of Chair:", A.max_occupants)
# print(id(A.max_occupants))
A.max_occupants = 20
print ("Chair A1 count after load is:", A.max_occupants)
print ("Type of A.max_occupants", type (A.max_occupants))

print ("Max occupants ", Chair.max_occupants)
print ("--> CHECKING TYPES")
print (Chair.max_occupants.__class__)
print (Chair.__init__.__class__)
print (Chair.load.__class__)
print (Chair.unload.__class__)
print ("END OF CHECKING TYPES <-- ")
print (Chair)  # __main__.Chair
print (type (Chair))  # <type 'classobj'>
print (id (Chair))  # 4465303384

print ("ID of A: ", id (A))

# Instance of a class
A = Chair ('A2')  # Use B = Chair('A2') if you want to hold Object assigned to A and it won't remap to another object
print ("Instance Variable 'id' of A is:", A.id)
A.load (10)
print ("After loading Count is:", A.count)
A.unload (2)
print ("After unloading Count is:", A.count)
print ("Constant Instance Class variable 'max_occupants' value:", A.max_occupants)
print ("ID of A: ", id (A))

# Instance of a class
B = Chair ('A3')  # Use B = Chair('A2') if you want to hold Object assigned to A and it won't remap to another object
print ("id of B is:", B.id)
B.load (10)
print ("After loading Count is:", B.count)
B.unload (2)
print ("After unloading Count is:", B.count)
print ("Constant Instance Class variable 'max_occupants' value:", B.max_occupants)

C = B  # TELLING OBJECT C IS EQUAL TO B
print ("ID of C:", id (C))
print ("ID of B:", id (B))
print ("Expecting count from B Object after unload:", C.count)

print ("Printing C all variables:", C.__dict__)

##############################################################################
