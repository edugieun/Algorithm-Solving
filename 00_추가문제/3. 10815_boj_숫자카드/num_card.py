import sys
import time

start = time.time()

sys.stdin = open("input.txt", "r")

N = input()
N_cards = set(input().split()) # 아무것도 안쓰거나, list는 시간초과. set만 써야 됨. set은 순서를 보장하지 않아 시간 복잡도가 적음
print(N_cards)
M = input()
M_cards = input().split()
print(M_cards)
for M_card in M_cards:
    
    if M_card in N_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')

print(time.time() - start)


