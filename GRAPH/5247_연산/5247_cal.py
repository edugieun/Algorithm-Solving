import sys
from collections import deque
from time import time
sys.stdin = open('input.txt', 'r')

def BFS(start):
    visit[start] = True
    Q = deque() # Q = [] 에 append, pop 하는 것보다 deque의 append, popleft 가 큰 차이는 아니나, 약간 더 빠름 
    Q.append(start)
    depth[start] = 0
    while Q:
        now_num = Q.popleft()
        for oper in range(4): # 처음에는 수식 문자열 eval 사용했는데 느림(지속적인 함수 호출로 인해).
            if oper == 0:
                tmp = now_num + 1
                if 0 < tmp <= 1000000 and not visit[tmp]:
                    visit[tmp] = True
                    Q.append(tmp)
                    depth[tmp] = depth[now_num] + 1
                    if tmp == M:
                        return depth[tmp]
            elif oper == 1:
                tmp = now_num - 1
                if 0 < tmp <= 1000000 and not visit[tmp]:
                    visit[tmp] = True
                    Q.append(tmp)
                    depth[tmp] = depth[now_num] + 1
                    if tmp == M:
                        return depth[tmp]
            elif oper == 2:
                tmp = now_num * 2
                if 0 < tmp <= 1000000 and not visit[tmp]:
                    visit[tmp] = True
                    Q.append(tmp)
                    depth[tmp] = depth[now_num] + 1
                    if tmp == M:
                        return depth[tmp]
            elif oper == 3:
                tmp = now_num - 10
                if 0 < tmp <= 1000000 and not visit[tmp]:
                    visit[tmp] = True
                    Q.append(tmp)
                    depth[tmp] = depth[now_num] + 1
                    if tmp == M:
                        return depth[tmp]

testcase = int(input())

for test in range(testcase):
    N, M = map(int, input().split())

    visit = [False] * 1000001 # 처음에는 빈리스트 형성 후 visit.append로 했는데 엄청난 시간이 필요.
    depth = [0xffffffff] * 1000001
    result = BFS(N)
    print('#{} {}'.format(test + 1, result))

