import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    aisle = [0] * 201

    n_students = int(input())
    room_lists = [list(map(int, input().split())) for i in range(n_students)]
    for room in room_lists:
        # 숨겨진 test_case: room[0]이 room[1]보다 클 경우
        if room[0] > room[1]:
            room[0], room[1] = room[1], room[0]

        for i in range((room[0] + 1) // 2, (room[1] + 1) // 2 + 1):
            aisle[i] += 1

    print('#{} {}'.format(test + 1, max(aisle)))