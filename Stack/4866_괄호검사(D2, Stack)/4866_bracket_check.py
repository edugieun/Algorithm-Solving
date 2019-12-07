bracket = ['(', '{', ')', '}']
test_case = int(input())


def push(item):  # full 상태 체크
    S.append(item)


def pop():
    return S.pop()

for test in range(test_case):
    paren = input()
    cnt = 0
    S = []
    for ch in paren:
        if ch in bracket:
            if ch == '(' or ch == '{':
                cnt += 1
                push(ch)
            else:
                if bool(S) == 0:
                    print('#{} 0'.format(test+1))
                    break
                elif ch == ')' and S[-1] == '(':
                    pop()
                elif ch == '}' and S[-1] == '{':
                    pop()

    else:
        if bool(S) == 0 and cnt != 0:
            print('#{} 1'.format(test+1))
        else: print('#{} 0'.format(test+1))


"""
# 도대체 뭐가 틀린거지. 9개만 맞다고 나오네.
import sys
sys.stdin = open("sample_input.txt", "r")

bracket = ['(', '{', ')', '}']
test_case = int(input())


def push(item):  # full 상태 체크
    S.append(item)


def pop():
    return S.pop()

for test in range(test_case):
    paren = input()
    cnt = 0
    S = []
    for ch in paren:
        if ch in bracket:
            if ch == '(' or ch == '{':
                cnt += 1
                push(ch)
            else:
                if bool(S) == 0:
                    print('#{} 0'.format(test+1))
                    break
                elif ch == ')' and S[-1] == '(':
                    pop()
                elif ch == '}' and S[-1] == '{':
                    pop()

    else:
        if bool(S) == 0 and cnt != 0:
            print('#{} 1'.format(test+1))
        else:
            print('#{} 0'.format(test+1))

"""