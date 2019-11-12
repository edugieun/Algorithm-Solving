import sys
import copy
sys.stdin = open('sample_input.txt', 'r')


def convert(num, con_num):
    sum_tmp = 0
    for i in range(len(num)):
        sum_tmp += num[len(num) - 1 - i] * (con_num**i)
    return sum_tmp

test_case = int(input())

for test in range(test_case):

    bi_num = list(map(int, input()))
    tri_num = list(map(int, input()))

    try:
        for i in range(len(bi_num)):
            bi_num_tmp = copy.deepcopy(bi_num)
            bi_num_tmp[i] = int(not bi_num_tmp[i])
            for j in range(len(tri_num)):
                tri_num_tmp = copy.deepcopy(tri_num)
                for k in range(3):
                    tri_num_tmp[j] = k
                    a = convert(bi_num_tmp, 2)
                    b = convert(tri_num_tmp, 3)

                    if a == b:
                        raise ValueError
    except ValueError:
        print('#{} {}'.format(test+1, a))

