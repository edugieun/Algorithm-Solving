import sys
sys.stdin = open('input.txt', 'r')

for test in range(10):
    dump_num = int(input()) # 덤프 횟수
    box_list = list(map(int, input().split())) # 박스들의 높이를 담은 리스트

    # 반복문에서 상자의 최대, 최소 높이를 갖는 column의 인덱스를 담을 변수(인덱스. 초기 0으로 설정)
    min_col_num = 0
    max_col_num = 0

    ## 1. 덤프 횟수를 반복하면서
    for dum_count in range(dump_num):

        ## 2. 매 회 덤프 마다 인덱스를 이용하여 리스트의 최대 최소 상자 높이를 찾고
        for box_col_num in range(len(box_list)): 
            # 선택한 column이 max_col보다 같거나 크다면 옮겨담고
            if box_list[box_col_num] > box_list[max_col_num]:
                max_col_num = box_col_num
            # 동시에 min_col보다 작거나 같다면 옮겨 담아
            if box_list[box_col_num] < box_list[min_col_num]:
                min_col_num = box_col_num

        ## 3. 최대 길이의 column은 -1을, 최소 column +1을 해줘
        box_list[max_col_num] -= 1
        box_list[min_col_num] += 1
    
    ## 4. 만약, 2번 마지막 과정에서 같은 값이 존재할 경우 3번을 시행하고 나오면 올바른 최대, 최소 값이 아니다.
    ##    그러므로 마지막으로 한번도 최대 최소를 검사해준다.
    ## (이 부분을 처리하는 더 좋은 방법이 없을까.)
    for box_col_num in range(len(box_list)): 
            # 선택한 column이 max_col보다 같거나 크다면 옮겨담고
            if box_list[box_col_num] > box_list[max_col_num]:
                max_col_num = box_col_num
            # 동시에 min_col보다 작거나 같다면 옮겨 담아
            if box_list[box_col_num] < box_list[min_col_num]:
                min_col_num = box_col_num

    result = box_list[max_col_num] - box_list[min_col_num]

    print('#{} {}'.format(test + 1, result))

"""
### 다른 방법(비교 대상이 많아지면 이 방법이 더 효율적)
### 처음부터 모든 블록의 개수를 카운팅한다.
for test_case in randge(1, 11):
dump = int(input())
arr = list(map~~)


cnt = [0] * 101 # 빈도수 저장하는 List
for val in arr:
cnt[val] += 1

minIdx, maxIdx = 0, 100

i = 0
while i < dump:
    while cnt[minIdx] == 0:
    minIdx += 1
    while cnt[maxIdx] == 0:
    maxIdx -= 1
    
    cnt[minIdx] -= 1
    cnt[minIdx + 1] += 1
    cnt[maxIdx] -= 1
    cnt[maxIdx - 1] += 1
    i += 1
    
if xnt[minIdx] == 0: minIdx += 1
if cnt[maxIdx] == 0: maxIdx -= 1
    
print(~~~max-min~~)
"""
