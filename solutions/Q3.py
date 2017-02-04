
s = '--->-><-><-->-'

def answer(s):
    num = 0
    p = 0

    while s != '':

        c = s[-1]
        s = s[:-1]

        if c == '<':
            p = p + 1
        elif c == '>':
            num = num + p

    return 2*num
