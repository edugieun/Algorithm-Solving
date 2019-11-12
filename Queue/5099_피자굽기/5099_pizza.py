import sys
sys.stdin = open('sample_input.txt', 'r')

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ele):
        self.queue.append(ele)

    def dequeue(self):
        if len(self.queue) < 1:
            print('empty')
            return False
        else:
            return self.queue.pop(0)

test_case = int(input())

for test in range(test_case):
    N, M = list(map(int, input().split()))

    left_pizza = [i for i in range(M)]
    Ci = list(map(int, input().split()))

    # 화덕 회전 구현
    oven = Queue()
    while 1:
        if len(left_pizza) != 0 and len(oven.queue) != N:
            pizza = left_pizza.pop(0)
            oven.enqueue(pizza)

        else:
            pizza = oven.dequeue()
            Ci[pizza] = Ci[pizza] // 2
            if Ci[pizza] != 0:
                oven.enqueue(pizza)

        if len(left_pizza) == 0 and len(oven.queue) == 1:
            break

    print('#{} {}'.format(test+1, oven.queue[0] + 1))

