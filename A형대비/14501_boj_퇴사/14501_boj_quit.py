import sys
sys.stdin = open('input.txt', 'r')


def backtrack(today):
    global work, p_sum
    for day in range(today, len(days)):
        if day + T[day] <= N+1:
            work.append(P[day])
            nxt_day = day + T[day]
            backtrack(nxt_day)
    if sum(work) > p_sum:
        p_sum = sum(work)
    work.pop()
    return None



N = int(input())
days = [i for i in range(N+1)]
TnP = [list(map(int, input().split())) for i in range(N)]
T, P = [0], [0]

for i in TnP:
    T.append(i[0])
    P.append(i[1])

p_sum = 0
for day in range(1, len(days)):
    work = []
    if day + T[day] <= N+1:
        work.append(P[day])
        nxt_day = day + T[day]
        backtrack(nxt_day)

print(p_sum)