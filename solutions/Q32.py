def getXor(x,y):
    def f(a):
        return [a,1,a+1,0][a%4]
    return f(x-1)^f(y)

def answer(start,length):
    result = 0
    for i in range(length):
        result = result ^ getXor(start + i*length, start + (i+1)*length -(i+1))
    return result
