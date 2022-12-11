#HHHHH
#H...H
#H.T.H
#H...H
#HHHHH
import sys

knots = [[0,0] for i in range(10)]    
visited = {(0,0)}

def is_adjacent(a, b):
    diff = max([abs(i - j) for i, j in zip(a, b)])
    return diff <= 1

def move_closer(a, b):
#    print('before:', head, tail)
    diffs = [i - j for i, j in zip(a,b)]
    if diffs[1] == 0:
        pass
    elif diffs[1] > 0:
        b[1] += 1
    else:
        b[1] -= 1

    if diffs[0] == 0:
        pass
    elif diffs[0] > 0:
        b[0] += 1
    else:
        b[0] -= 1
#    print('after:', head, tail)

def move_once(d):
    match d:
        case 'U':        
            knots[0][1] += 1
        case 'D':
            knots[0][1] -= 1
        case 'L':
            knots[0][0] -= 1
        case 'R':
            knots[0][0] += 1

    for i in range(1, len(knots)):
        head = knots[i-1]
        tail = knots[i]
        while not is_adjacent(head, tail):
            move_closer(head, tail)
    visited.add(tuple(knots[-1]))

def move(d, num):
    for i in range(num):
        move_once(d)

for line in sys.stdin:
    d, num = line.split()
    move(d, int(num))
print(len(visited))
    


