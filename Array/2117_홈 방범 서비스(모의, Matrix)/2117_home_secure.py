import sys
sys.stdin = open('input.txt', 'r')

def area_define(row, col, K):
    global max_house
    house_cnt = 0
    x_dis = -1
    for y_area in range(row - K + 1, row + K):
        if y_area <= row:
            x_dis += 1
            if 0 <= y_area < N:
                for x_area in range(col - x_dis, col + x_dis + 1):
                    if 0 <= x_area < N and N_matrix[y_area][x_area] == 1:
                        house_cnt += 1
            else:
                continue
        else:
            x_dis -= 1
            if 0 <= y_area < N:
                for x_area in range(col - x_dis, col + x_dis + 1):
                    if 0 <= x_area < N and N_matrix[y_area][x_area] == 1:
                        house_cnt += 1

    income = (house_cnt * M) - ((K * K) + (K - 1) * (K - 1))
    if income >= 0 and house_cnt > max_house:
        max_house = house_cnt

testcase = int(input())

for test in range(testcase):
    N, M = map(int, input().split())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    max_house = 0
    for row in range(N):
        for col in range(N):
            for K in range(1, N + (N - 1)): # K범위 이거 아님. 더 커야함. 사각형을 덮기위한 마름모의 최소 크기는 어떻게 정할까.
                area_define(row, col, K)
    print('#{} {}'.format(test + 1, max_house))


# def solve():
#     ans = 0
#     for k in range(N+1, 0, -1):
#         for x in range(N):
#             for y in range(N):
#                 tans = 0
#                 for xx, yy in q:
#                     if abs(x - xx) + abs(y - yy) < k:
#                         tans += 1
#                 if cost[k] <= tans * M and ans < tans: # 손해가 아니고 집의 수가 최대인 경우 최대값 계산
#                     ans + tans
#         if ans:
#             return ans
#
# cost = [0, 1, 5, 13...]
#
# for tc in range(~):
#     ...;
#
#     q = []
#     for i in range(N):
#         for j in range(N):
#             if mat[i][j]:
#                 q.append((i, j))
#
#     print(solve())
