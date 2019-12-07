import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())
for test in range(test_case):
    N, hex_num = map(str, input().split())
    print('#{}'.format(test + 1), end=' ')
    print('{0:b}'.format(int(hex_num, 16)).zfill(4*int(N)))

