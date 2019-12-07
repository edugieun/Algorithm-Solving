import sys
sys.stdin = open('input.txt', 'r')


def dfs(x, y, tmp_sum):
    global visited, min_sum
    if tmp_sum >= min_sum:
        return
    if len(visited) == N:
        tmp_sum += abs(x-home[0]) + abs(y-home[1])
        if tmp_sum < min_sum:
            min_sum = tmp_sum
        tmp_sum -= abs(x - home[0]) + abs(y - home[1])
        return

    for order in range(N):
        if order not in visited:
            visited.append(order)
            new_x = point_list[order][0]
            new_y = point_list[order][1]
            tmp_sum += abs(new_x - x) + abs(new_y - y)
            dfs(new_x, new_y, tmp_sum)
            tmp_sum -= abs(new_x - x) + abs(new_y - y)
            visited.pop()


testcase = int(input())

for test in range(testcase):
    N = int(input())
    tmp_point_list = list(map(int, input().split()))
    company = [tmp_point_list[0], tmp_point_list[1]]
    home = [tmp_point_list[2], tmp_point_list[3]]
    point_list = []
    for i in range(2, N + 2):
        point_list.append([tmp_point_list[i * 2], tmp_point_list[i * 2 + 1]])

    visited = []
    min_sum = 9999999

    dfs(company[0], company[1], 0)
    print('#{} {}'.format(test+1, min_sum))
