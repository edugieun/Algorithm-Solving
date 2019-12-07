import sys
sys.stdin = open("input.txt", "r")

from pprint import pprint

test_case = int(input())

for test in range(test_case):
    N = int(input()) # 원통 개수
    stick_list = list(map(int, input().split()))

    # 암,수 나사 쌍으로 리스트에 집어넣기
    pair_stick_list = []
    for i in range(N):
        stick_pair = []
        for j in range(2):
            stick_pair.append(stick_list[j + (i * 2)]) # idx : 0,1 / 2,3 / 4,5 ...
        pair_stick_list.append(stick_pair)

    ## 생성할 수 있는 모든 경우 담기
    every_case = [] # 각 원통의 최대길이를 담을 리스트
    for idx1, pick_pair in enumerate(pair_stick_list): # 처음 원통 하나 뽑아서
        used_idx = [idx1] # 뽑은 원통의 인덱스는 used_idx 에 넣고
        tmp_length = [pick_pair] # 각각 뽑힌 원통이 만들 수 있는 최대 길이

        for i in range(len(pair_stick_list)): # 원통의 개수만큼 반복
            for idx2, compare_pair in enumerate(pair_stick_list): # 다시 비교할 원통을 하나씩 뽑으면서
                if idx2 in used_idx: # 이미 사용된 인덱스는 넘어가고
                    continue
                # 처음 뽑은 원통의 암나사와 사용안한 인덱스에 해당하는 원통의 수나사 크기가 같으면
                if pair_stick_list[idx1][1] == pair_stick_list[idx2][0]:
                    # 해당 인덱스는 used_idx 에 담고
                    used_idx.append(idx2)
                    # 합체시킨 후
                    tmp_length.append(pair_stick_list[idx2])
                    # idx1 을 현재의 idx2 로 바꿔
                    idx1 = idx2
                    # break 나온 후 다시 처음부터 돌려
                    break

        # 합체된 길이를 담아
        every_case.append(tmp_length)

    ## 최대 길이 뽑기
    max_len = every_case[0] # 최대길이 첫 리스트로 초기화
    for i in every_case:
        if len(i) > len(max_len):
            max_len = i

    # 2차 배열 리스트를 1차 배열 리스트로 만들기
    order_1st_list = []
    for i in max_len:
        for ele in i:
            order_1st_list.append(ele)

    # 정수 리스트를 '1', '2' 과 같이 문자열 리스트로 만들기(문자열은 추후 .join을 통해 합체하기 용이함)
    order_1st_list = list(map(str, order_1st_list))

    print('#{} {}'.format(test + 1, ' '.join(order_1st_list)))


"""
# by. seung hyun 
# 모든 나사가 빠짐없이 이어진다는 가정하에
# insert와 append를 이용해 앞뒤로 붙이는 방식

import sys
sys.stdin = open("input.txt", "r")

test_case = int(input())

for test in range(test_case):
    
    N = int(input())
    n_list = list(map(int, input().split()))
    res = []
    for i, j in zip(n_list[::2], n_list[1::2]): # zip이 for 문이 돌아갈 줄은 몰랐네.
        res.append([i, j])

    find = [res[0]] # 첫 비교값 init

    while len(find) != len(res): # 전제가 모든 나사가 빠짐없이 이어진다는 전제네... 쨌든.
        for i in range(1, len(res)): # 이미 find에 하나를 init 해놨으니까 원래의 res 길이보다 하나 적게 해줘야지
            # find 리스트에 있는 요소 앞에 붙일거냐
            if res[i][1] == find[0][0]: # 만약 앞에 붙어 find에 요소가 추가되면, 자동적으로 find[0] 번째 요소는 바뀌게됨.
                find.insert(0, res[i]) # insert는 특정 인덱스 번호에 직접 삽입. insert와 append는 세트로 외워
            # find 리스트에 있는 요소 뒤에 붙일거냐
            if find[-1][1] == res[i][0]:
                find.append(res[i])
    
    print(find)
"""