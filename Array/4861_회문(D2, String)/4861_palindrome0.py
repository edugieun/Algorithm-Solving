import sys
from pprint import pprint
sys.stdin = open("sample_input.txt", "r")


test_case = int(input())

"""
for test in range(test_case):
    nxn_array, palin_len = map(int, input().split())

    ## 2차 배열 만들기 => 행스트링 리스트
    order_2nd_array = []
    for i in range(nxn_array):
        order_2nd_array.append(input())

    ## 열 나열을 갖는 2차 배열 만들기 => 열스트링 리스트
    order_2nd_array_col = []
    for i in range(nxn_array):
        tmp_string = ''
        for row in order_2nd_array:
            tmp_string += row[i]
        order_2nd_array_col.append(tmp_string)

    ## '행 palin 확인 법' 부분에서 쓰일 변수
    if palin_len % 2 == 0:
        even_comp = 1
    else:
        even_comp = 0

    ## palindrome 검사
    palin_check = 0
    while palin_check != 1:

        ## 행 검사
        for row in order_2nd_array:
            if palin_check == 1:
                break
            else:
                ## 행 palin 확인 법 => palin string을 반으로 자른 후 뒷 부분은 역방향 정렬 후 앞부분과 비교
                for i in range(nxn_array - palin_len + 1):
                    if (row[i] == row[i + palin_len - 1]) and (row[i:i + palin_len // 2] == row[i + palin_len:i + palin_len // 2 - even_comp:-1]):
                        palin_check = 1
                        palin_str = row[i:i + palin_len]
                        break

        ## 중간 검사: 행 검사에서 이미 찾았으면 빠져나와
        if palin_check == 1:
            break

        ## 열스트링 리스트 검사
        for row in order_2nd_array_col:
            if palin_check == 1:
                break
            else:
                ## 열스트링 리스트의 행 palin 확인 법
                for i in range(nxn_array - palin_len + 1):
                    if (row[i] == row[i + palin_len - 1]) and (row[i:i + palin_len // 2] == row[i + palin_len:i + palin_len // 2 - even_comp:-1]):
                        palin_check = 1
                        palin_str = row[i:i + palin_len]
                        break


    print('#{} {}'.format(test+1, palin_str))

## 너무 복잡하다. 다른 방법 찾아보자
"""

"""
for test in range(test_case):

    # 가능한 모든 경우를 조사하는 방법
    nxn_array, palin_len = map(int, input().split())

    ## 2차 배열 만들기 => 행스트링 리스트
    order_2nd_array = []
    for i in range(nxn_array):
        order_2nd_array.append(input())

    ## 열 나열을 갖는 2차 배열 만들기 => 열스트링 리스트
    order_2nd_array_col = []
    for i in range(nxn_array):
        tmp_string = ''
        for row in order_2nd_array:
            tmp_string += row[i]
        order_2nd_array_col.append(tmp_string)

    palin_check = 0
    while palin_check != 1:
        # 시작위치 0 ~ N - M
        for row in order_2nd_array:
            for start in range(nxn_array - palin_len + 1):
                end = start + palin_len - 1
                for i in range(palin_len//2):
                    if row[start + i] != row[end - i]:
                        break
                else:
                    palin_result = row[start:end]
                    palin_check = 1


        if palin_check != 1:
            for row in order_2nd_array_col:
                for start in range(nxn_array - palin_len + 1):
                    end = start + palin_len - 1
                    for i in range(palin_len // 2):
                        if row[start + i] != row[end - i]:
                            break
                    else:
                        palin_result = row[start:end]
                        palin_check = 1

    print(palin_result)
"""
