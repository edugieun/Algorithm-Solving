import sys
sys.stdin = open('input.txt', 'r')

direciton = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def DFS(start, now_direct):

    for d_row, d_col in direciton:
        new_row = cores[i][0] + d_row
        new_col = cores[i][1] + d_col

        check_ans = check()

        if check_ans:



testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    max_core = 0
    cores = []
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == 1:
                if row == 0 or row == N-1 or col == 0 or col == N-1:
                    max_core += 1
                else:
                    cores.append((row, col))

    DFS(0)