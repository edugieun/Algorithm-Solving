# 백준 14502번 연구소

> 출처 - [백준 알고리즘](https://www.acmicpc.net/)

## 문제 조건 및 분석

- NxM 매트릭스에서 3개의 벽을 세운다. -> 조합 ~NxM~C~3~ 
  - 벽을 세울 수 있는 곳의 좌표를 리스트에 담은 후 좌표의 조합을 구한다.
  - 해당 좌표에 벽을 세운다. -> 해당 조합이 끝난 후 벽을 다시 지우는 부분도 추가해준다.
- 바이러스 확산 BFS
  - Queue에 바이러스들의 좌표를 넣는다.
  - 확산된 지역인지 확인하기 위한 visit matrix를 만든다.
  - 확산될 때마다 cnt를 증가시킨다.

## Source Code

```python
# 416ms
from itertools import combinations
from collections import deque

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
NM_matrix = [list(map(int, input().split())) for i in range(N)]
empty_list = []

vir_list = []
for row in range(N):
    for col in range(M):
        if NM_matrix[row][col] == 0:
            empty_list.append((row, col))
        elif NM_matrix[row][col] == 2:
            vir_list.append((row, col))
least_vir = 999999
for wall_list in combinations(empty_list, 3):

    for r, c in wall_list:
        NM_matrix[r][c] = 1

    cnt = 0
    visit = [[False] * M for i in range(N)]
    Q = deque()
    for vir in vir_list:
        Q.append(vir)

    while Q and cnt < least_vir:
        v_r, v_c = Q.popleft()
        for dr, dc in D:
            tmp_r, tmp_c = v_r + dr, v_c + dc
            if 0 <= tmp_r < N and 0 <= tmp_c < M and (NM_matrix[tmp_r][tmp_c] == 0) and not visit[tmp_r][tmp_c]:
                visit[tmp_r][tmp_c] = True
                cnt += 1
                Q.append((tmp_r, tmp_c))
        if cnt > least_vir:
            break

    for r, c in wall_list:
        NM_matrix[r][c] = 0

    if cnt < least_vir:
        least_vir = cnt
print(len(empty_list) - least_vir - 3)
```

## 감상

- 조합과 BFS에 대한 문제이다.
- 조합에 대한 완전탐색 문제이기 때문에 시간을 어떻게 줄일 수 있을까 고민했는데, 바이러스 확산할 때마다 기존 매트릭스를 건드는 것보다는 visit matrix와 cnt 변수를 이용하였다.

