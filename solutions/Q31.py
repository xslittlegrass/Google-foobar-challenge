
def answer(M,F):
    m = int(M)
    f = int(F)

    if m%2 == 0 and f%2 == 0:
        return "impossible"

    generation = 0
    factor = 1

    while min(m,f) != 1:
        if max(m,f)%min(m,f) == 0:
            print(m,f)
            return "impossible1"
        elif m > f:
            factor = m//f
            m = m%f
            generation += factor
        else:
            factor = f//m
            f = f%m
            generation += factor

    generation = generation + m + f -2

    return generation
