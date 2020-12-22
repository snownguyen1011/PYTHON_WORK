class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print ("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubclass (BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me ()  ## OBSERVE
        print ("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubclass (BaseClass):
    num_right_calls = 0


    def call_me(self):
        super().call_me ()    ## OBSERVE
        print ("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass (LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me (self)
        RightSubclass.call_me (self)
        print ("Calling method on Subclass")
        self.num_sub_calls += 1

class Subclass1 ( RightSubclass, LeftSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me (self)
        RightSubclass.call_me (self)
        print ("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass()
s.call_me()
print("Sub Calls:",s.num_sub_calls,"Left Calls:", s.num_left_calls,"Right Calls:", s.num_right_calls,"Base Calls", s.num_base_calls)

print(" Printing Subclass1: -->\n")
s1 = Subclass1()
s1.call_me()
print("Sub Calls:",s1.num_sub_calls,"Left Calls:", s1.num_left_calls,"Right Calls:", s1.num_right_calls,"Base Calls", s1.num_base_calls)