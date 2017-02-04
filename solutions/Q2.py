#import numpy as np

def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


pegs = [4, 30, 50]

num = len(pegs)

dist = [pegs[i+1]-pegs[i] for i in range(len(pegs)-1)]


M = [[0 for i in range(num+1)] for j in range(num)]


for i in range(num-1):
    M[i][i] = 1
    M[i][i+1] = 1
    M[i][-1] = dist[i]

M[num-1][0] = 1
M[num-1][-2] = -2

b = dist + [0]

#xtp = np.linalg.solve(M,b)

#x = [i.as_integer_ratio() for i in xtp]

x = gauss(M)

print(list(x[0]))
