import sys
sys.stdin = open('bomber1_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N = int(input())

    N_matrix = [list(map(int, input().split())) for i in range(N)]

    max_sum = 0
    for idx, order in enumerate(N_matrix):
        order_sum = sum(order)
        for col in range(N):
            tmp_sum = 0
            for row in range(N):
                tmp_sum += N_matrix[row][col]
            kill = (order_sum + tmp_sum) - N_matrix[idx][col]
            if max_sum < kill:
                max_sum = kill

    print(max_sum)