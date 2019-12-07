import sys
sys.stdin = open('input.txt', 'r')


def quickSort(lo, hi):
    if lo >= hi: return

    # partition
    i, j, pivot = lo, hi, arr[lo]
    while i < j:
        while i <= hi and pivot >= arr[i]: i += 1
        while pivot < arr[j]: j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]

    quickSort(lo, j - 1)
    quickSort(j + 1, hi)


test_case = int(input())

for test in range(test_case):
    N = int(input())
    arr = list(map(int, input().split()))

    quickSort(0, len(arr) - 1)
    print('#{} {}'.format(test + 1, arr[N//2]))