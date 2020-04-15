import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt', 'r')

def valid_check(first, compare_area,len_check):
    visit = [False] * (N + 1)
    Q = deque()
    Q.append(first)
    cnt = 0
    while Q:
        q = Q.popleft()
        if not visit[q]:
            visit[q] = True
            cnt += 1
            for el in adj[q]:
                if el not in compare_area:
                    Q.append(el)
    if cnt == len_check:
        return True
    else: return False

def populcnt(area):
    cnt = 0
    for i in area:
        cnt += popul[i]
    return cnt

N = int(input())
areas = [i for i in range(1, N+1)]
popul = [0] + list(map(int, input().split()))
adj = [set() for i in range(N+1)]
for i in range(1, N+1):
    adj_tmp = list(map(int, input().split()))
    for j in range(adj_tmp[0]):
        adj[i].add(adj_tmp[j+1])
        adj[adj_tmp[j+1]].add(i)

least_diff = 99999

for i in range(1, N//2 + 1):
    for A_area in combinations(areas, i):
        B_area = areas[:]
        for a in A_area:
            B_area.remove(a)

        if valid_check(A_area[0], B_area,len(A_area)) and valid_check(B_area[0], A_area,len(B_area)):
            least_diff_tmp = abs(populcnt(A_area) - populcnt(B_area))
            if least_diff_tmp < least_diff:
                least_diff = least_diff_tmp

if least_diff == 99999:
    print(-1)
else:
    print(least_diff)