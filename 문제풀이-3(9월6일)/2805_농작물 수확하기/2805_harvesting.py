import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    N = int(input())
    N_matrix = [list(map(int, input())) for i in range(N)]

    left = N//2
    right = N//2 + 1
    hav_sum = 0
    for row in range(N):
        for col in range(left, right):
            hav_sum += N_matrix[row][col]

        if row < N//2:
            left -= 1
            right += 1
        else:
            left += 1
            right -= 1

    print('#{} {}'.format(test + 1, hav_sum))
