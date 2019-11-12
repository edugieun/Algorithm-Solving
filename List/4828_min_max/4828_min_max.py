import sys
sys.stdin = open("sample_input.txt", "r")

# testcase 개수
test_case = int(input())

# 나중에 더 큰 수를 옮겨줄 때 사용될 변수
tmp = 0

# testcase 만큼 반복
for test in range(test_case):
    num_of_num = int(input()) # 비교할 숫자들의 개수
    number_list = list(map(int, input().split())) # 비교할 숫자 리스트

    ## 1. 읽은 숫자 리스트를 크기순으로 정렬하기(버블 정렬)
    for j in range(num_of_num): # 리스트 내의 숫자들을 하나씩 읽으면서
        # 큰 숫자를 뒤로 보냄.
        for k in range(0, num_of_num - 1 - j): # 큰 수 들은 이미 뒤에 정렬되므로, 뒤에 정렬된 수까지는 비교를 안해도됨.
            if number_list[k] > number_list[k+1]: # 바로 뒤에 수와 비교해서, 현재 값이 더 크다면
                tmp = number_list[k] # 현재값을 임시 저장하고
                number_list[k], number_list[k+1] = number_list[k+1], tmp # 뒤에 값을 앞으로, 현재 값을 뒤로 보냄
    
    # 리스트의 첫 번째가 최소, 마지막이 최대. 차이를 구함
    diff = number_list[-1] - number_list[0]

    print('#{} {}'.format(test + 1, diff))