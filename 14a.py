import sys

def print_slice(rocks, sand, x1, x2, y1, y2):
    for j in range (y1, y2 + 1):
        s = ''
        for i in range (x1, x2 + 1):
            if (i,j) in rocks:
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

def find_move(rocks, sand, xy):
    for i in ((0,1), (-1, 1), (1, 1)):
        move = tuple(map(lambda i, j: i + j, xy, i))
        if move not in rocks and move not in sand:
            return move
    return None

def drop_sand(rocks, sand, start):
    cur = find_move(rocks, sand, start)
    last = cur
    while cur is not None:
        last = cur
        cur = find_move(rocks, sand, cur)
#    print(last)
    sand[last] = 1

    
rocks = get_rocks(sys.stdin.readlines())
#print(rocks)
sand = {}
# too lazy to add an end check in find_move() so just manually found i for which we get into an infinite loop
for i in range(638):
    drop_sand(rocks, sand, (500, 0))
#print_slice(rocks, sand, 494, 503, 0, 9)
