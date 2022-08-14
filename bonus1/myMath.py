# x is number to take sin of, n is number of iterations (higher = more accurate).
def mySin(x, n):
    sum = x
    prod = x
    sign = -1
    for i in range(1, n):
        prod *= (x*x) / ((2*i) * (2*i + 1))
        sum += sign * prod
        sign *= -1
    return sum

def myCos(x, n):
    sum = 1.0
    prod = 1.0
    sign = -1
    for i in range(1, n):
        prod *= (x*x) / ((2*i) * (2*i - 1))
        sum += sign * prod
        sign *= -1
    return sum

def myExp(x, n):
    sum = 1.0
    prod = 1.0
    for i in range(1, n):
        prod *= x / i
        sum += prod
    return sum
