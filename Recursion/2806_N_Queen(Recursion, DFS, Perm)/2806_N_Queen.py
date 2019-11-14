import sys
sys.stdin = open('input.txt', 'r')

# Recursion, DFS
def N_queen(q_num):
    global cnt
    # 3. 재귀함수로 해결할 경우, 마지막 퀸까지 배치 완료 될 때까지 호출한다.
    if q_num == N:
        cnt += 1
        return

    # 4. 해당 번호의 퀸을 놓을 수 있는 자리를 확인한다.
    # 1번에서 배열(init_pos)의 인덱스는 퀸의 번호를 의미하는 동시에 행의 번호라고 했다.
    # 아래 for 루프의 q_num는 행의 번호라고 생각하면 된다.
    # 따라서, 0부터 시작이 아닌, 앞선 0, 1, 2..번 퀸들이 놓은 후, 이후의 q_num번 퀸을 q_num행에 놓는다고 생각하면 된다.
    # 즉, 같은 행에 퀸을 놓는 것을 피하는 것이다.
    for q_pos_check in range(q_num, N):

        # 5. 해당 자리에 놓을 수 없다면 다음 자리는 확인한다.
        if not check(q_num, q_pos_check):
            continue

        # DFS, Permutation
        # 6. q_num 번 퀸을 놓을 수 있을 자리(q_pos_check)가 존재한다면, 해당 q_num번 퀸이 그 자리를 갖도록 한다.
        # 그 자리를 갖도록 하기 위해, 원래 그 자리(q_pos_check)를 갖기로 예정되어 있었던 퀸과 자리를 서로 교환한다.
        queen_pos[q_num], queen_pos[q_pos_check] = queen_pos[q_pos_check], queen_pos[q_num]
        # 7. 다음 퀸을 배치하기 위해 재귀 호출을 한다.
        N_queen(q_num + 1)
        # 8. 6번에 배치한 자리 이외에도 다른 자리에도 올 수 있는지 계속 확인해야 하므로 원래대로 돌려놓고
        # for 문을 계속 돌면서 다른 자리도 확인한다.
        queen_pos[q_num], queen_pos[q_pos_check] = queen_pos[q_pos_check], queen_pos[q_num]

# (4)
def check(q_num, q_pos_check):
    # (4) 현재 퀸(q_num)과 앞서 놓인 퀸들을 비교한다.
    for pre_q in range(q_num):
        # 앞의 0, 1, 2... 행에 놓인 퀸과 현재 놓고자 하는 퀸의 행의 y축 차이와 x축 차이를 비교한다.
        # 현재 퀸의 행은 항상 이전의 퀸들의 행보다 크지만, x축 차이는 이전 퀸의 위치에 따라 클수도, 작을 수도있다.
        y_distance = q_num - pre_q
        x_distance = abs(queen_pos[q_pos_check] - queen_pos[pre_q])
        # 대각선에 놓인다는 의미는 곧 x, y축의 차이(거리)가 같다는 의미이다.
        if y_distance == x_distance:
            return False
    return True

testcase = int(input())

for test in range(testcase):
    N = int(input())

    # 1. N개의 Q을 각 행마다 0번째, 1번째, 2,3...번째에 임의로 배열한다.
    # queen_pos의 index는 각 Q의 번호인 동시에 행의 번호이고(Q의 번호=행의 번호),
    # queen_pos의 숫자가 각 번호의 Q가 배치된 열 위치이다.
    queen_pos = [i for i in range(N)]

    cnt = 0
    # 2. 0번 퀸부터 시작한다.
    N_queen(0)
    print('#{} {}'.format(test + 1, cnt))
