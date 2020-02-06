import sys
sys.stdin = open('input.txt', 'r')

def combination(com_arr, start, left_enermies):
    if len(com_arr) == R:
        targets = []
        for arrow in com_arr:
            dis_min = 9999999
            for i in range(len(left_enermies)):
                dis_row = N+1 - left_enermies[i][0]
                dis_col = abs(left_enermies[i][1] - arrow)
                dis = dis_row + dis_col
                if dis <= D:
                    if dis < dis_min:

                    elif dis == dis_min:

        print()


    else:
        for i in range(start, N):
            combination(com_arr + [N_arr[i]], i + 1, left_enermies)


N, M, D = map(int, input().split())
R = 3
N_matrix = [list(map(int, input().split())) for i in range(N)]
N_arr = [i for i in range(N)]
enermies = []
for row in range(N):
    for col in range(M):
        if N_matrix[row][col] == 1:
            enermies.append([row, col])
combination([], 0, enermies)
print(enermies)
