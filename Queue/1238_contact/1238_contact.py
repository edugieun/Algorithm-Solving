import sys
sys.stdin = open('input.txt', 'r')


def bfs(start_node):
    visited = []
    Q = []
    distance = [0] * 101
    Q.append(start_node)

    while Q:
        start_node = Q.pop(0)
        if start_node in adj_lists:
            for next_node in adj_lists[start_node]:
                if next_node not in visited:
                    visited.append(next_node)
                    Q.append(next_node)
                    # visited에는 없지만 Q스택에 겹치는 경우가 있어서 중복해서 거리가 누적되는 경우가 있었음.
                    # 아래와같이 조건문으로 처리
                    if distance[next_node] not in Q:
                        distance[next_node] = distance[start_node] + 1

    far_dis = 0
    for i in range(len(distance)):
        if distance[i] >= far_dis:
            far_dis = distance[i]
            number = i
    # while 1:
    #     pass

    return number



test_case = 10
for test in range(test_case):
    N, S = map(int, input().split())
    links = list(map(int, input().split()))
    adj_lists = {}

    for i in range(N//2):
        adj_lists[links[i*2]] = []

    for i in range(N//2):
        adj_lists[links[i * 2]] += [links[i * 2 + 1]]

    print('#{} {}'.format(test+1, bfs(S)))