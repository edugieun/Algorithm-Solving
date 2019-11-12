import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())


def push(pair):
    route.append(pair)

def pop():
    global fail
    if len(route) == 0:
        fail = 1
        return None
    route.pop()


for test in range(test_case):
    V, E = map(int, input().split())

    between_node = [list(map(int, input().split())) for i in range(E)]

    S, G = map(int, input().split())


    route = []
    find = 0
    fail = 0
    while fail != 1 and find != 1:
        for node in between_node:
            if len(route) == 0 and node[0] == S:
                push(node)
                node[0] = 0
                break

            if len(route) != 0 and node[0] == route[-1][-1]:
                push(node)
                node[0] = 0
                break
        else:
            if len(route) != 0 and route[-1][-1] == G:
                find = 1
            pop()

    if find == 1:
        print('#{} 1'.format(test + 1))
    else:
        print('#{} 0'.format(test + 1))
