import time
import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
start = time.time()

## 빙고판 생성
bingo_matrix = []
for i in range(5):
    bingo_matrix.append(list(map(int, input().split())))

## 빙고가 가능한 모든 경우 저장
bingo_case = []
# 행 5개
for row in bingo_matrix:
    bingo_case.append(row)

# 열 5개
for i in range(5):
    tmp_list = []
    for row in bingo_matrix:
        tmp_list.append(row[i])
    bingo_case.append(tmp_list)

# 대각 좌상 우하
tmp_list = []
for i in range(5):
    tmp_list.append(bingo_matrix[i][i])
bingo_case.append(tmp_list)

# 대각 우상 좌하
tmp_list = []
for i in range(5):
    tmp_list.append(bingo_matrix[i][4-i])
bingo_case.append(tmp_list)

## 사회자 호출 저장
bingo_answer = []
for i in range(5):
    tmp_list = list(map(int, input().split()))
    for ele in tmp_list:
        bingo_answer.append(ele)

## 빙고 케이스 리스트 안의 번호를 하나씩 0으로 바꿔주면서 빙고 검사
count = 0
# 0인 라인 검사
zero_check = [0, 0, 0, 0, 0]
for answer in bingo_answer:
    bingo = 0
    count += 1
    for row in bingo_case:
        if answer in row:
            row[row.index(answer)] = 0

    if count >= 12:
        for check in bingo_case:
            if check == zero_check:
                bingo += 1

    if bingo >= 3: # == 3으로 하면 안됨. 한번에 3개 이상의 빙고가 맞춰지는 경우가 있음.
        print(count)
        break







"""
### 답은 맞지만, 런타임 에러. 다른 방법 생각
## 빙고판 생성
bingo_matrix = []
for i in range(5):
    bingo_matrix.append(list(map(int, input().split())))

## 빙고가 가능한 모든 경우 저장
bingo_case = []
# 행 5개
for row in bingo_matrix:
    bingo_case.append(row)

# 열 5개
for i in range(5):
    tmp_list = []
    for row in bingo_matrix:
        tmp_list.append(row[i])
    bingo_case.append(tmp_list)

# 대각 좌상 우하
tmp_list = []
for i in range(5):
    tmp_list.append(bingo_matrix[i][i])
bingo_case.append(tmp_list)

# 대각 우상 좌하
tmp_list = []
for i in range(5):
    tmp_list.append(bingo_matrix[i][4-i])
bingo_case.append(tmp_list)

## 사회자 호출 저장
bingo_answer = []
for i in range(5):
    tmp_list = list(map(int, input().split()))
    for ele in tmp_list:
        bingo_answer.append(ele)


## start
answer_order = []
for i in range(25):
    answer_order.append(bingo_answer[i])
    bingo = 0
    for case in bingo_case:
        count = 0
        for j in range(5):
            if case[j] in answer_order:
                count += 1
                if count == 5:
                    bingo += 1
    if bingo == 3:
        result = i
        break

print(result + 1)
print("time :", time.time() - start)
"""