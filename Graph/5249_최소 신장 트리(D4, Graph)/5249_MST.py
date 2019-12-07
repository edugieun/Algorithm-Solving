import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(start):
    distance[start] = 0
    cnt = V
    while cnt:
        node_1, MIN = 0, 0xffffffff
        for node in range(V + 1):
            if not visit[node] and MIN > distance[node]:
                node_1, MIN = node, distance[node]
        visit[node_1] = True
        for node_2, weight in graph[node_1]:
            if not visit[node_2] and distance[node_2] > weight:
                distance[node_2] = weight
        cnt -= 1


testcase = int(input())

for test in range(testcase):
    V, E = map(int, input().split())
    graph = [[] for i in range(E)]
    for i in range(E):
        node_1, node_2, weight = map(int, input().split())
        graph[node_1].append((node_2, weight))
        graph[node_2].append((node_1, weight))

    distance = [0xffffffff] * (V + 1)
    visit = [False] * (V + 1)
    dijkstra(0)
    print('#{} {}'.format(test + 1, sum(distance)))