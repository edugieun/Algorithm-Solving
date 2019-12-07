import sys
sys.stdin = open('input.txt', 'r')

# test_case = int(input())
#
# for test in range(test_case):
#     N, S = map(int, input().split())
#     H = list(map(int, input().split()))
#
#     min_sum = sum(H)
#     for selection in range(1 << N):
#         tmp_sum = 0
#         for pick in range(N):
#             if selection & (1 << pick):
#                 tmp_sum += H[pick]
#                 if tmp_sum >= min_sum:
#                     break
#
#         if S <= tmp_sum < min_sum:
#             min_sum = tmp_sum
#             if tmp_sum == S:
#                 break
#
#     print('#{} {}'.format(test + 1, min_sum - S))


# backtrack 가지치기
def backtrack(k):
    global tmp_sum, min_height
    if S <= tmp_sum < min_height:
        min_height = tmp_sum
        return

    for i in range(k, N):
        if tmp_sum > min_height:
            return
        if min_height == S:
            break
        tmp_sum += H[i]
        backtrack(i + 1)
        tmp_sum -= H[i]

test_case = int(input())

for test in range(test_case):
    N, S = map(int, input().split())

    H = list(map(int, input().split()))

    selected = []
    min_height = sum(H)
    tmp_sum = 0
    backtrack(0)

    print('#{} {}'.format(test + 1, min_height - S))
