import sys
sys.stdin = open('sample_input.txt', 'r')

test_case = int(input())

for test in range(test_case):
    cards = list(map(int, input().split()))

    card_dict_A = {}
    card_dict_B = {}
    for i in range(10):
        card_dict_A[i] = 0
        card_dict_B[i] = 0

    for i in range(len(cards)):
        if i % 2 == 0:
            card_dict_A[cards[i]] += 1
            if card_dict_A[cards[i]] == 3:
                print('#{} 1'.format(test + 1))
                break
            triplet = 0
            cnt = 0
            for value in card_dict_A.values():
                if value != 0:
                    cnt += 1
                    if cnt == 3:
                        triplet = 1
                        print('#{} 1'.format(test + 1))
                else:
                    cnt = 0

        else:
            card_dict_B[cards[i]] += 1
            if card_dict_B[cards[i]] == 3:
                print('#{} 2'.format(test + 1))
                break

            cnt = 0
            for value in card_dict_B.values():
                if value != 0:
                    cnt += 1
                    if cnt == 3:
                        triplet = 1
                        print('#{} 2'.format(test + 1))
                else:
                    cnt = 0

        if triplet == 1:
            break

    else:
        print('#{} 0'.format(test + 1))