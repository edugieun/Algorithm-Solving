import sys
sys.stdin = open('input.txt', 'r')

test_case = 10
for test in range(test_case):
    V, E = list(map(int, input().split()))
    nodes = list(map(int, input().split()))

    # in은 0으로 초기화, 아웃은 리스트 만들기
    nodes_dict = {i: [0, []] for i in range(1, V+1)}

    for i in range(E):
        # out target 리스트에 넣고
        nodes_dict[nodes[i * 2]][1] += [nodes[i*2 + 1]]
        # in 개수는 1씩 증가
        nodes_dict[nodes[i*2 + 1]][0] += 1

    work_order = []
    while 1:

        for number in nodes_dict:
            if nodes_dict[number][0] == 0:
                work_order.append(number)
                nodes_dict[number][0] -= 1
                for next_number in nodes_dict[number][1]:
                    nodes_dict[next_number][0] -= 1

        if len(work_order) == V:
            break

    work_order = ' '.join(list(map(str, work_order)))
    print('#{} {}'.format(test+1, work_order))




#
# def find_next():
#     for now in range(1, V + 1):
#         if work[now][0] == 0:
#             return now
#
# for test in range(1):
#     V, E = map(int, input().split())
#     work = {k: [0, []] for k in range(1, V + 1)}
#     lines = list(map(int, input().split()))
#     for i in range(0, len(lines), 2):
#         work[lines[i]][1].append(lines[i + 1])
#         work[lines[i + 1]][0] += 1
#
#     while 1:
#         now = find_next()
#         if now == None:
#             break
#         print(now, end=' ')
#         work[now][0] -= 1
#         for next in work[now][1]:
#             work[next][0] -= 1
#     print()


"""
for x in range(1, 2): 
    # n = 숫자 종류, b = 노드 개수
    n, b = map(int, input().split())  
    # l = 노드
    l = list(map(int, input().split()))   

    m = [[] for i in range(n)] 
    s = []
    for i in range(len(l)//2):  
        m[l[2*i+1]-1] = m[l[2*i+1]-1] + [l[2*i]]

    while len(s) < n:
        for i in range(len(m)):
            if m[i] == [] and i + 1 not in s:
                for j in m:
                    if i+1 in j:
                        j.remove(i+1)
                s += [i+1]
    print("#" + str(x), s)
"""