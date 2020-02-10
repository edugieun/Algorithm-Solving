import sys
sys.stdin = open('input.txt', 'r')


def dfs(idx, cnt, processor, summ):
    # idx: cores를 순서대로 보기 위한 idx
    # cnt: 코어 수
    # processor: 프로세서 수
    # summ: 전선 길이
    global m_core, m_line

    # 작업 종료 시 - 백트래킹
    if cnt == len(cores):
        # 최대 코어 설치 시 최소 전선 개수 구하기
        if processor > m_core:
            # 현재 설치된 프로세서 수가
            # 현재까지 알고 있던 최대 설치 프로세서 수보다 크다면
            # 최대 설치 프로세서 수와 최대 전선 수를 갱신한다
            m_core = processor
            m_line = summ
        elif processor == m_core:
            # 현재 설치된 프로세서 수가
            # 현재까지 알고 있던 초대 설치 프로세서 수와 같다면
            # 최대 설치 프로세서 수를 갱신하고,
            # 최대 전선 수는
            # 현재까지 알고 있는 최대 전선 수와
            # 지금까지 사용된 전선 수 중
            # 최소값으로 갱신한다
            m_core = processor
            m_line = min(m_line, summ)

        return

    # 프로세서를 추가 설치하는 경우
    for dx, dy in delta:
        tmp = []
        is_edge = False

        x, y = cores[idx]
        while True:
            # 가장자리
            if x == 0 or y == 0 or x == N - 1 or y == N - 1:
                is_edge = True
                break

            # 가장자리가 아닌 경우 해당 위치를 따라 이동
            x += dx
            y += dy

            # 해당 위치에 설치 가능하다면
            if arr[x][y] == 0:
                # 위치 정보 저장
                tmp.append((x, y))
            # 아니면 loop 종료
            else: break

        # 가장자리를 다녀갔다면
        if is_edge:
            ts = len(tmp)
            for m in range(ts):
                # 2: 전선 설치
                arr[tmp[m][0]][tmp[m][1]] = 2

            # 재귀 실시
            dfs(idx + 1, cnt + 1, processor + 1, summ + ts)

            # 재귀가 끝나면 원상 복구
            for m in range(ts):
                arr[tmp[m][0]][tmp[m][1]] = 0

    # 설치하지 않는 경우
    dfs(idx + 1, cnt + 1, processor, summ)


delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
TCs = int(input())
for T in range(1, TCs + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    for i in range(N):
        for j in range(N):
            # 코어를 발견하면 가장자리에 위치해 전기가 연결된 것을 제외한 나머지의 해당 위치를 저장한다.
            if arr[i][j] == 1:
                if 0 < i < N - 1 and 0 < j < N - 1:
                    cores.append((i, j))

    m_core, m_line = 0, 0xffff
    dfs(0, 0, 0, 0)

    print('#{} {}'.format(T, m_line))
