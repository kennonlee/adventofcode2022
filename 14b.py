import sys

def print_slice(rocks, sand, x1, x2, y1, y2):
    for j in range (y1, y2 + 1):
        s = ''
        for i in range (x1, x2 + 1):
            if (i,j) in rocks or j == floor_y:
                s += '#'
            elif (i,j) in sand:
                s += 'o'
            else:
                s += '.'
        print('{0:03}'.format(j), s)

def get_rocks(lines):
    rocks = {}
    for line in lines:
        coords = [c.strip() for c in line.split('->')]
        for i in range(0, len(coords) - 1):
            ax, ay = [int(c) for c in coords[i].split(',')]
            bx, by = [int(c) for c in coords[i+1].split(',')]
            if ax == bx:
                if ay < by:
                    for y in range (ay, by + 1):
                        rocks[ax, y] = 1
                else:
                    for y in range (by, ay + 1):
                        rocks[ax, y] = 1                    
            elif ay == by:
                if ax < bx:
                    for x in range (ax, bx + 1):
                        rocks[x, ay] = 1
                else:
                    for x in range (bx, ax + 1):
                        rocks[x, ay] = 1                        
    return rocks

def find_floor(rocks):
    return sorted(rocks.keys(), key=lambda x: x[1])[-1][1] + 2

def find_move(rocks, sand, xy, floor_y):
    for i in ((0,1), (-1, 1), (1, 1)):
        move = tuple(map(lambda i, j: i + j, xy, i))
        if move not in rocks and move not in sand and move[1] < floor_y:
            return move
    return None

def drop_sand(rocks, sand, start, floor_y):
    cur = find_move(rocks, sand, start, floor_y)

    if cur == None: 
       print(len(sand) + 1)
       exit()

    last = cur
    while cur is not None:
        last = cur
        cur = find_move(rocks, sand, cur, floor_y)
    sand[last] = 1

    
rocks = get_rocks(sys.stdin.readlines())
floor_y = find_floor(rocks)
sand = {}
for i in range(50000):
    drop_sand(rocks, sand, (500, 0), floor_y)
#print_slice(rocks, sand, 480, 520, 0, floor_y)
