import sys
sys.stdin = open('input.txt', 'r')

L = 0
R = int(input())
red = list(map(int, input().split()))
blue = list(map(int, input().split()))
yellow = list(map(int, input().split()))

C = sum(red) / 2
if R - C >= C - L:
    for i in range(len(blue)):
        if blue[i] < C:
            blue[i] = C - blue[i] + C

    for i in range(len(yellow)):
        if yellow[i] < C:
            yellow[i] = C - yellow[i] + C
    L = C

else:
    for i in range(len(blue)):
        if blue[i] > C:
            blue[i] = C - blue[i] + C

    for i in range(len(yellow)):
        if yellow[i] > C:
            yellow[i] = C - yellow[i] + C
    R = C

if blue[0] != blue[1]:
    C = sum(blue) / 2
    if R - C >= C - L:
        for i in range(len(yellow)):
            if yellow[i] < C:
                yellow[i] = C - yellow[i] + C
        L = C

    else:
        for i in range(len(yellow)):
            if yellow[i] > C:
                yellow[i] = C - yellow[i] + C
        R = C

if yellow[0] == yellow[1]:
    print(R - C)

else:
    C = sum(yellow) / 2
    if R - C >= C - L:
        print(R - C)
    else:
        print(C - L)