import sys
sys.stdin = open('sample_input.txt', 'r')

testcase = int(input())

for test in range(testcase):
    N = int(input())
    arr = list(map(int, input().split()))

    score_check = [0] * N * 100 + [0]
    score_check[0] = 1
    max_sum = arr[0]
    max_tmp = 0
    for i in arr:
        for j in range(max_sum, 0, -1):
            if score_check[j] != 0:
                score_check[j + i] += 1
                if (j + i) > max_tmp:
                    max_tmp = j + i
        if max_tmp > max_sum:
            max_sum = max_tmp
        score_check[i] += 1

    cnt = 0
    for i in score_check:
        if i != 0:
            cnt += 1
    print('#{} {}'.format(test + 1, cnt))

