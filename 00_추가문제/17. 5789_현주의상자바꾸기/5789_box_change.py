import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N, Q = map(int, input().split())

    N_list = [0]*N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            N_list[j - 1] = i


    print('#{} {}'.format(test+1, ' '.join(map(str, N_list))))