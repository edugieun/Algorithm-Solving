import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def BFS(sangwon):
    global cnt
    visit[sangwon] = True
    Q = deque()
    Q.append(sangwon)
    depth = [0] * (N + 1)
    while Q:
        person_1 = Q.popleft()
        if depth[person_1] == 2:
            continue
        for person_2 in people[person_1]:
            if not visit[person_2]:
                visit[person_2] = True
                Q.append(person_2)
                depth[person_2] = depth[person_1] + 1
                cnt += 1

testcase = int(input())

for test in range(testcase):
    N, M = map(int, input().split())
    people = [[] for i in range(N + 1)]

    for i in range(M):
        person_1, person_2 = map(int, input().split())
        people[person_1].append(person_2)
        people[person_2].append(person_1)

    visit = [False] * (N + 1)
    cnt = 0
    BFS(1)
    print('#{} {}'.format(test + 1, cnt))
