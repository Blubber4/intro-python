import quadratics

def main():
    print("\tSolve Quadratic equation for giving A, B, C coefficient")
    more = 'Y'
    while more == 'y' or more == 'Y':
        a = float(input("\n\t\tPlease input A: "))
        b = float(input("\n\t\t             B: "))
        c = float(input("\n\t\t             C: "))
        equation = quadratics.Quadratic(a, b, c)
        equation.solve()
        more = input("\n\t\tDo more (Y/N)?: ")

main()