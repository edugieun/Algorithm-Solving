import sys
sys.stdin = open('sample_input.txt', 'r')

def cost(k, total):
    global min_cost
    if total < min_cost: min_cost = total
    for i in range(k, 12):
        if arr[i] and sum(arr[i:i + 3]) > tri:
            cost(i + 3, total - sum(arr[i:i + 3]) + tri)

T = int(input())
for t in range(1, T + 1):
    d, m, tri, year = map(int, input().split())
    min_cost = year
    arr = list(map(lambda x: min(int(x) * d, m), input().split())) + [0, 0]
    cost(0, sum(arr))
    print('#{} {}'.format(t, min_cost))