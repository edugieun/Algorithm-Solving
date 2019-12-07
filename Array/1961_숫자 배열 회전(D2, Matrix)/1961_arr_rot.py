import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N = int(input())

    rot_180 = list(reversed([''.join(reversed(input().split())) for i in range(N)]))

    rot_90 = []
    rot_270 = []
    for col in range(N):
        tmp = ''
        for row in range(N):
            tmp += rot_180[row][col]
        rot_90.insert(0, tmp)
        rot_270.append(''.join(reversed(tmp)))

    print('#{}'.format(test+1))
    for i in range(N):
        print(rot_90[i], rot_180[i], rot_270[i])


