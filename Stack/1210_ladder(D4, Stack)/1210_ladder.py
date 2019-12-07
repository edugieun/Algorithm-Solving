import sys; sys.stdin = open('input.txt', 'r')
from pprint import pprint


def DFS(x, y):
    if x == 0: return y
    arr[x][y] = 0 # 길 지우기
    if y - 1 >= 0 and arr[x][y - 1]:
        return DFS(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        return DFS(x, y + 1)
    else:
        return DFS(x - 1, y)




for test in range(10):

    test_case_number = int(input())

    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    x, y = 99, 0
    for i in range(100):
        if arr[99][i] == 2:
            y = i
            break


    print('#{} {}'.format(test + 1, DFS(x, y)))

"""
## 강사님 풀이
# 방법 1
N = input()
arr = list~~

x, y= 99, 0
for i in range(100):
    if arr[99][i] == 2:
        y = i
        break

dir = 0     # 0: 위, 1: 왼쪽, 2: 오른쪽
while x: # x가 0이 되면 종료
    if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
        y, dir = y - 1, 1
    elif dir != 1 and y + 1 < 100 and arr[x][y +?-? 1]:
        y, dir = y + 1, 2
    else:
        x, dir = x - 1, 0

# 방법 2
dir = 0
while x:
    if y - 1 >= 0 and arr[x][y - 1]:
        while y - 1 >= 0 and arr[x][y - 1]:
            y -= 1
        x -= 1
        elif y + 1 < 100 and arr[x][y + 1]:
            while y + 1 < 100 and arr[x][y + 1]:
                y += 1
            x -= 1
        else:
            x -= 1


# 방법 3
def DFS(x, y):
    if x == 0: return y
    arr[x][y] = 0 # 길 지우기
    if y - 1 >= 0 and arr[x][y - 1]:
        return DFS(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        return DFS(x, y + 1)
    else:
        return DFS(x - 1, y)


print(DFS(x, y))
"""