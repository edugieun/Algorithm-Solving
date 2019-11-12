import sys
sys.stdin = open('sample_input.txt', 'r')


class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoLast(data):
    global pHead
    if pHead == None:
        pHead = Node(data, None)
    else:
        p = pHead
        while p.link != None:
            p = p.link
        p.link = Node(data, None)

def numInsert(idx, data):
    global pHead
    if idx == 0:
        pHead = Node(data, pHead)
    else:
        p = pHead
        for i in range(idx - 1):
            p = p.link
        p.link = Node(data, p.link)

def idxDelete(idx):
    global pHead
    if idx == 0:
        pHead = pHead.link
    else:
        p = pHead
        for i in range(idx - 1):
            p = p.link
        p.link = p.link.link

def numChange(idx, data):
    global pHead
    if idx == 0:
        pHead = Node(data, pHead.link)
    else:
        p = pHead
        for i in range(idx - 1):
            p = p.link
        p.link = Node(data, p.link.link)

def result_get(idx):
    p = pHead
    for i in range(idx):
        if p.link == None:
            return -1
        p = p.link

    return p.data

test_case = int(input())
for test in range(test_case):
    N, M, L = map(int, input().split())
    num_list = list(map(int, input().split()))

    pHead = None

    for num in num_list:
        addtoLast(num)

    for order in range(M):
        state = list(map(str, input().split()))
        # Insert
        if state[0] == 'I':
            numInsert(int(state[1]), int(state[2]))
        # Delete
        elif state[0] == 'D':
            idxDelete(int(state[1]))
        # Change
        elif state[0] == 'C':
            numChange(int(state[1]), int(state[2]))

    result = result_get(L)
    print('#{} {}'.format(test+1, result))



