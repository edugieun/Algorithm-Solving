import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

def my_cal(oper):
    global stack, error

    if len(stack) >= 2 and oper != '.':
        a = stack.pop(-1)
        b = stack.pop(-1)
        if oper == '+':
            stack.append(b + a)
        elif oper == '-':
            stack.append(b - a)
        elif oper == '/':
            stack.append(b / a)
        elif oper == '*':
            stack.append(b * a)

    else:
        if len(stack) == 1 and oper == '.':
            return print('#{} {}'.format(test+1, int(stack[0])))
        else:
            error = 1
            return print('#{} error'.format(test+1))

for test in range(test_case):
    math_string = list(map(str, input().split()))

    stack = []
    error = 0
    for char in math_string:
        if char.isdigit():
            stack.append(int(char))
        else:
            my_cal(char)
            if error == 1:
                break
    if len(stack) > 1 and error != 1:
        print('#{} error'.format(test + 1))