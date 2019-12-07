import sys
sys.stdin = open('input.txt', 'r')


def mergeSort(lo, hi):  # 매개변수 --> 문제의 크기
    global cnt
    if lo == hi: return

    # 분할
    mid = (lo + hi - 1) >> 1
    mergeSort(lo, mid)  # 왼쪽
    mergeSort(mid + 1, hi)  # 오른쪽
    # 왼쪽과 오른쪽을 병합
    i, j, k = lo, mid + 1, lo

    if arr[mid] > arr[hi]:
        cnt += 1

    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]



test_case = int(input())

for test in range(test_case):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N

    cnt = 0
    mergeSort(0, len(arr) - 1)
    print('#{} {} {}'.format(test+1, arr[N//2], cnt))
