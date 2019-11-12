import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

def push_and_pop(ch):
    # 스택이 비어있지 않고, 방금 받은 문자와 스택의 top 문자와 같으면 top 날려
    if len(stack) != 0 and stack[-1] == ch:
        stack.pop()
    # 아님 ch top으로 올려
    else:
        stack.append(ch)

for test in range(test_case):
    word = input()

    stack = []
    for ch in word:
        push_and_pop(ch)

    print('#{} {}'.format(test + 1, len(stack)))