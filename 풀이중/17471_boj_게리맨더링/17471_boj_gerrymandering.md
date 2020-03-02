# 백준 17471번 게리맨더링

> 출처 - [백준 알고리즘](https://www.acmicpc.net/)

## 문제 조건 및 분석

- 1~N 구역을 2개의 지역구로 나눈다. -> ~~부분집합 활용~~ 조합 활용
- 각 지역구가 가능한 방법인지 확인한다.
  - 인접리스트 활용.
  - 해당 구역의 첫번째 인자를 이용하여 BFS로 인접한 모든 구역을 리스트에 담는다.
    - 리스트 대신 cnt를 사용하면 시간을 줄일 수 있다.
  - 리스트의 길이와 해당 지역구의 길이가 같을 경우 타당하다고 본다.
- 각 지역구의 인구 수 차이 구하기.
  - 두 선거구로 나눌 수 없는 경우 -1 출력
    - 초기 인구 수 차이를 큰 수로 놓고, 코드가 끝날 때까지 이 큰 수가 바뀌지 않으면 -1 출력

## Source Code

```python
from itertools import combinations
from collections import deque

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
```

## 감상

- 양방향 인접 리스트 또는 인접 매트릭스에 대한 문제이다.
- 처음에는 두 지역구를 부분 집합을 이용하여 나누려고 했으나, 코드길이와 시간 상의 문제가 있을 것 같아 itertools 모듈로 바꾸었다.
- 반복되는 로직(ex: 지역구의 타당성 검사, 지역구의 인구 차이)이 있어서 함수를 선언하여 처리하였다.

