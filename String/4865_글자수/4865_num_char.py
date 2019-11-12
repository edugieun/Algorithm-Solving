import sys
sys.stdin = open("sample_input.txt", "r")


test_case = int(input())

for test in range(test_case):
    str1 = set(input())
    str2 = input()

    dict_str1 = {}
    for key in str1:
        dict_str1[key] = 0

    for char in str2:
        if char in dict_str1:
            dict_str1[char] = dict_str1.get(char) + 1

    print('#{} {}'.format(test+1, max(dict_str1.values())))
