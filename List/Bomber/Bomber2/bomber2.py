import sys
sys.stdin = open('bomber2_input.txt', 'r')


test_case = int(input())

for test in range(test_case):
    N = int(input())

    N_matrix = [list(map(int, input().split())) for i in range(N)]

    max_sum = 0
    for row in range(N):
        for col in range(N):
            sum = 0
            
            # 좌상
            row_tmp,col_tmp = row, col
            while (col_tmp != 0) and (row_tmp != 0):
                col_tmp -= 1
                row_tmp -= 1
                sum += N_matrix[row_tmp][col_tmp]

            # 우상
            row_tmp, col_tmp = row, col
            while (row_tmp != 0) and (col_tmp != (N-1)):
                col_tmp += 1
                row_tmp -= 1
                sum += N_matrix[row_tmp][col_tmp]

            # 좌하
            row_tmp, col_tmp = row, col
            while (col_tmp != 0) and (row_tmp != (N-1)):
                col_tmp -= 1
                row_tmp += 1
                sum += N_matrix[row_tmp][col_tmp]

            # 우하
            row_tmp, col_tmp = row, col
            while (col_tmp != (N-1)) and (row_tmp != (N-1)):
                col_tmp += 1
                row_tmp += 1
                sum += N_matrix[row_tmp][col_tmp]

            sum += N_matrix[row][col]
            if sum > max_sum:
                max_sum = sum
    print(max_sum)

