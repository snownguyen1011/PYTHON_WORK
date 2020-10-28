class CorrectChair:
    """ A Chair on a chairlift
        Checking loading correct number of Occupants
        DO NOT LOAD MORE THAN max_occupants
        Subclasses(Chair6) allow you to inherit methods of Super/parent (CorrectChair) classes,
        and override methods you want to change """

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


class StallChair (CorrectChair):
    def __init__(self, id, is_stalled):
        super ().__init__ (id)
        self.is_stalled = is_stalled
        self.stalls = 0

    # def load(self, number):
    #     print("test", self.is_stalled)
    #     if self.is_stalled(number, self):
    #         self.stalls += 1
    #         super().load(number)

    # def is_stalled():
    #     """Return True 10% of time"""
    #     return self.max_occupants


A = StallChair ('A1', 5)
print ("Initial:", A.__dict__)
A.load (5)
print ("After Loading", A.__dict__)
A.unload (1)
print ("After unloading 1:", A.__dict__)
# print ("Again loading 3:")
# A.load (3)
# print (A.__dict__)  # Throws ValueError: Invalid count:7
