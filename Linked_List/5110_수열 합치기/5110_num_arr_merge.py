
## 10개중 9개 성공 : 시간초과.
# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# class Node:
#     def __init__(self, data, link):
#         self.data = data
#         self.link = link
#
# class Llist:
#
#     def __init__(self):
#         self.Head = None
#
#     def addtoLast(self, data):
#         if self.Head == None:
#             self.Head = Node(data, None)
#         else:
#             pre = self.Head
#             while pre.link != None:
#                 pre = pre.link
#             pre.link = Node(data, None)
#
#     def add(self, idx, data):
#         pre = self.Head
#         if idx == 0:
#             Head = Node(data, pre)
#         else:
#             for i in range(idx - 1):
#                 pre = pre.link
#             pre.link = Node(data, pre.link)
#
#     def link_print(self):
#         num_list = []
#         tmp_head = self.Head
#         a = []
#         while tmp_head != None:
#             a.append(tmp_head.data)
#             tmp_head = tmp_head.link
#         return a
#
#
#     def search_index(self, idx):
#         Head_tmp = self.Head
#         for i in range(idx):
#             Head_tmp = Head_tmp.link
#         return Head_tmp.data
#
# def merge(target):
#
#     if target.Head.data < L1.Head.data:
#         tmp2 = target.Head.link
#         for i in range(N-2):
#             tmp2 = tmp2.link
#         tmp2.link = L1.Head
#         L1.Head = target.Head
#         return None
#
#
#     target.Head.data
#     tmp = L1.Head
#
#     while tmp.link != None:
#         if tmp.link.data > target.Head.data:
#             tmp2 = target.Head.link
#             for i in range(N-2):
#                 tmp2 = tmp2.link
#             tmp2.link = tmp.link
#             tmp.link = target.Head
#             break
#         tmp = tmp.link
#     else:
#         tmp.link = target.Head
#
# test_case = int(input())
#
# for test in range(test_case):
#     N, M = map(int, input().split())
#
#     arr_list = [list(map(int, input().split())) for i in range(M)]
#
#     L1 = Llist()
#     a = arr_list[0]
#     for i in range(len(a)):
#         L1.addtoLast(a[i])
#
#     for i in range(1, len(arr_list)):
#         target = Llist()
#         arr = arr_list[i]
#         for j in range(len(arr)):
#             target.addtoLast(arr[j])
#         merge(target)
#     a = L1.link_print()
#     print('#{} '.format(test + 1), end='')
#     for i in range(1, 11):
#         print(a[-i], end=' ')
#     print()

# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# class Node:
#     def __init__(self, data, nxt, prev):
#         self.data = data
#         self.nxt = nxt
#         self.prev = prev
#
# class Llist:
#
#     def __init__(self):
#         self.Head = None
#         self.tail = None
#
#     def addtoLast(self, data):
#         if self.Head == None:
#             self.Head = Node('head', None, None)
#             self.tail = Node('tail', None, None)
#         else:
#             new_node = Node(data, None, None)
#             new_node.nxt = self.tail
#             self.tail.prev = new_node
#
#             next_node = self.Head
#             while next_node.nxt != 'tail':
#                 next_node = next_node.nxt
#             new_node.prev = next_node
#             next_node.nxt = new_node
#
#     def link_print(self):
#         num_list = []
#         tmp_head = self.Head
#         a = []
#         while tmp_head != None:
#             a.append(tmp_head.data)
#             tmp_head = tmp_head.link
#         return a
#
# def merge(target):
#
#     if target.Head.data < L1.Head.data:
#         tmp2 = target.Head.link
#         for i in range(N-2):
#             tmp2 = tmp2.link
#         tmp2.link = L1.Head
#         L1.Head = target.Head
#         return None
#
#
#     target.Head.data
#     tmp = L1.Head
#
#     while tmp.link != None:
#         if tmp.link.data > target.Head.data:
#             tmp2 = target.Head.link
#             for i in range(N-2):
#                 tmp2 = tmp2.link
#             tmp2.link = tmp.link
#             tmp.link = target.Head
#             break
#         tmp = tmp.link
#     else:
#         tmp.link = target.Head
#
# test_case = int(input())
#
# for test in range(test_case):
#     N, M = map(int, input().split())
#
#     arr_list = [list(map(int, input().split())) for i in range(M)]
#
#     L1 = Llist()
#     a = arr_list[0]
#     for i in range(len(a)):
#         L1.addtoLast(a[i])
#
#     for i in range(1, len(arr_list)):
#         target = Llist()
#         arr = arr_list[i]
#         for j in range(len(arr)):
#             target.addtoLast(arr[j])
#         merge(target)
#     a = L1.link_print()
#     print('#{} '.format(test + 1), end='')
#     for i in range(1, 11):
#         print(a[-i], end=' ')
#     print()


import sys
sys.stdin = open('sample_input.txt', 'r')

# 선생님 풀이 : 이중 연결 리스트
class Node:
    def __init__(self, data, pre, link):
        self.data = data
        self.pre = pre
        self.link = link

def addLast(data):
    global pHead
    global pTail
    if pHead == None:
        pHead = Node(data, None, None)
        pTail = pHead
    else:
        p = pHead
        while p.link != None:
            p = p.link
        p.link = Node(data, p, None)
        pTail = p.link
    return


def addNumbers():
    global pHead
    global pTail
    p = pHead
    if p == None:
        for i in range(N):
            addLast(s[i])
    else:
        while p.link != None and p.data <= s[0]:
            p = p.link
        if p.data > s[0]:
            if p.pre == None:
                p.pre = Node(s[0], None, p)
                pHead = p.pre
                for i in range(1, N):
                    p.pre.link = Node(s[i], p.pre, p)
                    p.pre = p.pre.link
            else:
                for i in range(N):
                    p.pre.link = Node(s[i], p.pre, p)
                    p.pre = p.pre.link
        else:
            for i in range(N):
                addLast(s[i])
    return

def get():
    global pTail
    p = pTail
    for i in range(10):
        print(p.data, end='')
        p = p.pre
    print()

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pHead = None
    pTail = None
    for i in range(M):
        s = list(map(int, input().split()))
        addNumbers()
        print('#{}'.format(tc), end='')
        get()
