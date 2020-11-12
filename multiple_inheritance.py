#####################################################
##### TO UNDERSTAND **kwargs  IN MULTIPLE INHERITANCE
#####################################################
class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):  # 2.
        super ().__init__ (**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append (self)


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super ().__init__ (**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend (Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):  # 1:
        super ().__init__ (**kwargs)  # 3.
        self.phone = phone


# # 1: PASSING ONLY ONE ARGUMENT
# f = Friend("903111222")
# print("PHONE",f.phone)
# # 2: PASSING 3 ARGS
# f1 = Friend("903111222",name="ravi", email="ravi@gmail.com")   ## name and email parameter names must be passed
# print("NAME",f1.name)
# print("EMAIL",f1.email)
# print("PHONE",f1.phone)
# 3. PASSING MULTIPLE ARGS
f2 = Friend ("903111222", name="ravi", email="ravi@gmail.com", city="Durham", state="North Carolina")
print ("NAME", f2.name)
print ("EMAIL", f2.email)
print ("PHONE", f2.phone)
print ("STREET", f2.street)  # PRINTS BLANK AS WE DIDN'T PASS THIS ARGUMENT
print ("CITY", f2.city)
print ("STATE", f2.state)
print ("CODE", f2.code)  # PRINTS BLANK AS WE DIDN'T PASS THIS ARGUMENT
