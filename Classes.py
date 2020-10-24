class CorrectChair:
    """ A Chair on a chairlift
        Checking loading correct number of Occupants
        DO NOT LOAD MORE THAN max_occupants """

    max_occupants = 20

    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        new_val = self._check (self.count + number)
        self.count = new_val

    def unload(self, number):
        new_val = self._check (self.count - number)
        self.count = new_val

    def _check(self, number):
        if number > self.max_occupants:
            raise ValueError ('Invalid count:{}'.format (
                number))
        return number


A = CorrectChair ('A1')
print ("Initial:", A.__dict__)
A.load (20)
print ("After Loading", A.__dict__)
A.unload (10)
print ("After unloading 10:", A.__dict__)
print ("Again loading 11:")
# A.load(11)
# print(A.__dict__) # Throws ValueError: Invalid count:21
