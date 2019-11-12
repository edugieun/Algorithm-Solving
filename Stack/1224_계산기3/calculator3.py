import sys
sys.stdin = open('input.txt', 'r')
order_dict = {'(': 0, '+': 1, '*': 2}

test_case = 10
for test in range(test_case):

    input()
    string = input()
    postfix_notation = []
    oper_stack = []

    for char in string:
        if char.isdigit():
            postfix_notation.append(int(char))
        else:
            if char == '(':
                oper_stack.append(char)
            elif char == ')':
                while oper_stack[-1] != '(':
                    postfix_notation.append(oper_stack.pop())
                oper_stack.pop()
            else:
                while len(oper_stack) != 0 and order_dict[oper_stack[-1]] >= order_dict[char]:
                    postfix_notation.append(oper_stack.pop())
                oper_stack.append(char)
    while len(oper_stack) != 0:
        postfix_notation.append(oper_stack.pop())

    cal = []
    for char in postfix_notation:
        if type(char) == int:
            cal.append(char)
        else:
            num2 = cal.pop()
            num1 = cal.pop()
            if char == '+':
                cal.append(num1 + num2)
            elif char == '*':
                cal.append(num1 * num2)
    print('#{} {}'.format(test+1, cal[0]))
