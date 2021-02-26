import math

#Metodo Congruencial Mutiplicativo
def multiplicativo(x, a, m, n): #TODO check implementation
    # x Semilla
    # a Multiplicador
    # m Parametro del modulo
    # n numero de valores a crear

    # Ciclo para crear los numeros 
    rList = []
    xi = float((x * a) % m)
    ri = xi/m
    rList.append(ri)
    while(n > 1):
        xi = (xi * a) % m
        ri = xi/m
        rList.append(ri)
        n -= 1
    return rList
#fin  

# print(multiplicativo(5, 5, 32, 12))
