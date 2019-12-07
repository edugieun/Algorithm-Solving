import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())), reverse=True)
    T = sorted(list(map(int, input().split())), reverse=True)

    stuff_sum = 0
    for stuff in W:
        for i in range(len(T)):
            if T[i] >= stuff:
                T[i] = 0
                stuff_sum += stuff
                break

    print('#{} {}'.format(test + 1, stuff_sum))
