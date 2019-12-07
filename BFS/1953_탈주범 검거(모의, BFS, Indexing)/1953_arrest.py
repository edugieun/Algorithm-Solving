import sys
sys.stdin = open('input.txt', 'r')

# Indexing
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
now_out_possible = [[1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6], [1, 3, 6, 7]]
new_in_possible = [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]]

# BFS
def bfs(start_row, start_col):
    Q = []
    visit[start_row][start_col] += 1
    cnt = 1
    Q.append((start_row, start_col))
    while Q:
        now_row, now_col = Q.pop(0)
        if visit[now_row][now_col] >= L:
            continue
        for i in range(4):
            new_row = now_row + dy[i]
            new_col = now_col + dx[i]
            if 0 <= new_row < N and 0 <= new_col < M:
                if NM_matrix[now_row][now_col] in now_out_possible[i] and NM_matrix[new_row][new_col] in new_in_possible[i]:
                    if not visit[new_row][new_col]:
                        Q.append((new_row, new_col))
                        visit[new_row][new_col] = visit[now_row][now_col] + 1
                        cnt += 1
    return cnt

testcase = int(input())

for test in range(testcase):
    N, M, R, C, L = map(int, input().split())
    NM_matrix = [list(map(int, input().split())) for i in range(N)]

    visit = [[0] * M for i in range(N)]
    print('#{} {}'.format(test+1, dfs(R, C)))
