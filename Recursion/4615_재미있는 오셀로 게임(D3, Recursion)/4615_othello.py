import sys
from pprint import pprint
sys.stdin = open('sample_input.txt', 'r')

# 8방향 탐색 변수
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def othello_func(row, col, direc_dy, direc_dx, color):
    global N_matrix, find
    # 3. 진행중인 방향으로 한칸 더 이동
    new_row = row + direc_dy
    new_col = col + direc_dx

    find = 0
    # 4-1. 한칸 더 이동한(총 2칸 이동) 곳이, 0이 아닐 경우
    if 0 <= new_row < N and 0 <= new_col < N and N_matrix[new_row][new_col] != 0:
        # 놓은 돌과 같은 색이면 오셀로 조건 만족 find = 1
        if N_matrix[new_row][new_col] == color:
            find = 1
            # 불러온(최종 목적지의 한칸 전) 곳의 색을 변환
            N_matrix[row][col] = color
            return None
        else:
            # 4-2. 여전히 놓은 돌과 다른 색이면 재귀함수 호출
            othello_func(new_row, new_col, direc_dy, direc_dx, color)
    # 5. 오셀로 조건 만족시 거꾸로 돌아가면서 한번 더 색 변경
    if find == 1:
        N_matrix[row][col] = color


test_case = int(input())

for test in range(test_case):
    N, M = map(int, input().split())

    # 1. 오셀로 경기판 초기 설정
    N_matrix = [[0]*N for i in range(N)]
    init = 1
    for row in range(N//2 - 1, N//2 + 1):
        if init == 2:
            init = 1
        else:
            init = 2
        for col in range(N//2 - 1, N//2 + 1):
            N_matrix[row][col] = init
            if init == 2:
                init = 1
            else:
                init = 2
    
    # 2. 돌 놓는 좌표 읽은 후 하나씩 불러옴
    put_list = [list(map(int, input().split())) for i in range(M)]
    for put in put_list:
        # put[0] : y좌표, put[1]: x좌표, put[2]: 돌의 색깔
        N_matrix[put[0] - 1][put[1] - 1] = put[2]
        # 8방향 탐색하면서
        for i in range(8):
            row = dy[i] + (put[0] - 1)
            col = dx[i] + (put[1] - 1)
            # 경계조건을 벗어나지 않고, 0이 아니며, 자신이 놓는 돌 색깔과 다른 색일 때 함수 호출
            if 0 <= row < N and 0 <= col < N and N_matrix[row][col] != 0 and N_matrix[row][col] != put[2]:
                # 현재 진행 중인 방향(dy[i], dx[i])을 함수로 가져감
                othello_func(row, col, dy[i], dx[i], put[2])
    w_cnt = 0
    b_cnt = 0
    for row in range(N):
        for col in range(N):
            # 검은 돌 수 확인
            if N_matrix[row][col] == 1:
                b_cnt += 1
            # 흰 돌 수 확인
            elif N_matrix[row][col] == 2:
                w_cnt += 1

    print('#{} {} {}'.format(test+1, b_cnt, w_cnt))
