import sys
sys.stdin = open('sample_input.txt' , 'r')

def seperation():
    global people
    tmp = []
    tmp.append(people[0:(len(people) - 1) // 2 + 1])
    tmp.append(people[(len(people) - 1) // 2 + 1:])
    people = tmp

    while len(tmp[0]) > 2:
        tmp = []
        for i in people:
            tmp.append(i[0:(len(i)-1)//2 + 1])
            tmp.append(i[(len(i)-1)//2 + 1:])
        people = tmp

def match(person1, person2):
    global winners

    if shape[person1-1] == shape[person2-1]:
        if person1 > person2:
            winner = person2
        else:
            winner = person1
    else:
        if shape[person1 - 1] == '1':
            if shape[person2 - 1] == '2':
                winner = person2
            elif shape[person2 - 1] == '3':
                winner = person1

        elif shape[person1 - 1] == '2':
            if shape[person2 - 1] == '1':
                winner = person1
            elif shape[person2 - 1] == '3':
                winner = person2

        elif shape[person1 - 1] == '3':
            if shape[person2 - 1] == '1':
                winner = person2
            elif shape[person2 - 1] == '2':
                winner = person1
    winners.append(winner)

test_case = int(input())

for test in range(test_case):
    people = [i for i in range(1, int(input()) + 1)]
    shape = list(input().split())

    while 1:

        seperation()

        winners = []
        for rival in people:
            if len(rival) == 1:
                winners.append(rival[0])
            else:
                match(rival[0], rival[1])

        if len(winners) == 2:
            match(winners[0], winners[1])
            break
        else:
            people = winners

    print('#{} {}'.format(test + 1, winners[2]))
