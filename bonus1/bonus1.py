import math
import myMath

def main():
    more = 'y'
    n = int(21)
    while (more == 'y' or more == 'Y'):
        x = float(input("\n\t\tInput x: "))
        print("\n\t\t\t\t   My Result     LibraryResult", end = "")
        print("\n\t\tSin(", x, "),\t", format(myMath.mySin(x, n), '10.6f'), "\t", format(math.sin(x), '10.6f'))
        print("\n\t\tCos(", x, "),\t", format(myMath.myCos(x, n), '10.6f'), "\t", format(math.cos(x), '10.6f'))
        print("\n\t\tExp(", x, "),\t", format(myMath.myExp(x, n), '10.6f'), "\t", format(math.exp(x), '10.6f'))
        more = input("\n\n\t\t\tDo more (Y/N)?: ")
        
main()
