import sys
sys.stdin = open('input.txt', 'r')


def dfs():
    global prob_max, prob_tmp, visited, row

    if len(visited) == person:
        prob_max = prob_tmp
        return None

    for col in range(person):
        if col not in visited and N_matrix[row][col] != 0:
            visited.append(col)
            if (prob_tmp * N_matrix[row][col] / 100) < prob_max:
                visited.pop()
                continue
            prob_tmp *= N_matrix[row][col] / 100
            row += 1
            dfs()
            row -= 1
            prob_tmp /= N_matrix[row][col] / 100
            visited.pop()




test_case = int(input())

for test in range(test_case):
    person = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(person)]

    # Initialization
    visited = []
    row = 0
    prob_max = 1
    prob_tmp = 1
    for i in range(person):
        prob_max *= N_matrix[i][i] / 100

    dfs()
    print('#{} {:.6f}'.format(test+1, round(prob_max*100, 6)))
