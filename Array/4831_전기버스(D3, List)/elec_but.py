import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) # T: 노선 수

for line in range(T):
    # K: 최대 이동 가능 거리
    # N: 종점
    # M: 충전소 개수
    K, N, M = list(map(int, input().split()))
    stations = list(map(int, input().split())) # stations: 충전소가 존재하는 번호
    recent_location = 0 # 현재 위치.
    charge_cnt = 0 # 충전 횟수.
    fail = 0 # 충전 실패를 나타낼 변수. fail = 1이면 충전 실패

    # 현재 위치가 N-K 보다 커지거나(즉, 충전 없이 갈 수 있는 거리), 또는 fail이 1이면 탈출
    while recent_location < (N - K) and fail == 0:

        # K 이내 거리에 충전소가 있는지 확인. 충전을 최소로 해야하니 먼쪽부터 확인.
        for j in range(K, 0, -1): # 이 때, j는 충전소까지의 거리
            # 충전소가 없다면 fail = 1.
            if (recent_location + j) not in stations:
                fail = 1
            # 있다면, 이 때의 이동거리 j
            else:
                fail = 0 # fail은 다시 충전소가 있음을 나타내는 0으로 바꿔줌
                recent_location += j # 현재 위치에서 충전소까지 거리(j) 만큼 이동 후
                charge_cnt += 1 # 충전
                break # 충전을 했으니 다시 최대이동거리를 확보. 다시 가장 먼 충전소를 찾는다.

    # fail이 1이 되기 전에 이미 count된 충전소가 있음.
    # 최종 결과 출력 전 fail이 1이면 카운트는 다시 0
    if fail == 1:
        charge_cnt = 0

    print('#{} {}'.format(line+1, charge_cnt))


"""
### 다른 방법

arr = [0] + list(map(in~~~) + [N]

ans = bus = 0

for i in range(1, M + 2):
    if arr[i] - arr[i - 1] > K:
        and = 0
        break
    if arr[i] > bus + K:
        bus = arr[i - 1]
        ans += 1
"""