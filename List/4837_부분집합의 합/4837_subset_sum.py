import sys
sys.stdin = open("sample_input.txt", "r")

# 전체 집합
set_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num_ele = len(set_list) # 원소의 개수

test_case = int(input())
for test in range(test_case):

    N, K = list(map(int, input().split()))

    # 모든 부분집합 구하기
    subset_list = []  # 부분집합 리스트
    for i in range(1 << num_ele):
        tmp_list = []
        for j in range(num_ele):
            a = 1 << j
            if i & a:
                tmp_list.append(set_list[j])
        subset_list.append(tmp_list)

    # 원소 개수가 N 개인 부분집합 중 합이 K인 경우 count (선생님 풀이: 이 부분을 걍 위에 부분집합에서 바로 합쳐버릴 수 있음)
    count = 0
    for i in subset_list:
        if len(i) == N and sum(i) == K:
            count += 1
    print('#{} {}'.format(test+1, count))
"""
# full set
set_list = [1, 2, 3]
num_ele = len(set_list) # number of element

# get all of subset of set
# 부분집합 구하는 원리가 도저히 이해가 안감.
subset_list = [] # 부분집합 리스트
for i in range(1 << num_ele):
    tmp_list = []
    for j in range(num_ele):
        a = 1 << j
        if i & a:
            tmp_list.append(set_list[j])
    subset_list.append(tmp_list)

# 원소 개수가 N = 3 개인 부분집합 중 합이 K = 6인 경우 count
count = 0
for i in subset_list:
    if len(i) == 3 and sum(i) == 6:
        count += 1

print(count)

"""