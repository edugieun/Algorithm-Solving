
import sys
sys.stdin = open('sample_input.txt', 'r')

def recursion(row):
    global tmp_sum, min_sum

    # 실행 시간을 줄이기 위해 중간 덧셈 과정에서 이미 min_sum 값을 넘어버리면 재귀를 바로 나온다.
    if tmp_sum >= min_sum:
        return

    if row == N:
        if tmp_sum < min_sum:
            min_sum = tmp_sum
        return

    for col in range(N):
        if col not in visited:
            visited.append(col)
            tmp_sum += N_matrix[row][col]
            new_row = row + 1
            recursion(new_row)
            tmp_sum -= N_matrix[row][col]
            visited.pop(-1)

test_case = int(input())
for test in range(test_case):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]

    visited = []
    min_sum = 0
    for i in range(N):
        min_sum += N_matrix[i][i]
    tmp_sum = 0
    row = 0
    recursion(row)
    print('#{} {}'.format(test+1, min_sum))


# # 시간 초과
# import sys, time
# sys.stdin = open('sample_input.txt', 'r')
#
# start = time.time()
#
# def recursion(row, tmp_sum):
#     for col in range(N):
#         if col not in visited:
#             visited.append(col)
#             new_tmp_sum = tmp_sum + N_matrix[row][col]
#             if len(visited) == N:
#                 sum_list.append(new_tmp_sum)
#                 visited.pop(-1)
#                 break
#             new_row = row + 1
#             if new_row < N:
#                 recursion(new_row, new_tmp_sum)
#     if len(visited):
#         visited.pop(-1)
#     return None
#
#
#
# test_case = int(input())
# for test in range(test_case):
#     N = int(input())
#     N_matrix = [list(map(int, input().split())) for i in range(N)]
#
#     visited = []
#     sum_list = []
#     tmp_sum = 0
#     row = 0
#     recursion(row, tmp_sum)
#     print('#{} {}'.format(test+1, min(sum_list)))
# print('time : {}'.format(time.time() - start))
