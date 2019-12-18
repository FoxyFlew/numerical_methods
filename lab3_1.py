import math
import random

def metod(f, a, b, e):
    while abs(a - b) >= e:
        c = (a + b) * 0.5
        fa = f(a)
        fb = f(b)
        fc = f(c)
        if abs(fc) < e:
            return c
        if fa * fc < 0:
            b = c
        elif fb * fc < 0:
            a = c
    return (a + b) * 0.5

if __name__ =='__main__':
    f = lambda x: (1 + x ** 2) * math.exp(-x) + math.sin(x)
    random.seed(999)
    roots = []
    for i in range(1000):
        r1 = random.uniform(0, 10)
        r2 = random.uniform(0, 10)
        if r1 > r2:
            r1, r2 = r2, r1
        if not(f(r1) * f(r2) < 0):
            continue
        s = metod(f, r1, r2, 1e-12)
        sum_ = sum(1 for x in roots if abs(x - s) < 1e-9)
        
        if sum_ == 0:
            
            roots.append(s)
    print(sorted(roots))