import sys
sys.stdin = open('input.txt', 'r')

testcase = int(input())

for test in range(testcase):
    N, M, X = map(int, input().split())
    G = [[] for _ in range(N + 1)]