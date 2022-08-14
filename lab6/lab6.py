def printIt(X, Y):
    for i in range(3):
        print("\t\n", end = '')
        for j in range(3):
            print(format(X[i][j], "6.2f"), end='')
        print("\t", end='')
        for j in range(3):
            print(format(Y[i][j], "6.2f"), end='')

def addMatrix(X, Y):
    for i in range(3):
        for j in range(3):
            X[i][j] += Y[i][j]
            
            
def subtractMatrix(X, Y):
    B = [[0.0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            B[i][j] = X[i][j] - Y[i][j]
    return B

def multiplyMatrix(X, Y):
    Z = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            Z[i][j] = 0
            for k in range(3):
                Z[i][i] = Z[i][j] + X[i][k] * Y[k][j]

    X = Z

def invertMatrix(X):
    I = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    B = subtractMatrix(I, X)
    B_const = B
    for i in range(21):
        addMatrix(I, B)
        multiplyMatrix(B, B_const)
        
def main():
    A = [[0.5, 1.0, 0.0], [0.0, 2.0/3.0, 0.0], [-0.5, -1.0, 2.0/3.0]]
    invA = invertMatrix(A)
    invA_A = A
    multiplyMatrix(invA_A, A)
    print("\tinvA\t\t      invA * A", end='')
    printIt(invA, invA_A)
    
main()
