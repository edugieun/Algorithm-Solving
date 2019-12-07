# 서버 제출할 때는 아래 두 둘은 빼야됨.
import sys
# input.txt 파일을 읽어 stdin(standard input으로 간주)
sys.stdin = open("input.txt", "r")
####

for j in range(10):
    t_length = int(input()) # test case 길이
    bd_location = list(map(int, input().split())) # building 위치(=idx)와 높이

    result = 0
    next_top = 0
    next_top1 = 0
    next_top2 = 0

    for i in range(t_length):
        # 가장자리 처리
        if i < 2 or i > (t_length-3):
            continue

        difference = 0

        # 양옆 1번째 칸 먼저 확인
        if bd_location[i] > bd_location[i - 1] and bd_location[i] > bd_location[i + 1]:
            # 둘 중 더 큰 값 확인
            if bd_location[i - 1] > bd_location[i + 1]:
                next_top1 = bd_location[i - 1]
            else:
                next_top1 = bd_location[i + 1]

            # 양옆 2번째 칸 확인
            if bd_location[i] > bd_location[i - 2] and bd_location[i] > bd_location[i + 2]:
                if bd_location[i - 2] > bd_location[i + 2]:
                    next_top2 = bd_location[i - 2]
                else:
                    next_top2 = bd_location[i + 2]

                # 기준 빌딩 제외한 양쪽 4개 건물 중 최대값
                if next_top1 > next_top2:
                    next_top = next_top1
                else:
                    next_top = next_top2
                
                # 기준 빌딩과의 차이
                difference = bd_location[i] - next_top
                result += difference
    print('#{} {}'.format(j + 1, result))

        

## 풀이
"""
for n in range(10):
    N = int(input())
    num = list(map(int, input().split()))

    result = 0
    for i in range(2, N-1):
        MAX = max(num[i-2], num[i-1], num[i+1], num[i+2])
        if MAX < num[i]:
            result += num[i] - MAX
"""
            