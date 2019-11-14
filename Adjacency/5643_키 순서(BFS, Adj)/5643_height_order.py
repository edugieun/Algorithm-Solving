import sys
sys.stdin = open('input.txt', 'r')

# bfs
def bfs(person, adj_type):
    global visited
    Q = []
    per_cnt = 0
    Q.append(person)
    while Q:
        per_idx = Q.pop(0)
        for nxt_per in adj_type[per_idx]:
            if not visited[nxt_per]:
                visited[nxt_per] = True
                per_cnt += 1
                Q.append(nxt_per)
    return per_cnt


testcase = int(input())

for test in range(testcase):
    N = int(input())
    M = int(input())

    # adjacency list & reverse adjacency list
    adj_list = [[] for i in range(N+1)]
    re_adj_list = [[] for i in range(N + 1)]
    for i in range(M):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        re_adj_list[e].append(s)

    cnt = 0
    for person in range(1, N+1):
        visited = [False] * (N + 1)
        result = bfs(person, adj_list) + bfs(person, re_adj_list) + 1
        if result == N:
            cnt += 1

    print('#{} {}'.format(test+1, cnt))