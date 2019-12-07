import sys
sys.stdin = open('input.txt', 'r')

for a in range(int(input())):
    N = int(input())
    n = list(map(int, input().split()))
    r = -1
    for i in range(N):
        for j in range(i + 1, N):
            mul = n[i] * n[j]
            if mul >= 10:
                tmp = 1
                for k in str(mul):
                    if int(k) >= tmp:
                        tmp = int(k)
                    else:
                        break
                else:
                    if mul >= r:
                        r = mul
    print('#{} {}'.format(a + 1, r))

# 50개중 27개 제한시간 초과
# test_case = int(input())
#
# for test in range(test_case):
#     N = int(input())
#     numbers_list = list(map(int, input().split()))
#
#     max_mul_result = -1
#     for i in range(N - 1):
#         for j in range(i+1, N):
#             mul_result = numbers_list[i] * numbers_list[j]
#             mul_result_list = list(map(int, list(str(mul_result))))
#             if len(mul_result_list) > 1:
#                 for k in range(len(mul_result_list) - 1):
#                     if mul_result_list[k+1] >= mul_result_list[k]:
#                         pass
#                     else:
#                         break
#                 else:
#                     if mul_result > max_mul_result:
#                         max_mul_result = mul_result
#
#     print('#{} {}'.format(test+1, max_mul_result))

# 36개 시간초과
# test_case = int(input())
#
# for test in range(test_case):
#     N = int(input())
#     numbers_list = list(map(int, input().split()))
#
#     max_mul_result = -1
#     for i in range(N - 1):
#         for j in range(i+1, N):
#             mul_result = numbers_list[i] * numbers_list[j]
#             if mul_result < 10:
#                 break
#
#             mul_result_list = list(map(int, list(str(mul_result))))
#
#             for k in range(len(mul_result_list) - 1):
#                 if mul_result_list[k+1] < mul_result_list[k]:
#                     break
#             else:
#                 if mul_result > max_mul_result:
#                     max_mul_result = mul_result
#
#     print('#{} {}'.format(test+1, max_mul_result))

# #  선생님 풀이
# max_num = -1
#
# for i in range(N-1):
#     for j in range(i+1, N):
#         s = li[i] * li[j]
#         t = s
#         # 선생님의 자릿수 비교 방식
#         while t != 0:
#             # 1. 1의자리 먼저 뽑고
#             a = t % 10 # 1의 자리수
#             # 2. 1의 자리를 제외한 나머지만 t에 갱신
#             t = t // 10 # 1의 자리를 제외한 나머지 수
#             # 3. 갱신된 수에서 다시 1의자리를 추출하여 비교
#             b = t % 10
#             if b > a:
#                 break
#         # t==0인 수 중(단조 증가하는 수 중)에서 최대값만 담기
#         if t == 0:
#             if max_num < s:
#                 max_num = s
