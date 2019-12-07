import sys
sys.stdin = open('sample_input.txt', 'r')


def check(idx):
    global new_arr
    if (idx // 2) != 0 and new_arr[idx] < new_arr[idx//2]:
        new_arr[idx], new_arr[idx//2] = new_arr[idx//2], new_arr[idx]
        check(idx // 2)

testcase = int(input())

for test in range(testcase):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    new_arr = [0] + [0]*N
    for i in range(1, len(arr)):
        new_arr[i] = arr[i]
        check(i)

    result = 0
    idx = N
    for i in range(N):
        idx = idx // 2
        result += new_arr[idx]
        if idx == 1:
            break


    print('#{} {}'.format(test + 1, result))