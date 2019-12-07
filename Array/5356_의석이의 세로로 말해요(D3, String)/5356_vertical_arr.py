import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    word_list = [input() for i in range(5)]
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    cnt = 0
    print('#{} '.format(test + 1), end='')
    for i in range(max_length):
        for word in word_list:
            if len(word) - 1 >= cnt:
                print(word[cnt], end='')
        cnt += 1

    print(

# 선생님 코드
#
# for i in range(ml):
#     for j in range(5):
#         # 문자열이 짧은 경우 처리 방법
#         if l[j] > i:
#             temp += s[j][i]
# print(~~)