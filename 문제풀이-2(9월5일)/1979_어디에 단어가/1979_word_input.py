import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N, K = map(int, input().split())

    N_matrix = [list(map(int, input().split())) for i in range(N)]

    result_cnt = 0
    
    # 가로 확인
    for row in range(N):
        start = 0
        cnt = 0
        for col in range(N):
            if N_matrix[row][col] == 1:
                start = 1
                cnt += 1
            if start == 1 and N_matrix[row][col] == 0:
                start = 0
                if cnt == K:
                    result_cnt += 1
                cnt = 0
        if cnt == K:
            result_cnt += 1

    # 세로 확인
    for col in range(N):
        start = 0
        cnt = 0
        for row in range(N):
            if N_matrix[row][col] == 1:
                start = 1
                cnt += 1
            if start == 1 and N_matrix[row][col] == 0:
                start = 0
                if cnt == K:
                    result_cnt += 1
                cnt = 0
        if cnt == K:
            result_cnt += 1

    print('#{} {}'.format(test+1, result_cnt))


