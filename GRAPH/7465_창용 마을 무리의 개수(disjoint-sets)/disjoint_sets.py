import sys
sys.stdin = open('input.txt', 'r')

# disjoint-sets
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    p = [x for x in range(V + 1)] # 정점의 번호 1 ~V

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    ans = V
    for _ in range(E):
        u, v = map(int, input().split())
        a = find_set(u); b = find_set(v)
        if a == b: continue
        p[b] = a
        ans -= 1

    print('#{} {}'.format(tc, ans))