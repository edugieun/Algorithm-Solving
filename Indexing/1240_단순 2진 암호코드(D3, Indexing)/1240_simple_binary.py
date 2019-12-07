import sys
sys.stdin = open('input.txt', 'r')

num_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

test_case = int(input())

for test in range(test_case):
    N, M = map(int, input().split())

    N_matrix = [input() for i in range(N)]

    for row in range(N):
        for col in range(M - 1, -1, -1):
            if N_matrix[row][col] == '1':
                code_string = N_matrix[row][col::-1]
                break

    code = []
    for i in range(8):
        if code_string[i*7:i*7 + 7][::-1] in num_code:
            code.insert(0, num_code[code_string[i*7:i*7 + 7][::-1]])

    code.insert(0, 0)
    odd = []
    even_sum = 0
    for i in range(1, 8):
        if i % 2 == 1:
            odd.append(code[i])
        else:
            even_sum += code[i]
    result_sum = sum(odd)*3 + even_sum + code[8]

    if result_sum % 10 == 0:
        print('#{} {}'.format(test + 1, sum(code)))
    else:
        print('#{} 0'.format(test + 1))






