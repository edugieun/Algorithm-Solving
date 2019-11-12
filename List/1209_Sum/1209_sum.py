import sys
sys.stdin = open("input.txt", "r")

for test in range(10):
    order = input()
    # 배열의 크기 N x N
    N = 100
    # 빈리스트에 N x N 배열 할당
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    emp_list = []

    # 행 합
    for i in range(N):
        emp_list.append(sum(arr[i]))
    # 열 합
        col_sum = 0
        for j in range(N):
            col_sum += arr[j][i]
        emp_list.append(col_sum)

    # 대각선 합
    diag1_sum = 0
    diag2_sum = 0

    for i in range(N):
        # 대각선 합 1
        diag1_sum += arr[i][i]
        # 대각선 합 2
        diag2_sum += arr[i][N-1-i] # 인덱스는 0~99이므로 N-1=99
    emp_list.append(diag1_sum)
    emp_list.append(diag2_sum)

    max_sum = max(emp_list)

    print('#{} {}'.format(order, max_sum))

"""
## 강사님 풀이
for rc in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for _ in range(100)] # 단순 반복의 경우 변수로 언더바(_)를 사용해도 됨..?되나?

    ans = 0 # 최대값 저장
    # 행들의 합
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[i][j]
        ans = max(ans, S) # 행들의 합중 max 값

    # 열들의 합
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[j][i]
        ans = max(ans, S) # 행 max값과 열들의 합 중 max 값

    # 좌상단=>우하단
    S = 0
    for i in range(100):
        S += arr[i][i]
    ans = max(ans, S)

    # 우상단=>좌하단
    S = 0
    for i in range(100):
        S += arr[i][99-i]
    ans = max(ans, S)

    print(ans)

# 좀 더 줄여보기
ans = 0
dsum1 = dsum2 = 0
for i in range(100):
    rsum = csum = 0
    dsum1 += arr[i][i]
    dsum2 += arr[i][99 - i]
    for j in range(100):
        rsum += arr[i][j]
        csum += arr[j][i]
    ans = max(ans, rsum, csum)
ans = max(ans, dsum1, dsum2)
"""