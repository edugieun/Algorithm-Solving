import sys
sys.stdin = open("sample_input.txt", "r")
test_case = int(input())

for test in range(test_case):


    P, Pa, Pb = list(map(int, input().split()))

    l = 1 # 왼쪽
    r = P # 오른쪽
    c = 1 # 현재 쪽

    count_A = 0
    while c != Pa:
        count_A += 1
        c = int((l + r) / 2)
        if Pa > c:
            l = c
        if Pa < c:
            r = c

    l = 1  # 왼쪽
    r = P  # 오른쪽
    c = 1  # 현재 쪽

    count_B = 0
    while c != Pb:
        count_B += 1
        c = int((l + r) / 2)
        if Pb > c:
            l = c
        if Pb < c:
            r = c

    if count_A < count_B:
        winner = 'A'
    elif count_A > count_B:
        winner = 'B'
    else:
        winner = 0

    print('#{} {}'.format(test+1, winner))
