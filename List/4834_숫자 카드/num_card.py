import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트케이스 개수
T = int(input())

for test in range(T):
    N = int(input()) # 뽑는 카드 개수
    n_cards = input() # 뽑은 카드들의 숫자나열(str)

    cards_dict = {} # 추후에 카드의 번호와 해당 카드의 개수를 담을 빈 딕셔너리 key: 카드 번호 / value: 개수

    # 카드숫자 나열의 숫자 하나씩 돌면서
    for n in n_cards:
        # 딕셔너리(cards_dict) value에 1 할당
        if n not in cards_dict.keys():
            cards_dict[n] = 1
        # 중복이 있다면 value+1
        else:
            cards_dict[n] = cards_dict.get(n) + 1

    # 가장 많은 카드 수 비교
    result_key, result_value = 0, 0 # 가장 큰 값을 담을 value와 key
    for key, value in cards_dict.items(): # 딕셔너리에서 key와 value를 뽑아 비교
        # 카드 수는 가장 많아야 하고, 카드 수가 같다면 key가 큰 수를 저장
        # 카드 수가 많다면 바로 저장
        if result_value < value:
            result_key, result_value = int(key), value
        # 카드 수가 같은 경우가 발생하면 키 값이 더 큰 쪽을 저장
        elif result_value == value:
            if result_key < int(key):
                result_key, result_value = int(key), value

    print('#{} {} {}'.format(test+1, result_key, result_value))