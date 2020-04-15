# SWEA 5650번 핀볼게임

> 출처 - [SWEA](https://swexpertacademy.com/)

## 문제 조건 및 분석

- 볼의 초기 위치와 방향은 임의로 정할 수 있다.
  
  - 위치 N^2^ * 방향 4
  
- 5가지의 블록에 대한 전략
  
  - 각 블록마다 볼이 어느 위치에서 닿았는지, 닿은 후의 볼의 방향을 어떻게 되는지를 정의해준다. 블록은 0번이 아니라 1번부터 시작한다.
  
  ```python
  Block_list = [(), (2, 3, 1, 0), (1, 3, 0, 2), (3, 2, 0, 1), (2, 0, 3, 1), (2, 3, 0, 1)]
  ```
  
- 웜홀에 대한 전략
  - 같은 번호를 가진 웜홀의 좌표를 쌍으로 저장한다. 웜홀은 10번까지 존재한다.
  
  ```python
  worm_list = [[] for i in range(11)]
  ```
  
  - 볼의 좌표가 웜홀의 위치와 같을 때, 번호는 같고 좌표는 다른 다른 웜홀로 볼의 좌표를 바꿔준다.
  
- 벽에 대한 전략
  
  - 볼의 좌표가 매트릭스 범위를 넘었을 때, 각 벽에 대한 조건을 작성해 볼의 방향을 바꿔준다.
  
- 게임종료 조건
  - 볼의 최초 위치 저장
  - 볼의 다음 좌표가 블랙홀이거나, 최초 좌표와 같으면 종료

## Source Code

```python
def out_matrix(r, c, d):
    global cnt
    cnt += 1
    if r == -1:
        return 2
    elif c == N:
        return 3
    elif r == N:
        return 0
    elif c == -1:
        return 1

def wormhole(in_pos, worm_num):
    for out_pos in worm_list[worm_num]:
        if in_pos != out_pos:
            return out_pos

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
Block_list = [(), (2, 3, 1, 0), (1, 3, 0, 2), (3, 2, 0, 1), (2, 0, 3, 1), (2, 3, 0, 1)]

testcase = int(input())

for test in range(testcase):
    N = int(input())
    N_matrix = [list(map(int, input().split())) for i in range(N)]
    worm_list = [[] for i in range(11)]
    for r in range(N):
        for c in range(N):
            if N_matrix[r][c] != 0:
                if N_matrix[r][c] >= 6:
                    worm_list[N_matrix[r][c]].append((r, c))

    max_cnt = 0
    for r in range(N):
        for c in range(N):
            if N_matrix[r][c] == 0:
                for direct in range(4):
                    tmp_r, tmp_c = r, c
                    tmp_direct = direct
                    cnt = 0
                    while 1:
                        tmp_r, tmp_c = tmp_r + D[tmp_direct][0], tmp_c + D[tmp_direct][1]
                        if 0 <= tmp_r < N and 0 <= tmp_c < N:
                            if (tmp_r == r and tmp_c == c) or (N_matrix[tmp_r][tmp_c] == -1):
                                if cnt > max_cnt:
                                    max_cnt = cnt
                                break
                            elif N_matrix[tmp_r][tmp_c] > 5:
                                tmp_r, tmp_c = wormhole((tmp_r, tmp_c), N_matrix[tmp_r][tmp_c])
                            elif N_matrix[tmp_r][tmp_c] > 0:
                                cnt += 1
                                tmp_direct = Block_list[N_matrix[tmp_r][tmp_c]][tmp_direct]
                        else:
                            tmp_direct = out_matrix(tmp_r, tmp_c, tmp_direct)
    print('#{} {}'.format(test+1, max_cnt))
```

## 감상

- 문제를 주어진대로 이해하지 않고, 내 생각이 들어가면서 풀이가 꼬이기 시작했다.
- 공의 최초 시작 위치가 벽에 붙어있을 때, 공의 방향이 벽쪽일 경우 공의 방향이 반대쪽바뀐 상태에서 계속 진행하는 줄 알았다. 하지만, 공이 튕긴 순간 게임은 시작된 거니, 같은 좌표일지라도 그 게임을 끝내야 하는게 맞다.
- 문제를 마음대로 해석해서는 안되고, 내 마음대로 추가 조건을 붙여서도 안된다.
