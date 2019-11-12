# bfs 사용법 익히기

import sys, pprint
sys.stdin = open('input.txt', 'r')

def bfs(S, r_list):
    global visited, cnt
    cnt += 1
    queue = []
    queue.append(S)
    visited.append(S)
    while queue:
        ele_idx = queue.pop(0)
        for ele in r_list[ele_idx]:
            if ele not in visited:
                visited.append(ele)
                queue.append(ele)



testcase = int(input())

for test in range(testcase):
    N, M = map(int, input().split())

    r_list = [[] for i in range(N + 1)]

    for i in range(M):
        node = list(map(int, input().split()))
        r_list[node[0]].append(node[1])
        r_list[node[1]].append(node[0])

    cnt = 0
    visited = []
    for i in range(1, N + 1):
        if i not in visited:
            bfs(i, r_list)

    print('#{} {}'.format(test + 1, cnt))
