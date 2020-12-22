student_joe = {'gpa': 3.7, 'major': 'physics', 'name': 'Joe Smith'}
student_jane = {'gpa': 3.8, 'major': 'chemistry', 'name': 'Jane Jones'}
student_zoe = {'gpa': 3.4, 'major': 'literature', 'name': 'Zoe Fox'}
students = [student_joe, student_jane, student_zoe]

####### METHOD 1 - OLD WAY
def max_by_gpa(items):
    biggest = items[0]
    for item in items[1:]:
        if item["gpa"] > biggest["gpa"]:
            biggest = item
            return biggest

print("METHOD 1: ", max_by_gpa (students))
#### FUNCTION AS AN OBJECT #####
def get_gpa(who):
    return who["gpa"]
################################
####### METHOD 2 - NEW WAY
nums = ["12", "7", "30", "14", "3"]   ### items are Strings
print("Max of List nums:(WRONG WAY) ",max(nums))
def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
            return biggest

print("Max of List nums:(CORRECT WAY) ",max_by_key(nums, int))

print(max_by_key(students, get_gpa))  ## FUNCTION(get_gpa) AS AN OBJEST

integers = [3, -2, 7, -1, -20]
print("Max of List integers: ",max(integers))
def max_by_abs(items):
    biggest = items[0]
    for item in items[1:]:
        if abs(item) > abs(biggest):
            biggest = item
    return biggest

print("Max by Absolute value of List integers: ",max_by_abs(integers))