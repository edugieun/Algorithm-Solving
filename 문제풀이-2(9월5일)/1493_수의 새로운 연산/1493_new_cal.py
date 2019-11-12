import sys
import time
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    p, q =map(int, input().split())





# N = 301
#
# N_matrix = [[0] * N for i in range(N)]
#
# cnt = 0
# for i in range(1, N):
#     for j in range(1, i + 1):
#         cnt += 1
#         N_matrix[i+1 - j][j] = cnt
#
# test_case = int(input())
# for test in range(test_case):
#
#     p, q = map(int, input().split())
#
#     cnt = 0
#     for row in range(N):
#         if cnt == 2:
#             break
#
#         if p in N_matrix[row]:
#             col1 = N_matrix[row].index(p)
#             row1 = row
#             cnt += 1
#
#         if q in N_matrix[row]:
#             col2 = N_matrix[row].index(q)
#             row2 = row
#             cnt += 1
#
#     print('#{} {}'.format(test + 1, N_matrix[row1 + row2][col1 + col2]))


