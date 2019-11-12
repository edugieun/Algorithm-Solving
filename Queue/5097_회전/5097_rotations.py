import sys
sys.stdin = open('sample_input.txt', 'r')

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ele):
        self.queue.append(ele)
        return None

    def dequeue(self):
        if len(self.queue) < 1:
            print("Empty")
            return False
        else:
            return self.queue.pop(0)


test_case = int(input())

for test in range(test_case):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    q1 = Queue()
    for number in numbers:
        q1.enqueue(number)

    for i in range(M):
        first_ele = q1.dequeue()
        q1.enqueue(first_ele)

    print('#{} {}'.format(test + 1, q1.queue[0]))