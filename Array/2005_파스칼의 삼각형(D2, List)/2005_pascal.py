import sys
sys.stdin = open('input.txt', 'r')


def pascal(order, tmp_prev):
    global tmp
    tmp = []
    if order == 1:
        tmp.append(1)
        return tmp

    tmp.append(1)
    for i in range(len(tmp_prev) - 1):
        tmp.append(tmp_prev[i] + tmp_prev[i + 1])
    tmp.append(1)
    return tmp

test_case = int(input())

for test in range(test_case):

    N = int(input())

    tmp = []
    print('#{}'.format(test + 1))
    for order in range(1, N+1):
        tmp = pascal(order, tmp)
        print(' '.join(list(map(str, tmp))))
