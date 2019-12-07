import sys
sys.stdin = open('sample_input.txt', 'r')

horizon_n, vertical_n = map(int, input().split())
cut_N = int(input())

horizon_cut = [0, vertical_n]
vertical_cut = [0, horizon_n]
for i in range(cut_N):
    tmp = list(map(int, input().split()))
    if tmp[0]:
        vertical_cut.append(tmp[1])
    else:
        horizon_cut.append(tmp[1])

vertical_cut = sorted(vertical_cut)
horizon_cut = sorted(horizon_cut)

vertical_max = 0
horizon_max = 0
for i in range(len(horizon_cut) - 1):
    if vertical_max < (horizon_cut[i+1] - horizon_cut[i]):
        vertical_max = (horizon_cut[i+1] - horizon_cut[i])
for i in range(len(vertical_cut) - 1):
    if horizon_max < (vertical_cut[i+1] - vertical_cut[i]):
        horizon_max = (vertical_cut[i+1] - vertical_cut[i])

print(vertical_max*horizon_max)