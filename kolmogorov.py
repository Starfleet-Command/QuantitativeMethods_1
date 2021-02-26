import math
from scipy.stats import ksone 

def kolmogorovSmirnov(stringList, alpha):
    sortedList = sorted(stringList)
    N = len(sortedList)

    i_N = [(float(i)/N) for i in range(N+1)]
    dPlus = [float(abs(i_N[i+1] - sortedList[i])) for i in range(N)]
    dMinus = [float(abs(sortedList[i] - i_N[i])) for i in range(N)]
    
    d = max([max(dPlus), max(dMinus)])
    dalpha = ksone.ppf(1-alpha/2, N)

    if(d > dalpha):
        hipothesis = False
    else:
        hipothesis = True
        
    return  d, dalpha, hipothesis


# rlist = [0.44, 0.81, 0.14, 0.05, 0.95]

# print(kolmogorovSmirnov(rlist, 0.05))
