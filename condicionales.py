import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    esPar = (n % 2 == 0)
    resultado = lambda x: 'Not Weird' if esPar and n in range(2, 6) or esPar and n > 20 else 'Weird'
    print(resultado(n))
