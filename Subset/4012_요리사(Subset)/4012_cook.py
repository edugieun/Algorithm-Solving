import sys
sys.stdin = open('input.txt', 'r')

# subset
def subset(arr):
    min_dif = 99999999
    for selection in range(int((1 << N)/2)):
        group_a = []
        group_b = []
        for compare in range(N):
            if selection & (1 << compare):
                group_a.append(compare)
            else:
                group_b.append(compare)
        if len(group_a) == N/2:
            taste_dif = abs(synergy(group_a) - synergy(group_b))
            if taste_dif < min_dif:
                min_dif = taste_dif
    return min_dif

def synergy(arr):
    taste = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            taste = taste + N_matrix[arr[i]][arr[j]] + N_matrix[arr[j]][arr[i]]
    return taste

testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_arr = [i for i in range(N)]
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    print('#{} {}'.format(test+1, subset(N_arr)))