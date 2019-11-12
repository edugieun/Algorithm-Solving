"""
i =     0   1   2   3       4       5       6       7       8       9
idx =   0   -1  1   -2      2       -3      3       -4      4       -5
diff =  i   -i  i-1 -(i-1)  (i-2)   -(i-2)  (i-3)   -(i-3)  (i-4)   -(i-4)
x??
"""

import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for test in range(test_case):
    N = int(input()) # 정수의 개수
    N_list = sorted(list(map(int, input().split())), reverse=True)

    change = 0
    x = 0
    new_list = []
    for i in range(10): # 10개 까지만
        if change == 0:
            new_list.append(N_list[(i-x)])
            change = 1

        elif change == 1:
            new_list.append(N_list[-(i-x)])
            change = 0
            x += 1
    print(new_list)
    new_list = list(map(str, new_list))
    print('#{} {}'.format(test + 1, ' '.join(new_list)))

