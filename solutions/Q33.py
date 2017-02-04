import math

def answer(n):

    partitionQ_memo = {}

    def partitionQ(n):

        if n == 0:
            return 1
        elif n < 0:
            return 0


        if n not in partitionQ_memo:
            an = 0
            qn = 0

            m1 = 1.0/6*(1+math.sqrt(1+12*n))
            m2 = 1.0/6*(1-math.sqrt(1+12*n))

            if int(m1) == m1:
                an = (-1)**m1
            if int(m2) == m2:
                an = (-1)**m2

            for k in range(-n,0):
                qn = qn + (-1)**(k-1)*partitionQ(n-k*(3*k-1)//2)
            for k in range(1,n+1):
                qn = qn + (-1)**(k-1)*partitionQ(n-k*(3*k-1)//2)

            qn = int(qn + an)

            partitionQ_memo[n] = qn

        return partitionQ_memo[n]


    return partitionQ(n) - 1
