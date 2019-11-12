import sys
sys.stdin = open('sample_input.txt', 'r')

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)


test_case = int(input())

for test in range(test_case):

    N = int(input())

    # 조합 combination 변수
    n = N // 10

    result = 0
    for r in range(0, (N // 20) + 1):
        result += (factorial(n - r) // (factorial(r) * factorial(n - r - r))) * 2 ** r

    print('#{} {}'.format(test+1, result))
