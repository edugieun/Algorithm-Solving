import sys
sys.stdin = open('sample_input.txt', 'r')
sys.setrecursionlimit(2000)

def inorder(node):
    global cnt
    if node != 0:
        cnt += 1
        inorder(child[node][0])
        inorder(child[node][1])

testcase = int(input())

for test in range(testcase):
    E, N = map(int, input().split())

    child = [[0]*2 for i in range(1002)]
    arr = list(map(int, input().split()))
    for i in range(len(arr)//2):
        if child[arr[i*2]][0] == 0:
            child[arr[i*2]][0] = arr[i*2 + 1]
        else:
            child[arr[i*2]][1] = arr[i*2 + 1]

    cnt = 0
    inorder(N)
    print('#{} {}'.format(test + 1, cnt))
