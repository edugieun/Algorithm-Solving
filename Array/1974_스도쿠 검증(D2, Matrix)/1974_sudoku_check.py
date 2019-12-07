import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N_matrix = [list(map(int, input().split())) for i in range(9)]

    # 가로,세로 검사
    error = 0
    for row in range(9):
        if error == 1:
            break
        check_ho = []
        check_ve = []
        for col in range(9):
            if N_matrix[row][col] in check_ho or N_matrix[col][row] in check_ve:
                error = 1
                break
            else:
                check_ho.append(N_matrix[row][col])
                check_ve.append(N_matrix[col][row])

    # 사각형 검사
    if error == 0:
        for row in range(0, 9, 3):
            if error == 1:
                break
            for col in range(0, 9, 3):
                if error == 1:
                    break
                check_box = []
                for row_check in range(row, row + 3):
                    if error == 1:
                        break
                    for col_check in range(col, col + 3):
                        if N_matrix[row_check][col_check] in check_box:
                            error = 1
                            break
                        else:
                            check_box.append(N_matrix[row_check][col_check])

    print('#{} {}'.format(test + 1, int(not error)))

