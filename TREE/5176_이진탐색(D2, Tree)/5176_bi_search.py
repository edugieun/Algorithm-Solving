import sys
sys.stdin = open('sample_input.txt', 'r')


def inorder(node):
    global idx
    if node <= N:
        inorder(2*node)
        t_list[node] = idx
        idx += 1
        inorder(2*node + 1)



testcase = int(input())

for test in range(testcase):
    N = int(input())
    t_list = [0 for i in range(N + 1)]
    idx = 1
    inorder(1)
    print('#{} {} {}'.format(test + 1, t_list[1], t_list[N//2]))