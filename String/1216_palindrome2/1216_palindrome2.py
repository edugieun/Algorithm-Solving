import sys
sys.stdin = open("input.txt", "r")

test_case = 10
"""
for test in range(test_case):

    test_number = int(input())
    len_nxn = 100

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

    max_len = 0

    ## 가로 palindrome
    for row in arr_nxn:
        # 회문 길이를 100~1까지 조사
        for len_palin in range(100, 0, -1):
            for start in range(len_nxn - len_palin + 1):
                end = start + len_palin - 1
                for i in range(len_palin // 2):
                    if row[start + i] != row[end - i]:
                        break
                else:
                    # 회문을 찾음
                    # max 회문 길이 갱신 후 다음 줄 검사
                    if len_palin > max_len:
                        max_len = len_palin
                        break

    ## 세로 palindrome
    for row in arr_nxn_col:
        for len_palin in range(100, 0, -1):
            for start in range(len_nxn - len_palin + 1):
                end = start + len_palin - 1
                for i in range(len_palin // 2):
                    if row[start + i] != row[end - i]:
                        break
                else:
                    # 회문을 찾음
                    if len_palin > max_len:
                        max_len = len_palin
                        break

    print('#{} {}'.format(test_number, max_len))

"""

"""
# 다른 방법
# 중간에서 길이를 늘려가면서 회문 조사
for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(100)]
    ans = 1
    
    for idx in range(100:
    for x in range(100):
        #길이가 짝수인 경우에는 x -> l(왼쪽)
        l, r, cnt = x, x + 1, 0
        while l >= 0 and r < 100:
            if arr[idx][l] != arr[idx][r]: beak
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)
            
        l, r, cnt = x, x + 1, 0
        while l >= 0 and r < 100:
            if arr[l][idx] != arr[r][idx]: beak
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)
            
        # 길이가 홀수일 때
        l, r, cnt = x - 1 , x + 1, 0
        while l >= 0 and r < 100:
            if arr[idx][l] != arr[idx][r]: beak
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)
            
        l, r, cnt = x - 1, x + 1, 0
        while l >= 0 and r < 100:
            if arr[l][idx] != arr[r][idx]: beak
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

"""