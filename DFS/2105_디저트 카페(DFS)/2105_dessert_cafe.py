import sys
sys.stdin = open('input.txt', 'r')

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]


def dfs(row, col, direction, depth):
    global max_dessert
    if row == s_row and col == s_col and direction == 3:
        if dessert_sort[N_matrix[row][col]] and depth > max_dessert:
            max_dessert = depth
        return
    new_row = row + dy[direction]
    new_col = col + dx[direction]
    if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N: return
    if dessert_sort[N_matrix[new_row][new_col]]: return
    dessert_sort[N_matrix[new_row][new_col]] = True
    dfs(new_row, new_col, direction, depth + 1)
    if direction < 3:
        dfs(new_row, new_col, direction + 1, depth + 1)
    dessert_sort[N_matrix[new_row][new_col]] = False

testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    dessert_sort = [False for i in range(101)]

    max_dessert = -1
    for s_row in range(N):
        for s_col in range(N):
            dfs(s_row, s_col, 0, 0)
    print('#{} {}'.format(test + 1, max_dessert))