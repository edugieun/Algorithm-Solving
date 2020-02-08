# 백준 17135번 캐슬 디펜스

- 문제 출처 - [백준 알고리즘](https://www.acmicpc.net/)

## 문제 조건 및 분석

1. M개의 격자에서 궁수를 배치할 3자리를 선택

   - 조합~M~C~3~

2. 궁수가 먼저 공격

   - 거리 D이하인 적 중에서 가장 가까운 적 + 가장 왼쪽에 있는 적

     - 각각 적의 위치를 리스트에 담는다. [행, 열]

     - 궁수의 타겟 선정하기(초기 target = ~~False~~ None)

       ❗ 값이 정의 되지 않은 target을 처음에는 `False`로 설정했었는데, 타겟의 index가 0인 경우에도 `False` 조건문에 진입하는 문제가 발생하였고, `False`를 `None`으로 변경하여 해결

       - 적과 궁수와의 거리를 계산한다.
       - 적과의 거리 = abs(궁수 행 - 적 행) + abs(궁수 열 - 적 열)
       - 적과의 거리 <= D 일 때,
         - target이 ~~False~~ None일 경우
           - target = 적의 index
           - target의 거리 = 적과의 거리
         - else
           - 적과의 거리 < target의 거리
             - target = 적의 index
             - target의 거리 = 적과의 거리
           - 적과의 거리 == target의 거리 and 적의 col < target의 col
             - target = 적의 index
             - target의 거리 = 적과의 거리

   - 같은 적을 공격할 수도 있다.

     - 각각의 궁수가 정한 타겟들을 ~~리스트~~ set에 담는다. 같은 값이 들어가지 않게 `set()`을 사용하여 담는다.

3. 궁수 공격 후 적이 한 칸 아래로 이동

   - 공격이 끝나면 생존한 적들을 갱신 및 이동
     - 타겟 리스트에 담긴 적들을 제거한다.
     - 탈출에 성공한 적들을 제거한다.
       - 적의 위치가 행의 끝(N)이면 탈출하는 적이므로 제거
       - 그렇지 않은 적들은 이동 처리를 해준다. row = row + 1

4. 생존한 적이 없을 때까지 반복

## 시행착오

❗ `Null`과 `False`는 다르며, `False`와 0은 같다.

❗ 리스트를 함수의 인자로 전해줄 경우, 함수 내에서 다시 딥카피를 해줘야하며, 리스트안에 또 리스트가 있을 경우 그 각각의 리스트 원소 또한 딥카피([:])를 해줘야 한다.

❗ 모든 테스트 케이스를 맞췄지만, 채점 과정에서 계속 오답이 발생

- 결국 직접 테스트 케이스를 만드는 코드를 코딩한 다음, 정답자의 코드를 돌려 나의 답을 비교
- 오답의 원인은 로직 상의 문제가 아닌 정말 사소한 변수하나를 잘못 설절해줌.

```python
# 궁수가 위치할 수 있는 총 열(col)의 크기
N_arr = [i for i in range(N)]
...;
# 궁수 위치를 정하는 조합을 구하는 부분에서의 for문
for i in range(start, N):
```

- 당연히 N과 M중, N이 행인줄 알았으나, M이 행이었다. 행과 열을 바꿔서 사용하고 있었음에도 모든 테스트 케이스는 통과를 했으니, 전혀 예상하지도 못하는 문제점이었다.
- 다음에도 이런 실수가 발생한다고 해도 예상이나 할 수 있을지 의문이 든다. 로직상 틀린 것이 없다고 판단될 경우에는 `변수의 초기설정`부터 다시 자세하게 훑어봐야 겠다.

## Source Code

```python
def combination(com_arr, start):
    global max_kill
    if len(com_arr) == R:
        deep_copy_enermies = []
        for i in enermies:
            deep_copy_enermies.append(i[:])
        kill = play(com_arr, deep_copy_enermies, 0)
        if max_kill < kill:
            max_kill = kill
    else:
        for i in range(start, M):
            combination(com_arr + [M_arr[i]], i + 1)

def play(arrows, now_enermies, cnt):
    deep_copy_now_enermies = []
    for i in now_enermies:
        deep_copy_now_enermies.append(i[:])
    if not deep_copy_now_enermies:
        return cnt
    targets = set()
    for arrow in arrows:
        target = None
        for idx, enermy in enumerate(deep_copy_now_enermies):
            dis_e = abs(N - enermy[0]) + abs(arrow - enermy[1])
            if dis_e <= D:
                if target == None:
                    target = idx
                    target_dis = dis_e
                else:
                    if dis_e < target_dis:
                        target = idx
                        target_dis = dis_e
                    elif dis_e == target_dis and enermy[1] < deep_copy_now_enermies[target][1]:
                        target = idx
                        target_dis = dis_e
        if target != None:
            targets.add(target)

    # 죽은 적 제거
    for i in sorted(targets, reverse=True):
        deep_copy_now_enermies.remove(deep_copy_now_enermies[i])
        cnt += 1
    # 적 이동과 탈출한 적 제거
    numof_enermies = len(deep_copy_now_enermies)
    for i in range(numof_enermies - 1, -1, -1):
        if deep_copy_now_enermies[i][0] == (N - 1):
            deep_copy_now_enermies.remove(deep_copy_now_enermies[i])
        else:
            deep_copy_now_enermies[i][0] += 1
    return play(arrows, deep_copy_now_enermies, cnt)

N, M, D = map(int, input().split())
R = 3
N_matrix = [list(map(int, input().split())) for i in range(N)]
M_arr = [i for i in range(M)]
enermies = []
for row in range(N):
    for col in range(M):
        if N_matrix[row][col] == 1:
            enermies.append([row, col])

max_kill = 0
combination([], 0)

print(max_kill)
```

