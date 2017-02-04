import math
from decimal import *

def answer(m_str):
    getcontext().prec = 300
    m = Decimal(int(m_str))
    res =  m*(m+Decimal(1))*Decimal(2).sqrt()/Decimal(2)-m/Decimal(2)
    print res
    return format(res,'.0f')

def check(m_str):
    m = int(m_str)
    sum = 0
    for i in range(m+1):
        sum += math.floor(i*math.sqrt(2))

    return str(int(sum))


# we can find a recurence relationship using Beatty's theorem


def S(n):
    getcontext().prec = 300
    c = Decimal(2).sqrt() - Decimal(1)
    if n == Decimal(0):
        return Decimal(0)
    m = (c*n).quantize(Decimal(0),rounding = ROUND_FLOOR)
    return n*m + n*(n+Decimal(1))/Decimal(2) - m*(m+Decimal(1))/Decimal(2) - S(m)

def answer(n_str):
    n = Decimal(n_str)
    return format(S(n),'.0f')
