
import sys

sys.stdin = open("sample_input.txt", "r")

test_case = int(input())

for test in range(test_case):

    word = input()  # 단어
    word_len = len(word)  # 단어 길이

    # 팬린드룸 검사
    for start in range(word_len // 2):
        end = -(start + 1)
        # 양쪽이 같거나,
        if (word[start] == word[end]):
            continue
        # 그전까진 양쪽이 같다가, 갑자기 *을 만남. 그럼 게임 끝. 무조건 있음.
        elif (word[start] == '*') or (word[end] == '*'):
            print('#{} Exist'.format(test + 1))
            break
        # 그렇지 않은 경우는 not 팰린드룸
        else:
            print('#{} Not exist'.format(test + 1))
            break

    else:
        print('#{} Exist'.format(test + 1))
