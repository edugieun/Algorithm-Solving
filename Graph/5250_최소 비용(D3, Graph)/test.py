import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    c = (0,0)
    dx = [1,0]
    dy = [0,1]
    lim = 2000
    dp = [[lim] * n for _ in range(n)]
    vis = [[False]*n for _ in range(n)]
    dp[0][0] = 0
    vis[0][0] = True
    stk = [c]
    while stk:
        c = stk.pop(0)
        now_w = dp[c[0]][c[1]]
        for d in range(2):
            nc = c[0]+dx[d], c[1]+dy[d]
            if nc[0]<n and nc[1] < n:
                h_sub = 0 if arr[nc[0]][nc[1]] <= arr[c[0]][c[1]] else arr[nc[0]][nc[1]] - arr[c[0]][c[1]]
                if dp[nc[0]][nc[1]] > now_w + 1 + h_sub:
                    dp[nc[0]][nc[1]] = now_w + 1 + h_sub
                    stk.append(nc)
        vis[c[0]][c[1]] = True
    print('#{} {}'.format(test_case, dp[-1][-1]))