import sys
sys.stdin = open('sample_input.txt', 'r')

def BFS(start):
    global min_distance
    Q.append(start)
    visited[start] = 1

    while Q:
        start = Q.pop(0)
        for next_node in range(1, V+1):
            if visited[next_node] == 0 and V_matrix[start][next_node] == 1:
                visited[next_node] = 1
                Q.append(next_node)
                distance[next_node] = distance[start] + 1
                if next_node == G:
                    min_distance = distance[next_node]
                    return

test_case = int(input())
for test in range(test_case):
    V, E = list(map(int, input().split()))
    lines = [list(map(int, input().split())) for i in range(E)]
    S, G = list(map(int, input().split()))

    # 인접 행렬
    V_matrix = [[0]*(V+1) for i in range(V+1)]
    for line in lines:
        V_matrix[line[0]][line[1]] = 1
        V_matrix[line[1]][line[0]] = 1

    # 방문 체크, 큐 생성
    visited = [0] * (V+1)
    Q = []
    distance = [0] * (V+1)
    min_distance = 0
    BFS(S)

    print('#{} {}'.format(test+1, min_distance))

