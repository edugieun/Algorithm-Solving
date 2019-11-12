import sys, time
sys.stdin = open('input.txt', 'r')

start = time.time()


def shark_change():

    # 위치 변경
    for shark_num in sharks.keys():
        # 위
        if sharks[shark_num][3] == 1:
            sharks[shark_num][2] = sharks[shark_num][2] % (2 * R - 2)
            sharks[shark_num][0] -= sharks[shark_num][2]
            while sharks[shark_num][0] <= 0 or sharks[shark_num][0] > R:
                if sharks[shark_num][3] == 1:
                    sharks[shark_num][0] = sharks[shark_num][0] * (-1) + 2
                    sharks[shark_num][3] = 2
                elif sharks[shark_num][3] == 2:
                    sharks[shark_num][0] = R - (sharks[shark_num][0] - R)
                    sharks[shark_num][3] = 1
        # 아래
        elif sharks[shark_num][3] == 2:
            sharks[shark_num][2] = sharks[shark_num][2] % (2 * R - 2)
            sharks[shark_num][0] += sharks[shark_num][2]
            while sharks[shark_num][0] <= 0 or sharks[shark_num][0] > R:
                if sharks[shark_num][3] == 1:
                    sharks[shark_num][0] = sharks[shark_num][0] * (-1) + 2
                    sharks[shark_num][3] = 2
                elif sharks[shark_num][3] == 2:
                    sharks[shark_num][0] = R - (sharks[shark_num][0] - R)
                    sharks[shark_num][3] = 1
        # 오른쪽
        elif sharks[shark_num][3] == 3:
            sharks[shark_num][2] = sharks[shark_num][2] % (2 * C - 2)
            sharks[shark_num][1] += sharks[shark_num][2]
            while sharks[shark_num][1] > C or sharks[shark_num][1] <= 0:
                if sharks[shark_num][3] == 3:
                    sharks[shark_num][1] = C - (sharks[shark_num][1] - C)
                    sharks[shark_num][3] = 4
                elif sharks[shark_num][3] == 4:
                    sharks[shark_num][1] = sharks[shark_num][1] * (-1) + 2
                    sharks[shark_num][3] = 3
        # 왼쪽
        elif sharks[shark_num][3] == 4:
            sharks[shark_num][2] = sharks[shark_num][2] % (2 * C - 2)
            sharks[shark_num][1] -= sharks[shark_num][2]
            while sharks[shark_num][1] > C or sharks[shark_num][1] <= 0:
                if sharks[shark_num][3] == 3:
                    sharks[shark_num][1] = C - (sharks[shark_num][1] - C)
                    sharks[shark_num][3] = 4
                elif sharks[shark_num][3] == 4:
                    sharks[shark_num][1] = sharks[shark_num][1] * (-1) + 2
                    sharks[shark_num][3] = 3

    N_matrix = [[0] * (C + 1) for i in range(R + 1)]

    # 동족 상잔
    # 시간 초과 해결 방법:
    # 상어가 10000마리 일 때 상어끼리 비교하기 위해, 10000*10000번을 읽는 것이 아니라 /
    # 딱 상어 10000번만 읽되, matrix를 이용하여 겹치는 자리를 처리한다.
    dead_shark = []
    for shark_num in sharks.keys():
        if N_matrix[sharks[shark_num][0]][sharks[shark_num][1]] == 0:
            N_matrix[sharks[shark_num][0]][sharks[shark_num][1]] = shark_num
        elif N_matrix[sharks[shark_num][0]][sharks[shark_num][1]] != shark_num:
            if sharks[N_matrix[sharks[shark_num][0]][sharks[shark_num][1]]][4] < sharks[shark_num][4]:
                dead_shark.append(N_matrix[sharks[shark_num][0]][sharks[shark_num][1]])
                N_matrix[sharks[shark_num][0]][sharks[shark_num][1]] = shark_num
            else:
                dead_shark.append(shark_num)


    for shark_num in dead_shark:
        del sharks[shark_num]


R, C, M = map(int, input().split())

sharks = {}
for i in range(M):
    sharks['s' + str(i)] = list(map(int, input().split()))
shark_sum = 0
for person_pos in range(1, C + 1):
    # 낚시
    get_shark_row = 99999

    for shark_num in sharks.keys():
        if sharks[shark_num][1] == person_pos and sharks[shark_num][0] < get_shark_row:
            get_shark = shark_num
            get_shark_row = sharks[get_shark][0]

    if get_shark_row != 99999:
        shark_sum += sharks[get_shark][4]
        del sharks[get_shark]

    # 상어 위치 변경 및 동족상잔
    shark_change()

print(shark_sum)

print(time.time() - start)

# 시간초과
# def shark_change():
#
#     # 위치 변경
#     for shark_num in sharks.keys():
#         # 위
#         if sharks[shark_num][3] == 1:
#             sharks[shark_num][2] = sharks[shark_num][2] % (2 * R - 2)
#             sharks[shark_num][0] -= sharks[shark_num][2]
#             while sharks[shark_num][0] <= 0 or sharks[shark_num][0] > R:
#                 if sharks[shark_num][3] == 1:
#                     sharks[shark_num][0] = sharks[shark_num][0] * (-1) + 2
#                     sharks[shark_num][3] = 2
#                 elif sharks[shark_num][3] == 2:
#                     sharks[shark_num][0] = R - (sharks[shark_num][0] - R)
#                     sharks[shark_num][3] = 1
#         # 아래
#         elif sharks[shark_num][3] == 2:
#             sharks[shark_num][2] = sharks[shark_num][2] % (2 * R - 2)
#             sharks[shark_num][0] += sharks[shark_num][2]
#             while sharks[shark_num][0] <= 0 or sharks[shark_num][0] > R:
#                 if sharks[shark_num][3] == 1:
#                     sharks[shark_num][0] = sharks[shark_num][0] * (-1) + 2
#                     sharks[shark_num][3] = 2
#                 elif sharks[shark_num][3] == 2:
#                     sharks[shark_num][0] = R - (sharks[shark_num][0] - R)
#                     sharks[shark_num][3] = 1
#         # 오른쪽
#         elif sharks[shark_num][3] == 3:
#             sharks[shark_num][2] = sharks[shark_num][2] % (2 * C - 2)
#             sharks[shark_num][1] += sharks[shark_num][2]
#             while sharks[shark_num][1] > C or sharks[shark_num][1] <= 0:
#                 if sharks[shark_num][3] == 3:
#                     sharks[shark_num][1] = C - (sharks[shark_num][1] - C)
#                     sharks[shark_num][3] = 4
#                 elif sharks[shark_num][3] == 4:
#                     sharks[shark_num][1] = sharks[shark_num][1] * (-1) + 2
#                     sharks[shark_num][3] = 3
#         # 왼쪽
#         elif sharks[shark_num][3] == 4:
#             sharks[shark_num][2] = sharks[shark_num][2] % (2 * C - 2)
#             sharks[shark_num][1] -= sharks[shark_num][2]
#             while sharks[shark_num][1] > C or sharks[shark_num][1] <= 0:
#                 if sharks[shark_num][3] == 3:
#                     sharks[shark_num][1] = C - (sharks[shark_num][1] - C)
#                     sharks[shark_num][3] = 4
#                 elif sharks[shark_num][3] == 4:
#                     sharks[shark_num][1] = sharks[shark_num][1] * (-1) + 2
#                     sharks[shark_num][3] = 3
#
#     #동족 상잔
#     dead_shark = []
#     for shark_num in sharks.keys():
#         if shark_num not in dead_shark:
#             for shark_num_next in sharks.keys():
#                 if shark_num_next not in dead_shark and shark_num != shark_num_next and sharks[shark_num][0] == sharks[shark_num_next][0] and sharks[shark_num][1] == sharks[shark_num_next][1]:
#                     if sharks[shark_num][4] > sharks[shark_num_next][4]:
#                         dead_shark.append(shark_num_next)
#                     elif sharks[shark_num][4] < sharks[shark_num_next][4]:
#                         dead_shark.append(shark_num)
#     for shark_num in dead_shark:
#         del sharks[shark_num]
#
# R, C, M = map(int, input().split())
#
# sharks = {}
# for i in range(M):
#     sharks['s' + str(i)] = list(map(int, input().split()))
#
# shark_sum = 0
# for person_pos in range(1, C + 1):
#     # 낚시
#     get_shark_row = 99999
#
#     for shark_num in sharks.keys():
#         if sharks[shark_num][1] == person_pos and sharks[shark_num][0] < get_shark_row:
#             get_shark = shark_num
#             get_shark_row = sharks[get_shark][0]
#
#     if get_shark_row != 99999:
#         shark_sum += sharks[get_shark][4]
#         del sharks[get_shark]
#
#     # 상어 위치 변경 및 동족상잔
#     shark_change()
#
#
# print(shark_sum)