import sys
sys.stdin = open("input.txt", "r")

test_case = 10

for test in range(test_case):

    len_palin = int(input())
    len_nxn = 8

    arr_nxn = []

    ## 문자열 읽어 2차 배열 형성
    for i in range(len_nxn):
        arr_nxn.append(input())

    ## 열 -> 행으로 바꾼 배열 형성
    arr_nxn_col = []
    for i in range(len_nxn):
        tmp_string = ''
        for row in arr_nxn:
            tmp_string += row[i]
        arr_nxn_col.append(tmp_string)

    count = 0

    ## 가로 palindrome
    for row in arr_nxn:
        for start in range(len_nxn - len_palin + 1):
            end = start + len_palin - 1
            for i in range(len_palin // 2):
                if row[start + i] != row[end - i]:
                    break
            else:
                count += 1

    ## 세로 palindrome
    for row in arr_nxn_col:
        for start in range(len_nxn - len_palin + 1):
            end = start + len_palin - 1
            for i in range(len_palin // 2):
                if row[start + i] != row[end - i]:
                    break
            else:
                count += 1

    print('#{} {}'.format(test+1, count))


"""
# 강사님 코드
for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    ans = 0

    # 한행에 대해서 길이가 N인 문자열의 모든 시작 위치, 0 ~ 8 - N
        for idx in range(8):
            for s in range(8 - N + 1):
                e = s + N - 1
                for i in range(N//2):
                    if arr[idx][s + i] != arr[idx][e - i]: break
                else:
                    ans += 1
                for i in range(N//2):
                    if arr[s + i][idx] != arr[e - i][idx]: break
                else:
                    ans += 1
"""