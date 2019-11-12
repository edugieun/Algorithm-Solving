import sys
sys.stdin = open('input.txt', 'r')


def change(cnt, start):
    global max_num

    if cnt == N:
        max_num = max(max_num, int(''.join(map(str, int_nums))))

    else:
        for i in range(start, len(int_nums)):
            for j in range(i+1, len(int_nums)):
                if int_nums[i] <= int_nums[j]:
                    int_nums[i], int_nums[j] = int_nums[j], int_nums[i]
                    change(cnt + 1, i)
                    int_nums[j], int_nums[i] = int_nums[i], int_nums[j]

testcase = int(input())

for test in range(testcase):
    str_nums, N = map(str, input().split())
    N = int(N)
    int_nums = list(map(int, str_nums))
    max_num = 0
    change(0, 0)
    print('#{} {}'.format(test + 1, max_num))