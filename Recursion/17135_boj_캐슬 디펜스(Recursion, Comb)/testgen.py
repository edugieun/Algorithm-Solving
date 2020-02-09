from random import *

for _ in range(20):

    N = randint(3, 15)
    M = randint(3, 15)
    D = randint(1, 10)
    print(N,M,D)
    for i in range(N):
        for j in range(M):
            val = randint(0, 1)
            print(val, end=' ')
        print()
