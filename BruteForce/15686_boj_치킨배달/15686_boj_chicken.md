# 백준 15686번 치킨 배달

> 출처 - [백준 알고리즘](https://www.acmicpc.net/)

## 문제 조건 및 분석

- 모든 집과 치킨 집의 좌표를 저장한다.
- 전체 치킨집 중에서 M개를 고른다. => 조합 nCm
- 각 집마다 선택된 모든 치킨 집과의 거리를 계산했을 때 최소 값을 누적한다.

## Source Code

```python
# 184ms
from itertools import combinations
N, M = map(int, input().split())

N_matrix = [list(map(int, input().split())) for i in range(N)]

every_chicken = []
every_home = []
for row in range(N):
    for col in range(N):
        if N_matrix[row][col] == 2:
            every_chicken.append([row, col])
        elif N_matrix[row][col] == 1:
            every_home.append([row, col])

total_dis = 9999999
for chi_list in combinations(every_chicken, M):
    total_tmp = 0
    for home in every_home:
        min_tmp = 999999
        for chi in chi_list:
            dis = abs(home[0]-chi[0]) + abs(home[1]-chi[1])
            if dis < min_tmp:
                min_tmp = dis
        total_tmp += min_tmp
    if total_tmp < total_dis:
        total_dis = total_tmp

print(total_dis)
```

## 감상

- 완전탐색과 조합에 관련된 문제이다. 경우의 수도 크지가 않아서 시간초과에 대한 우려도 없어보인다.
