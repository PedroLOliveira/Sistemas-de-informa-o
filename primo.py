import math
from time import time
def ehPrimo(n):
    result = True
    for i in range (2,int(math.sqrt(n))+1):
        #print('{} dividido por {}'.format(n,i))
        if (n % i) == 0:
            result = False
            break

    return result

def performance(n):
    rates = {}

    start = time()
    retorno = ehPrimo(n)
    end = time()

    diff = (end - start) * 1000
    rates[n] = diff
    print(n, '\t demorou ', diff, '\t e retornou ', retorno)

if __name__ == "__main__":
    for n in range (1,100001):
        performance(n)