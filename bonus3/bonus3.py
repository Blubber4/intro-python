def printIt(ax):
    for i in ax:
        print(i, end=" ")

def shellSort(x, size): # do we need size?
    jump = size // 2
    while jump > 0:
        for i in range(jump):
            for j in range(i + jump, size, jump):
                cur = x[j]
                pos = j
                while x[pos - jump] > cur and pos >= jump:
                    x[pos] = x[pos - jump]
                    pos = pos - jump
                    x[pos] = cur
        jump = jump // 2

def binarySearch(x, tgt, size):
    first = 0
    last = size - 1
    while first <= last:
        m = (first + last) // 2
        if x[m] < tgt:
            first = m + 1
        elif x[m] > tgt:
            last = m - 1
        else:
            return m + 1
    return 0 # returns 0 if not found



def main():
    n = [48, 29, 95, 68, 85, 72, 17, 33, 37, 14, 9, 55, 42, 59, 3]
    size = 15 # size of array to sort
    print("\n\t Unsorted Sequence: ", end='')
    printIt(n)
    print("\n\t Sorted Sequence:   ", end='')
    shellSort(n, size)
    printIt(n)

    more = 'y'
    while more == 'y' or more == 'Y':
        tgt = int(input("\n\t\tInput a number to search: "))
        loc = binarySearch(n, tgt, size)
        if loc > 0:
            print("\n\t\t", tgt, "was found at location", loc)
        else:
            print("\n\t\t", tgt, "was NOT found")

        more = input("\n\t\t\tDo more (Y/N)? ")

main()
