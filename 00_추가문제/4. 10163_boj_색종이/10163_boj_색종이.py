import sys
sys.stdin = open("input.txt", "r")

#색종이 개수
num_papers = int(input())

# 101 x 101 2차 배열 생성
matrix_101 = []
for i in range(101):
    tmp = []
    for j in range(101):
        tmp.append(0)
    matrix_101.append(tmp)

# 불러오는 색종이 영역을 순서에 따른 숫자로 채운다.
for paper in range(1, num_papers + 1):
    x1, y1, width, height = map(int, input().split())

    for row in range(height):
        for col in range(width):
            matrix_101[row + y1][col + x1] = paper

# matrix_101 배열에 채워진 각각의 숫자의 개수를 읽어 출력한다.
for i in range(1, num_papers + 1):
    tmp_sum = 0
    for j in matrix_101:
        tmp_sum += j.count(i)
    
    print(tmp_sum)