from fractions import gcd

pegs = [4, 30, 50]

# construct the inverse matrix


def answer(pegs):

    divider = 1

    num = len(pegs)

    if num%2 == 0:
        divider = 3

    if num%2 == 0:
        factor = -1
    else:
        factor = 1

    M = [[0 for i in range(num)] for j in range(num)]

    for i in range(num-1):
        for j in range(num-1):

            if i <= j:
                if (i+j)%2 == 0:
                    M[i][j] = 2
                else:
                    M[i][j] = -2
            else:
                if (i+j)%2 == 0:
                    M[i][j] = factor
                else:
                    M[i][j] = -1*factor

                    
    
    for i in range(num):
        if i%2 == 1:
            M[i][-1] = factor
        else:
            M[i][-1] = -1*factor
    for i in range(num-1):
        if i%2 == 1:
            M[-1][i] = -1
        else:
            M[-1][i] = 1


    # ==== calculate M1 ==========

    M1 = [0 for i in range(num)]

    for i in range(num-1):
        if i%2 == 0:
            M1[i] = 2
        else:
            M1[i] = -2

    if i%2 == 0:
        M1[-1] = 1
    else:
        M1[-1] = -1 

    distance = [pegs[i+1] - pegs[i] for i in range(num-1)] + [0]

    x1 = sum([M1[i]*distance[i] for i in range(num)])

    x = []


    for i in range(num):
        x.append(sum([M[i][j]*distance[j] for j in range(num)]))


    for i in range(num):
        if x[i]<divider:
            return [-1,-1]

    x1 = x[0]

    if x1%divider == 0:
        return [x1/divider,1]
    else:
        return [x1,divider]



