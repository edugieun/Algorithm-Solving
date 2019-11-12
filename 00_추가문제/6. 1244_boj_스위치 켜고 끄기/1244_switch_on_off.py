import sys
sys.stdin = open('input.txt', 'r')

n_switch = int(input())
switch_list = [0] + list(map(int, input().split()))
n_student = int(input())
student_list = [list(map(int, input().split())) for i in range(n_student)]

for info in student_list:
    if info[0] == 1:
        for i in range(1, n_switch//info[1] + 1):
            switch_list[i * info[1]] = int(not switch_list[i * info[1]])
    else:
        switch_list[info[1]] = int(not switch_list[info[1]])
        move = 1
        while (info[1]-move) > 0 and (info[1]+move) <= n_switch and switch_list[info[1] - move] == switch_list[info[1] + move]:
            switch_list[info[1] - move] = int(not switch_list[info[1] - move])
            switch_list[info[1] + move] = int(not switch_list[info[1] + move])
            move += 1

for i in range(1, len(switch_list)):
    print(switch_list[i], end= ' ')
    if i%20 == 0:
        print()