import sys
sys.stdin = open('input.txt', 'r')

def combination(com_arr, start):
    if len(com_arr) == R:
        print(com_arr)
    else:
        for i in range(start, N):
            combination(com_arr + [N_arr[i]], i + 1)


N, M, D = map(int, input().split())
R = 3
N_matrix = [list(map(int, input().split())) for i in range(N)]
N_arr = [i for i in range(N)]
combination([], 0)