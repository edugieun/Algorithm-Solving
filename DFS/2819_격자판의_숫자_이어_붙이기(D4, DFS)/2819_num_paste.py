import sys
sys.stdin = open('sample_input.txt', 'r')


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(row, col, make_string):
    global num_list
    if len(make_string) == 7:
        num_list.add(make_string)
        return

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if 0 <= new_col < 4 and 0 <= new_row < 4:
            dfs(new_row, new_col, make_string + str(N_matrix[new_row][new_col]))


testcase = int(input())

for test in range(testcase):
    N_matrix = [list(map(int, input().split())) for i in range(4)]

    num_list = set()
    for row in range(4):
        for col in range(4):
            dfs(row, col, str(N_matrix[row][col]))
    print('#{} {}'.format(test + 1, len(num_list)))
