import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def prim(start):
    Q = deque()
    Q.append(start)
    D[0] = 0
    while Q:
        node_1 = Q.popleft()
        for node_2 in graph[node_1]:

testcase = int(input())

for test in range(testcase):
    N, E = map(int, input().split())

    graph = [[] for i in range(N + 1)]
    for i in range(E):
        node_1, node_2, w = map(int, input().split())
        graph[node_1].append((node_2, w))

    D = [0xffffffff] * (N + 1)
    prim(0)