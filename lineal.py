import math
from fractions import gcd

#Congruencia Lineal
def linear_congruential(x, a, c, m, N):
    rList = []
    xi = float((x * a + c) % m)
    ri = xi/m
    rList.append(ri)
    while(N > 1):
        xi = (xi * a + c) % m
        ri = xi/m
        rList.append(ri)
        N -= 1
    return rList

#Congruencia lineal mixta
def smallestPrimeDivisor(n):
    if(n % 2 == 0):
        return 2

    i = 3
    while(i * i <= n):
        if(n % i == 0):
            return i
        i += 2

    return n


def hullDobell(x, a, c, m):
    q = smallestPrimeDivisor(m)
    cond1 = False
    cond2 = False
    cond3 = False
    

    if gcd(c, m) == 1:
        cond1 = True
    
    if (a-1) % q == 0:
        cond2 = True

    if (a-1) % 4 == 0:
        cond3 = True


    conditions = (cond1, cond2, cond3)


    if all(conditions):
        return True, conditions
    else:
        return False, conditions
#Aqui termina congruencia lineal mixta
#Aqui termina congruencia lineal mixta
liste = []
liste = linear_congruential(8,9,13,32,32)

for i in liste:
    print(i)