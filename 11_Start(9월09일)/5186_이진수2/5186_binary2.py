import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    F = float(input())
    result = ''
    while F != 0:
        a = (F * 2) // 1
        F = (F * 2) % 1
        result += str(int(a))

    if len(result) >= 13:
        result = 'overflow'
    print('#{} {}'.format(test+1, result))