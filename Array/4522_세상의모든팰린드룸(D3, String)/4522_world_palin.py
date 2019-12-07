import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for test in range(test_case):

    word = input() # 단어
    word_len = len(word) # 단어 길이

    # 팬린드룸 검사
    for start in range(word_len // 2):
        end = -(start + 1)
        # 양쪽이 같거나, 양쪽 한 곳에 ?가 있으면 팰린드룸
        if (word[start] == word[end]) or (word[start] == '?') or (word[end] == '?'):
            continue
        
        # 그렇지 않은 경우는 not 팰린드룸
        else:
            print('#{} Not exist'.format(test + 1))
            break

    else:
        print('#{} Exist'.format(test + 1))
