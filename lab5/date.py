import string

class Date(object):
    non_leap_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # alternative since no overloading
    def __init__(self, d, y, m = 0):
        self.y = int(y)
        if self.isLeap():
            self.days = self.leap_days
        else:
            self.days = self.non_leap_days

        if m != 0:
            self.m = int(m)
            self.d = int(d)
        else:
            self.toDate(int(d))

    def isLeap(self):
        if self.y % 4 == 0 and self.y % 100 != 0 or self.y % 400 == 0:
            return True
        return False

    def isValid(self):
        if self.m < 1 or self.m > 12:
            return False
        if self.d > self.days[self.m - 1] or self.d < 1:
            return False
        return True

    def toDays(self):
        sum = 0
        for i in range(self.m - 1):
            sum += self.days[i]
        return sum + self.d

    def toDate(self, d):
        i = 0
        while self.days[i] < d and i < 11:
            d -= self.days[i]
            i += 1
        self.m = i + 1
        self.d = d
