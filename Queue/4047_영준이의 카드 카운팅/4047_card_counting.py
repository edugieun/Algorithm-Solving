import sys
sys.stdin = open('sample_input.txt', 'r')

card_shapes = ['S', 'D', 'H', 'C']

test_case = int(input())

for test in range(test_case):
    jun_cards = input()

    card_dict = {}
    for shape in card_shapes:
        card_dict[shape] = [0, []]
    needs = []
    for i in range(len(jun_cards)//3):
        if jun_cards[i*3] in card_dict:
            card_dict[jun_cards[i*3]][0] += 1
            card_num = int(jun_cards[i * 3 + 1:i * 3 + 3])
            if card_num in card_dict[jun_cards[i * 3]][1]:
                print('#{} ERROR'.format(test + 1))
                break
            else:
                card_dict[jun_cards[i * 3]][1] += [card_num]
    else:
        for card_number in card_dict:
            needs.append(13 - card_dict[card_number][0])
        print('#{} {}'.format(test+1, ' '.join(list(map(str, needs)))))
