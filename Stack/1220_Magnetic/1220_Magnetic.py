import sys
sys.stdin = open('input.txt', 'r')


def dead_lock(row, col):
    global N_matrix, status, cnt
    for d_row in range(row, N):
        if status == 1 and N_matrix[d_row][col] == 2:
            cnt += 1
            status = 2
        elif status == 2 and N_matrix[d_row][col] == 1:
            status = 1


for test in range(10):

    N = int(input())

    N_matrix = [list(map(int, input().split())) for i in range(N)]

    cnt = 0
    for col in range(N):
        for row in range(N):
            if N_matrix[row][col] == 1:
                status = 1
                dead_lock(row, col)
                break

    print('#{} {}'.format(test + 1, cnt))


### 강사님 코드

for tc i n range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    a = 0
    for i in range(n):
        c = 0
        for j in range(n):
            if arr[j][i] == 1:
                c = 1
            if arr[j][i] == 2 and c == 1:
                c = 0
                a += 1
    print('#%d %d'%(tc, a))