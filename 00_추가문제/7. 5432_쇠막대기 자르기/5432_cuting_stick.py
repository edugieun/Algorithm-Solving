import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    stick_cutting = input()

    stick_acc = 0
    total_stick = 0

    for idx in range(len(stick_cutting)):
        if stick_cutting[idx] == '(':
            stick_acc += 1
        elif stick_cutting[idx] == ')':
            stick_acc -= 1
            if stick_cutting[idx - 1] == '(':
                total_stick += stick_acc
            else:
                total_stick += 1

    print('#{} {}'.format(test+1, total_stick))
