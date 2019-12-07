import sys
sys.stdin = open("GNS_test_input.txt", "r")

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

test_case = int(input())

for test in range(test_case):
    num_array = int(input()[3:]) # input 파일에서 #1 를 제외한 뒤에 숫자들의 개수만 가져옴.
    strings = list(map(str, input().split()))

    order_string = []

    # ZRO 부터 비교하면서
    for number in numbers:

        for str_number in strings:
            # 같은 숫자가 있으면 새로운 리스트에 넣어버림
            if str_number == number:
                order_string.append(number)

    print('#{} {}'.format(test + 1, ' '.join(order_string)))

"""
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

strings = ['TWO', 'NIN', 'TWO', 'TWO', 'FIV', 'FOR']

order_string = []

for number in numbers:

    for str_number in strings:
        if str_number == number:
            order_string.append(number)

print(order_string)
"""