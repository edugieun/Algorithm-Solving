import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    para = input()

    for i in range(len(para)):
        a = para[:i+1]
        b = para[i+1:2*i+2]
        if len(a) != 0 and a == b:
            break
    print('#{} {}'.format(test+1, len(a)))