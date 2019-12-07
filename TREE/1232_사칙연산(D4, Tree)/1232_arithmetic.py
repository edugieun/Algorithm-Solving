import sys
sys.stdin = open('input.txt', 'r')


def preorder(node):
    global child
    # if isinstance(child[node], list) and isinstance(child[child[node][1]], int) and isinstance(child[child[node][2]], int):
    #     child[node] = child[child[node][1]] + child[child[node][2]]
    #     return

    if isinstance(child[node], list):
        preorder(child[node][1])
        preorder(child[node][2])
        if child[node][0] == '+':
            child[node] = child[child[node][1]] + child[child[node][2]]
        elif child[node][0] == '-':
            child[node] = child[child[node][1]] - child[child[node][2]]
        elif child[node][0] == '*':
            child[node] = child[child[node][1]] * child[child[node][2]]
        elif child[node][0] == '/':
            child[node] = child[child[node][1]] / child[child[node][2]]




for test in range(10):

    N = int(input())
    child = [0 for i in range(N+1)]
    for i in range(N):
        node = list(map(str, input().split()))
        if len(node) == 4:
            child[int(node[0])] = [node[1], int(node[2]), int(node[3])]
        else:
            child[int(node[0])] = int(node[1])

    preorder(1)
    print('#{} {}'.format(test + 1, int(child[1])))



    # 단, 중간 과정에서의 연산은 실수 연산으로 하되,
    # 최종 결과값이 정수로 떨어지지 않으면 정수부만 출력한다.