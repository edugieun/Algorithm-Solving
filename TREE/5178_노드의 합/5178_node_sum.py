import sys
sys.stdin = open('sample_input.txt', 'r')

testcase = int(input())

for test in range(testcase):
    N, M, L = map(int, input().split())
    tree = [0 for i in range(N+1)]
    for i in range(M):
        node = list(map(int, input().split()))
        tree[node[0]] = node[1]

    for i in range(N, 1, -1):
        if i % 2 == 0:
            if i == N:
                tree[i//2] = tree[i]
            else:
                tree[i//2] = tree[i] + tree[i+1]

    print('#{} {}'.format(test + 1, tree[L]))