# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# class Node:
#     def __init__(self, data, link):
#         self.data = data
#         self.link = link
#
# def addtoLast(data):
#     global Head
#     if Head == None:
#         Head = Node(data, None)
#     else:
#         pre = Head
#         while pre.link != None:
#             pre = pre.link
#         pre.link = Node(data, None)
#
# def add(idx, data):
#     global Head
#     pre = Head
#     if idx == 0:
#         Head = Node(data, pre)
#     else:
#         for i in range(idx - 1):
#             pre = pre.link
#         pre.link = Node(data, pre.link)
#
# def link_print(linked_list):
#     while linked_list.link != None:
#         print(linked_list.data, end=' ')
#         linked_list = linked_list.link
#     print(linked_list.data)
#
# def search_index(idx):
#     Head_tmp = Head
#     for i in range(idx):
#         Head_tmp = Head_tmp.link
#     return Head_tmp.data
#
#
# test_case = int(input())
# for test in range(test_case):
#     N, M, L = map(int, input().split())
#
#     num_list = list(map(int, input().split()))
#
#     Head = None
#     for i in range(len(num_list)):
#         addtoLast(num_list[i])
#
#     add_list = [list(map(int, input().split())) for i in range(M)]
#     for info in add_list:
#         add(info[0], info[1])
#
#     print('#{} {}'.format(test+1, search_index(L)))


# 선생님 풀이
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addLast(data):
    global pHead
    if pHead == Nonde:
        pHead = Node(data, None)
    else:
        p = pHead
        while p.link != None:
            p = p.link
        p.link = Node(data, None)
    return

def add(data, idx):
    global pHead
    p = pHead
    n = 0
    while n < idx - 1:
        p = p.link
        n += 1
    t = p.link
    p.link = Node(data, t)
    return

def get(idx):
    p = pHead
    n = 0
    while n < idx:
        p = p.link
        n += 1
    return p.data

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    pHead = None

    s = list(map(int, input).split())

