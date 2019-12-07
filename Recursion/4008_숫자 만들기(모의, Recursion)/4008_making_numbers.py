import sys
sys.stdin = open('input.txt', 'r')

# Recursion
def cal(tmp_sum, idx):
    global  op_num, min_result, max_result
    if idx == N:
        if tmp_sum < min_result:
            min_result = tmp_sum
        if tmp_sum > max_result:
            max_result = tmp_sum
        return
    if op_num[0] > 0:
        op_num[0] -= 1
        cal(tmp_sum + num_cards[idx], idx + 1)
        op_num[0] += 1
    if op_num[1] > 0:
        op_num[1] -= 1
        cal(tmp_sum - num_cards[idx], idx + 1)
        op_num[1] += 1
    if op_num[2] > 0:
        op_num[2] -= 1
        cal(tmp_sum * num_cards[idx], idx + 1)
        op_num[2] += 1
    if op_num[3] > 0:
        op_num[3] -= 1
        cal(int(tmp_sum / num_cards[idx]), idx + 1)
        op_num[3] += 1

ops = ['+', '-', '*', '/']

testcase = int(input())

for test in range(testcase):
    N = int(input())
    op_num = list(map(int, input().split()))
    num_cards = list(map(int, input().split()))
    min_result = 100000000
    max_result = -100000000
    cal(num_cards[0], 1)

    print('#{} {}'.format(test+1, max_result-min_result))