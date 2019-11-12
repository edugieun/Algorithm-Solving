import sys
sys.stdin = open("input.txt", "r")


code = 'ABCDEFGHIJKLNMOPQRSTUVWXYZ'

test_case = int(input())

for test in range(test_case):

    num_alpha = int(input())

    # dictionary에 저장
    zip_dict = {}
    for i in range(num_alpha):
        key, value = map(str, input().split())
        value = int(value)
        zip_dict[key] = value


    count = 0

    print('#{} '.format(test + 1))

    # code에서 차례대로 알파벳을 선택하면서
    for char in code:
        # 딕셔너리에 알파벳이 있으면
        if char in zip_dict:
            # 바로 print
            for i in range(zip_dict.get(char)):
                print(char, end='')
                count += 1
                if count == 10:
                    print()
                    count = 0

    print()


