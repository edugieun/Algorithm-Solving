import sys
sys.stdin = open('input.txt', 'r')

def binary_search(l, r, looking, direction):
    global cnt
    m = (l + r) // 2
    # 찾을 경우
    if A[m] == looking:
        cnt += 1
        return
    # 왼쪽
    elif A[m] > looking and direction == 1:
        if m == l:
            if A[r] == looking:
                cnt += 1
        else:
            r = m - 1
        direction = 0
    elif A[m] < looking and direction == 0:
        l = m + 1
        direction = 1
    else:
        return

    binary_search(l, r, looking, direction)

test_case = int(input())

for test in range(test_case):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    B = list(map(int, input().split()))

    cnt = 0
    for b in B:
        l_init = 0
        r_init = N - 1
        m_init = r_init // 2
        if A[m_init] == b:
            cnt += 1
            continue
        elif A[m_init] > b: # 왼쪽
            r_init = m_init - 1
            direction_init = 0
        else:
            # 오른쪽
            if m_init == 0:
                if A[-1] == b:
                    cnt += 1
                    continue
                else:
                    continue
            l_init = m_init + 1
            direction_init = 1

        binary_search(l_init, r_init, b, direction_init)

    print('#{} {}'.format(test + 1, cnt))