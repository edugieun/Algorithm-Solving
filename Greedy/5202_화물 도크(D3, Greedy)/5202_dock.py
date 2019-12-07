import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N = int(input())
    schedules = [list(map(int, input().split())) for i in range(N)]

    for j in range(len(schedules)):
        for i in range(0, len(schedules) - j - 1):
            if schedules[i][1] > schedules[i + 1][1]:
                schedules[i], schedules[i + 1] = schedules[i + 1], schedules[i]
            elif schedules[i][1] == schedules[i + 1][1]:
                if schedules[i][0] > schedules[i + 1][0]:
                    schedules[i], schedules[i + 1] = schedules[i + 1], schedules[i]

    cnt = 1
    init = schedules[0]
    for i in range(1, len(schedules)):
        if schedules[i][0] >= init[1]:
            cnt += 1
            init = schedules[i]

    print('#{} {}'.format(test + 1, cnt))
