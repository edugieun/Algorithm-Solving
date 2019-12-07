import sys
sys.stdin = open('input.txt', 'r')


def BFS(num):
    global cnt
    if visit[num]:
        return
    visit[num] = True
    Q = []
    Q.append(num)
    while Q:
        now_num = Q.pop()
        for next_num in node[now_num]:
            if not visit[next_num]:
                visit[next_num] = True
                Q.append(next_num)
    cnt += 1

testcase = int(input())

for test in range(testcase):
    N, M = map(int, input().split())
    node = [set() for i in range(N + 1)]
    info = list(map(int, input().split()))
    for i in range(M):
        node[info[2 * i]].add(info[2 * i + 1])
        node[info[2 * i + 1]].add(info[2 * i])

    visit = [False] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        BFS(i)
    print('#{} {}'.format(test + 1, cnt))

