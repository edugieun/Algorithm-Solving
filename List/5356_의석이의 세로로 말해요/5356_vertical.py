import sys
sys.stdin = open('input.txt', 'r')

testcase = int(input())
for test in range(testcase):
    max_len = 0
    words = []
    for i in range(5):
        word = input()
        if len(word) > max_len:
            max_len = len(word)
        words.append(word)

    tmp_word = ''
    for i in range(max_len):
        for word in words:
            if len(word) > i:
                tmp_word += word[i]
    print('#{} {}'.format(test+1, tmp_word))