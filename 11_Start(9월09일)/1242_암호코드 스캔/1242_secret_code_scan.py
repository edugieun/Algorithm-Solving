import sys
sys.stdin = open('sample_input.txt', 'r')

code_num = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

test_case = int(input())

for test in range(test_case):
    N, M = map(int, input().split())
    N_matrix = ['{}'.format(bin(int(input(), 16))[2:]).zfill(M*4) for i in range(N)]
    stack = []
    result = 0
    for row in range(1, N):
        col = M*4 - 1
        while col > 0:
            if N_matrix[row][col] != '0' and N_matrix[row - 1][col] == '0':
                c4 = c3 = c2 = c1 = 0
                while N_matrix[row][col] == '1': c4 += 1; col -= 1
                while N_matrix[row][col] == '0': c3 += 1; col -= 1
                while N_matrix[row][col] == '1': c2 += 1; col -= 1
                mul = min(c2, c3, c4); c2, c3, c4 = c2//mul, c3//mul, c4//mul
                if (c2, c3, c4) in code_num:
                    stack.insert(0, code_num[(c2, c3, c4)])
            col -= 1

            if len(stack) == 8:
                odd_sum = (stack[0] + stack[2] + stack[4] + stack[6]) * 3
                even_sum = stack[1] + stack[3] + stack[5] + stack[7]
                total_sum = odd_sum + even_sum
                if total_sum % 10 == 0:
                    result += sum(stack)
                    stack = []
                else:
                    stack = []

    print('#{} {}'.format(test+1, result))

