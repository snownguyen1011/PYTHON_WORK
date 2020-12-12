# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries.
# Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function.
# The arguments are the name of the new class and a string containing the names of the elements.

from collections import namedtuple

Student = namedtuple('Student', ('fname','lname','age') )
print("What is Student:",Student)
print("Default fields of Student Namedtuple:",Student._fields)
###  Creating a tuple for default Values ###
defaults = (None,) * (len(Student._fields)-1) + (18,)
print("default values to be inserted: ",defaults)

StudentTest = namedtuple('Student', ('fname','lname','age'), defaults =(None, None, None) )
print("NamedTuple with defaults:", StudentTest._fields)
print("StudentTest._field_defaults", StudentTest._field_defaults)

### Applying default values ###
print("After applying default values to Student Namedtuple: ",Student._make(defaults))

Student1 = Student(*defaults)
print("Student1 created with defaults: ",Student1)
print(isinstance(Student1, Student))
### Updating fields ###
Student1 = Student1._replace(fname='ravi raja',lname='koineni', age=32)
print("After replacing default values, Student1 is: ", Student1)

values = Student1[:2]
print("values are:", values)
### Updating fields ###
Student1 = Student._make(Student1[:2] + (33,))
print("Updated age:", Student1)
### Updating fields ###
Student1 = Student._make(values + (34,))
print("Updated age:", Student1)

### ADDING NEW FIELDS TO NAMEDTUPLE ###
StudentNew = namedtuple('Student', Student._fields + ('collegeName','city',))
print("Updating 2 new fields:", StudentNew._fields)

### UPDATING VALUES OF FIELDS ON NAMEDTUPLE ###
Student1 = StudentNew(*Student1, 'SAU','Magnolia',)
print("Student1 Values after updating College and City:", Student1)
print(isinstance(Student1, StudentNew))
print(isinstance(Student1, Student))

###  Reading NamedTuple values ###
print(Student1.fname)
print(Student1.city)

print(getattr(Student1, 'fname'))

Student2 = StudentNew('Anh','Nguyen',32,'HCC','Houston')
print(Student2)

print(Student1 is Student2)
print(Student1 == Student2)

###  CONVERTING NAMEDTUPLE TO DICTIONARY ###
print(Student2._asdict())
Student2Dict = Student2._asdict()
print("Pretty printing", dict(Student2Dict))

### CONVERTING DICTIONARY TO NAMEDTUPLE ###

vehicle_dict = {'Two_Wheeler':'Hero Passion', 'Four_Wheeler':'Toyota Camry', 'Flight':'Spirit'}
print("Vehicle Dictionary:", vehicle_dict)

vehicle_tuple = namedtuple('vehicle_tuple',vehicle_dict.keys(),defaults=(vehicle_dict.values()))
print("Type of vehicle_tuple", vehicle_tuple)
print("Default Fields of vehicle_tuple: ", vehicle_tuple._field_defaults, "\n")

###  BELOW THERE SHOULDN'T BE FIELD DEFAULTS ###
vehicle_tuple1 = namedtuple('vehicle_tuple1',vehicle_dict.keys())(**vehicle_dict)
print(vehicle_tuple1)
print("!!! UNDERSTAND THE CODE WHY NO FIELD DEFAULTS !!!  ==> ", vehicle_tuple1._field_defaults,"\n")

###  USE EITHER A SPACE OR COMMA
print(','.join(sorted(vehicle_dict.keys())))
print(' '.join(sorted(vehicle_dict.keys())))

vehicle_tuple2 = namedtuple('vehicle_tuple2', ' '.join(sorted(vehicle_dict.keys())))(**vehicle_dict)
print("vehicle_tuple2:", vehicle_tuple2,"\n")

### USING A FUNCTION ###
def convert(dictionary):
    return namedtuple('dict2namedtuple', dictionary.keys())(**dictionary)

test = convert(vehicle_dict)
print(test)


