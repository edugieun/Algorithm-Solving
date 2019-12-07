# 선생님 풀이 : 원형 연결 리스트
class Node:
    def __init__(self, data, pre, link):
        self.data = data
        self.pre = pre
        self.link = link

def addLast(data):
    global pHead
    if pHead == None:
        pHead = Node(data, None, None)
        pHead.pre = pHead
        pHead.link = pHead
    else:
        p = pHead.pre
        p.link = Node(data, p, pHead)
        pHead.pre = p.link
    return

def addNumbers():
    global pHead

    p = pHead
    for j in range(K):
        for i in range(M):
            p = p.link
        p.pre.link = Node(p.pre.data + p.data, p.pre, p)
        p.pre = p.pre.link
        p = p.pre
    return


def get():
    global pHead
    p = pHead.pre
    for i in range(10):
        print(p.data, end='')
        p = p.pre
        if p == pHead.pre:
            break
    print()