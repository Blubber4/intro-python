import math
import cmath

class Quadratic:
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.disc = ((b*b) - (4*a*c))

    def isInfinite(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            return True
        return False

    def isContradiction(self):
        if self.a == 0 and self.b == 0 and self.c != 0:
            return True
        return False

    def hasSingleRoot(self):
        if self.a == 0:
            if self.isInfinite() == False and self.isContradiction() == False:
                return True
        return False

    def hasRealRoots(self):
        if self.disc > 0:
            return True
        return False

    def hasRepeatedRoot(self):
        if self.disc == 0:
            return True
        return False

    def hasComplexRoots(self):
        if self.disc < 0:
            return True
        return False

    def quadraticPlus(self):
        if self.hasComplexRoots():
            # returning as string so formatting is in this function which is weird but this way can use i without overloading print
            ans_a = str(format(-self.b / (2*self.a), '.3f'))
            ans_b = str(format(math.sqrt(abs(self.disc)) / (2*self.a), '.3f'))
            return ans_a + " + " + ans_b + "i"
            # easier alternative using cmath library - uses j for imaginary - would need formatted in print function.
            # return (-self.b + cmath.sqrt(self.disc)) / (2*self.a)

        else:
            return (-self.b + math.sqrt(self.disc)) / (2*self.a)

    def quadraticMinus(self):
        if self.hasComplexRoots():
            # returning as string so formatting is in this function which is weird but this way can use i without overloading print
            ans_a = str(format(-self.b / (2*self.a), '.3f'))
            ans_b = str(format(math.sqrt(abs(self.disc)) / (2*self.a), '.3f'))
            return ans_a + " - " + ans_b + "i"
            # easier alternative using cmath library - uses j for imaginary - would need formatted in print function.
            # return (-self.b - cmath.sqrt(self.disc)) / (2*self.a)

        else:
            return (-self.b - math.sqrt(self.disc)) / (2*self.a)

    def solve(self):
        if self.isInfinite():
            print("\n\t\tInfinite Solutions.")
        elif self.isContradiction():
            print("\n\t\tContradict Equation.")
        elif self.hasSingleRoot():
            solution = -self.c / self.b
            print("\n\t\tSingle Root. x = ", format(solution, '.0f'), sep = '')
        elif self.hasRealRoots():
            print("\n\t\tTwo real roots. X1 = ", format(self.quadraticPlus(), '.0f'), " , X2 = ", format(self.quadraticMinus(), '.0f'), sep = '')
        elif self.hasRepeatedRoot():
            print("\n\t\tRepeated Root. X = ", format(self.quadraticPlus(), '.0f'), sep = '')
        elif self.hasComplexRoots():
            print("\n\t\tTwo Complex Roots. X1 = ", self.quadraticPlus(), ", X2 = " , self.quadraticMinus(), sep = '')
        else:
            print ("\n\t\tError, please check your input.")