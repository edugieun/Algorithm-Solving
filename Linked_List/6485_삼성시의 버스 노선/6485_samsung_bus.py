import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N = int(input())
    station_list = [list(map(int, input().split())) for i in range(N)]
    P = int(input())

    num_line_list = [0] * 5001

    for station in station_list:
        for i in range(station[0], station[1] + 1):
            num_line_list[i] += 1
    print('#{}'.format(test+1), end=' ')
    # P가 순서대로 나온다는 보장도 없음. 1~5000까지의 숫자에서 랜덤임
    for i in range(P):
        print(num_line_list[int(input())], end=' ')

    print()