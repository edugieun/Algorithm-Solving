import sys
sys.stdin = open('sample_input.txt', 'r')


def M_pick(in_row, in_col, pick_list):
    for pick in range(in_col, in_col + M):
        pick_list.append(N_matrix[in_row][pick])
    return sorted(pick_list, reverse=True)


def honey_amount(honey_list):
    honey_cost_max = 0
    for i in range(len(honey_list)):
        if honey_list[i] <= C:
            honey_cost = honey_list[i] ** 2
            honey_sum = honey_list[i]

        else:
            continue
        for j in range(i + 1, len(honey_list)):
            if honey_sum + honey_list[j] <= C:
                honey_cost += honey_list[j] ** 2
                honey_sum += honey_list[j]
        if honey_cost > honey_cost_max:
            honey_cost_max = honey_cost
    return honey_cost_max




testcase = int(input())

for test in range(testcase):

    N, M, C = map(int, input().split())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    honey_cost_result = 0

    for row in range(N):
        for col in range(N):
            # M 개 선택이 가능할 경우에만 선택하기
            if col <= (N - M) and (col + M) <= N:
                pick_1 = M_pick(row, col, [])
                # 최대 꿀 채취량 알아보기
                honey_1 = honey_amount(pick_1)
            else: break

            for row_2 in range(row, N):
                # 같은 라인일 경우
                if row == row_2:
                    for col_2 in range(col + M, N):
                        # 가능성 확인
                        if col_2 <= (N - M) and (col_2 + M) <= N:
                            pick_2 = M_pick(row_2, col_2, [])
                            # 최대 꿀 채취량 알아보기
                            honey_2 = honey_amount(pick_2)
                            if honey_1 + honey_2 > honey_cost_result:
                                honey_cost_result = honey_1 + honey_2
                        else: break
                # 아닐 경우
                else:
                    for col_2 in range(N):
                        if col_2 <= (N - M) and (col_2 + M) <= N:
                            pick_2 = M_pick(row_2, col_2, [])
                            # 최대 꿀 채취량 알아보기
                            honey_2 = honey_amount(pick_2)
                            if honey_1 + honey_2 > honey_cost_result:
                                honey_cost_result = honey_1 + honey_2
                        else: break

    print('#{} {}'.format(test + 1, honey_cost_result))