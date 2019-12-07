from pprint import pprint
import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for test in range(test_case):
    # Init 10 x 10 array
    ten_by_ten = []
    for i in range(10):
        grid = []
        for j in range(10):
            grid.append(0)
        ten_by_ten.append(grid)

    num_area =int(input()) # number of areas

    # Get location and color in num_area
    area_arr = [] # Info of location and color
    for i in range(num_area):
        area_arr.append(list(map(int, input().split())))

    # fulfill area
    for i in range(num_area):
        x1 = area_arr[i][0]
        y1 = area_arr[i][1]
        x2 = area_arr[i][2]
        y2 = area_arr[i][3]
        x_dif = area_arr[i][2] - area_arr[i][0] # x 좌표 차이
        y_dif = area_arr[i][3] - area_arr[i][1] # y 좌표 차이
        for j in range(y_dif + 1): # y축 (좌표상에서 행을 하나 고른 후)
            for k in range(x_dif + 1): # x축 (좌표상에서 열을 바꾸면서 채운다)
                ten_by_ten[y1 + j][x1 + k] += area_arr[i][4]

    # overlap area count
    overlap_cnt = 0
    for i in range(10):
        for j in range(10):
            if ten_by_ten[i][j] == 3: # 문제에서 같은 색은 겹치지 않는다고 했으니, 빨강이 3번 겹치지 않는이상 겹친 곳은 무조건 3
                overlap_cnt += 1

    print('#{} {}'.format(test + 1, overlap_cnt))

"""
from pprint import pprint

# 10 x 10 격자 생성
ten_by_ten = []
for i in range(10):
    grid = []
    for j in range(10):
        grid.append(0)
    ten_by_ten.append(grid)

## 영역 채우기
# 빨간 영역(1) 2.2 ~ 4.4 = 3x3
for i in range(3):
    for j in range(3):
        ten_by_ten[i + 2][j + 2] += 1

# 파란 영역(2) 3.3 ~ 6.6 = 4x4
for i in range(4):
    for j in range(4):
        ten_by_ten[i + 3][j + 3] += 2

pprint(ten_by_ten)

# 겹친 부분 = 빨간영역(1) + 파란영역(2) = 3
overlap_cnt = 0
for i in range(10):
    for j in range(10):
        if ten_by_ten[i][j] == 3:
            overlap_cnt += 1

print(overlap_cnt)
"""