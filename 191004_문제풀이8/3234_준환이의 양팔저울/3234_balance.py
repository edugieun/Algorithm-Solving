import sys, time
sys.stdin = open('sample_input.txt', 'r')


def dp_scale(right, left, state):
    if right > left:
        return 0

    if sum(visited) == N:
        return 1

    if memo[state] != -1:
        return memo[state]

    case = 0
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            case += dp_scale(right, left + W[i], state + (1 << i))
            case += dp_scale(right + W[i], left, state + (1 << (i + N)))
            visited[i] = 0

    memo[state] = case
    return case


testcase = int(input())

for test in range(testcase):
    N = int(input())
    W = list(map(int, input().split()))
    memo = [-1] * (1 << N*2)
    visited = [0] * N
    state = 0
    left, right = 0, 0
    result = dp_scale(right, left, state)

    print('#{} {}'.format(test + 1, result))

# def perm(in_list):
#     global visited, dp_list
#     if len(visited) == len(in_list):
#         impossible_cnt(0, 0, 0, visited)
#         return
#
#     for ele in in_list:
#         if ele not in visited:
#             visited.append(ele)
#             perm(in_list)
#             visited.pop()
#
#
# def impossible_cnt(start, right, left, in_list_2):
#     global im_cnt
#
#     for i in range(start, N):
#         right += in_list_2[i]
#         if right > left:
#             im_cnt += 2**(N - (i + 1))
#             right -= in_list_2[i]
#             left += in_list_2[i]
#         else:
#             impossible_cnt(i + 1, right, left, in_list_2)
#             left += in_list_2[i]
#             right -= in_list_2[i]
#
# start = time.time()
#
# testcase = int(input())
#
# for test in range(testcase):
#     N = int(input())
#     W = list(map(int, input().split()))
#     fact_N = 1
#     n_perm = 2**N
#     for i in range(1, N + 1):
#         fact_N *= i
#
#     im_cnt = 0
#     visited = []
#
#     perm(W)
#
#     print('#{} {}'.format(test + 1, fact_N*n_perm - im_cnt))
#
# print(time.time() - start)




# def perm(arr, pick_num):
#     global visited, cnt
#
#     if len(visited) == pick_num:
#         cnt_check(visited, [], [], 0)
#         return
#
#     for ele in arr:
#         if ele not in visited:
#             visited.append(ele)
#             perm(arr, pick_num)
#             visited.pop()
#
#
# def cnt_check(N_arr, left_list, right_list, start):
#     global cnt
#
#     if sum(left_list) < sum(right_list):
#         return
#
#     if sum(left_list) + sum(right_list) == sum(N_arr):
#         cnt += 1
#         return
#
#     for i in range(start, N):
#         right_list.append(N_arr[i])
#         cnt_check(N_arr, left_list, right_list, i + 1)
#         right_list.pop()
#         left_list.append(N_arr[i])
#         cnt_check(N_arr, left_list, right_list, i + 1)
#         if sum(left_list) == sum(N_arr):
#             break
#         left_list.pop()
#
#
# testcase = int(input())
#
# for test in range(testcase):
#     N = int(input())
#     W = list(map(int, input().split()))
#     W_half = sum(W)//2
#     cnt = 0
#     visited = []
#
#     perm(W, N)
#     print(cnt)
# print(time.time() - start )
