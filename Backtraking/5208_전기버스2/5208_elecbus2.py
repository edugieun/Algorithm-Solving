import sys
sys.stdin = open('input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    info = list(map(int, input().split()))
    final_station = info[0]
    capa_dict = {i:info[i] for i in range(1, final_station)}

    now_station = 1
    cnt = 0
    while 1:
        max_station = 0
        for move in range(1, capa_dict[now_station] + 1):
            next_station_tmp = now_station + move
            next_capa = capa_dict[next_station_tmp]
            max_station_tmp = next_capa + next_station_tmp

            if max_station_tmp > max_station:
                max_station = max_station_tmp
                next_station = next_station_tmp

        now_station = next_station
        cnt += 1
        if (now_station+capa_dict[now_station]) >= final_station:
            break

    print('#{} {}'.format(test+1, cnt))
