import sys
sys.stdin = open("sample_input.txt", "r")


test_case = int(input())

for test in range(test_case):
    str1 = input()
    str2 = input()

    for idx in range(len(str2)):
        if str1 == str2[idx:idx + len(str1)]:
            print('#{} 1'.format(test+1))
            break
    else:
        print('#{} 0'.format(test+1))
