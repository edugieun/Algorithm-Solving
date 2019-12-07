import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) # 테스트케이스 개수

for test in range(T):
    N, M = list(map(int, input().split())) # N: 정수의 개수, M: 구간의 개수
    n_numbers = list(map(int, input().split()))

    inter_sum_list = [] # 구간 합을 담을 리스트
    
    ## 1. 구간 합을 리스트에 담아
    # 합 구간을 고려한 반복 가능한 횟수는 N-M+1 번 가능함.
    for i in range(N - M + 1):
        inter_sum_tmp = 0  # 임시 구간합
        # 구간만큼 더해
        for j in range(M):
            inter_sum_tmp += n_numbers[i + j]
        #구간 합을 리스트에 담아.
        inter_sum_list.append(inter_sum_tmp)

    ## 2. 구간 합 리스트에서 최소와 최대를 구해
    max_sum, min_sum = inter_sum_list[0], inter_sum_list[0] # 최대, 최소. 리스트의 첫 값으로 초기화
    for inter_sum in inter_sum_list:
        if max_sum < inter_sum:
            max_sum = inter_sum
        if min_sum > inter_sum:
            min_sum = inter_sum
    ## 3. 최대와 최소의 차이
    result = max_sum - min_sum

    print('#{} {}'.format(test+1, result))

"""
### 슬라이딩 윈도우(Sliding Window) 사용
## for 문 2개를 하나로 줄여, 시간 복잡도를 N*M 에서 N으로 줄인다.

Sum = 0
for i in range(M):
    Sum += arr[i]
    
Min = Max = Sum
for i in range(N - M + 1):
    Sum += (arr[i + M] - arr[i])
    Min = min(Min, Sum)
    Max = max(Max, Sum)

"""