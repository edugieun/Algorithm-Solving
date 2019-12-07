import sys
sys.stdin = open('input.txt', 'r')

# subset
def sub_set(num_person):
    min_time = 9999999
    for selection in range(1 << num_person):
        group_a = []
        group_b = []
        for compare in range(num_person):
            if selection & (1 << compare):
                group_a.append(dist_A[compare][::])
            else:
                group_b.append(dist_B[compare][::])

        time_a = how_minute(group_a)
        time_b = how_minute(group_b)
        if time_a >= time_b:
            time = time_a
        else:
            time = time_b

        if time < min_time:
            min_time = time
    return min_time


def how_minute(people):
    Q = []
    finish = []
    minute = 0

    while len(finish) < len(people):
        minute += 1
        new_Q = []
        for person_num in Q:
            people[person_num][2] -= 1
            if people[person_num][2] > 0:
                new_Q.append(person_num)
            else:
                finish.append(person_num)
        Q = new_Q

        for person_num in range(len(people)):
            if person_num not in finish:
                if people[person_num][0] > 0:
                    people[person_num][0] -= 1
                elif people[person_num][0] == 0 and people[person_num][1] == 1 and len(Q) < 3:
                    people[person_num][1] = 0
                    Q.append(person_num)
    return minute

testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    people_pos = []
    stairs_pos = []
    for row in range(N):
        for col in range(N):
            if N_matrix[row][col] == 1:
                people_pos.append([row, col])
            elif N_matrix[row][col] > 1:
                stairs_pos.append([row, col, N_matrix[row][col]])

    dist_A = []
    dist_B = []
    for person in people_pos:
        dist_A.append([abs(person[0] - stairs_pos[0][0]) + abs(person[1] - stairs_pos[0][1]), 1, stairs_pos[0][2]])
        dist_B.append([abs(person[0] - stairs_pos[1][0]) + abs(person[1] - stairs_pos[1][1]), 1, stairs_pos[1][2]])

    result = sub_set(len(people_pos))
    print('#{} {}'.format(test+1, result))



