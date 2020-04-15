# 4940ms
# import sys
# from itertools import permutations
# sys.stdin = open('input.txt', 'r')
#
#
# N = int(input())
# A = list(map(str, input().split()))
# n_op = list(map(int, input().split()))
# op = ['+', '-', '*', '/']
# op_list = []
# for i in range(4):
#     op_list += [op[i]] * n_op[i]
#
# l_op = len(op_list)
# min_num = 1000000001
# max_num = -1000000001
# for op_tmp in set(permutations(op_list)):
#     tmp = A[0]
#     for i in range(l_op):
#         if op_tmp[i] == '/':
#             tmp = str(int(eval(tmp + op_tmp[i] + A[i + 1])))
#         else:
#             tmp = str(eval(tmp + op_tmp[i] + A[i+1]))
#
#     if int(tmp) < int(min_num):
#         min_num = tmp
#     if int(tmp) > int(max_num):
#         max_num = tmp
# print(max_num)
# print(min_num)
##########################
# 1088ms
# import sys
# from itertools import permutations
# sys.stdin = open('input.txt', 'r')
#
#
# N = int(input())
# A = list(map(int, input().split()))
# n_op = list(map(int, input().split()))
# op = ['+', '-', '*', '/']
# op_list = []
# for i in range(4):
#     op_list += [op[i]] * n_op[i]
#
# l_op = len(op_list)
# min_num = 1000000001
# max_num = -1000000001
# for op_tmp in set(permutations(op_list)):
#     tmp = A[0]
#     for i in range(l_op):
#         if op_tmp[i] == '/':
#             tmp = int(tmp / A[i + 1])
#         elif op_tmp[i] == '+':
#             tmp = tmp + A[i+1]
#         elif op_tmp[i] == '-':
#             tmp = tmp - A[i+1]
#         elif op_tmp[i] == '*':
#             tmp = tmp * A[i+1]
#
#     if tmp < min_num:
#         min_num = tmp
#     if tmp > max_num:
#         max_num = tmp
# print(max_num)
# print(min_num)
#############################
# 228ms
import sys
sys.stdin = open('input.txt', 'r')

def dfs(n_cal, n_add, n_sub, n_mul, n_div, tmp):
    global min_num, max_num
    if n_cal == t_n_op:
        if tmp < min_num:
            min_num = tmp
        if tmp > max_num:
            max_num = tmp
    else:
        if n_add:
            dfs(n_cal+1, n_add - 1, n_sub, n_mul, n_div, tmp + A[n_cal + 1])
        if n_sub:
            dfs(n_cal+1, n_add, n_sub - 1, n_mul, n_div, tmp - A[n_cal + 1])
        if n_mul:
            dfs(n_cal+1, n_add, n_sub, n_mul - 1, n_div, tmp * A[n_cal + 1])
        if n_div:
            dfs(n_cal+1, n_add, n_sub, n_mul, n_div - 1, int(tmp / A[n_cal + 1]))

N = int(input())
A = list(map(int, input().split()))
n_op = list(map(int, input().split()))
t_n_op = sum(n_op)

min_num = 1000000001
max_num = -1000000001
tmp = A[0]
dfs(0, n_op[0], n_op[1], n_op[2], n_op[3], tmp)

print(max_num)
print(min_num)
