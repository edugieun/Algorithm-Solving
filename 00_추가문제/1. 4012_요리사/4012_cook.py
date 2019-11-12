import sys
from pprint import pprint
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for test in range(test_case):

    N = int(input())
    synergy_matrix = [list(map(int, input().split())) for i in range(N)]
    min_sum = 0

    for set in range(1 << N):
        A, B = [], []
        for i in range(N):
            if set & (1 << i):
                A.append(i)
            else:
                B.append(i)
        if len(A) == len(B):
            a_synergy_sum = 0
            b_synergy_sum = 0

            for j in range(len(A) - 1):
                for k in range(j, len(A) - 1):
                    a_synergy_sum += synergy_matrix[A[j]][A[k+1]] + synergy_matrix[A[k+1]][A[j]]
                    b_synergy_sum += synergy_matrix[B[j]][B[k+1]] + synergy_matrix[B[k+1]][B[j]]
            if min_sum == 0:
                min_sum = abs(a_synergy_sum - b_synergy_sum)
            if min_sum > abs(a_synergy_sum - b_synergy_sum):
                min_sum = abs(a_synergy_sum - b_synergy_sum)
                if min_sum == 0:
                    break


    print('#{} {}'.format(test + 1, min_sum))