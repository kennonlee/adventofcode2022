import sys, numpy


def load_map(lines): 
    heightmap = []
    for line in lines:
        heightmap.append(line.strip())
    return heightmap

def find_start(heightmap):   
    for y, line in enumerate(heightmap):
        try:
            x = line.index('S')
            break
        except ValueError:
            continue
    print('start',x,y)
    return (x,y)

def find_starts(heightmap):
    starts = []
    starts.append(find_start(heightmap))
    for y, line in enumerate(heightmap):
        for x, c in enumerate(line):
            if c == 'a':
                starts.append((x, y))                
    return starts

def make_matrix(width, height, val):
    matrix = []
    for j in range(height):
        matrix.append([val for i in range(width)])
    return matrix

def valid_move(heightmap, vx, vy, zx, zy):
    if zx < 0 or zx > len(heightmap[0])-1:
        return False
    if zy < 0 or zy > len(heightmap)-1:
        return False
    v = heightmap[vy][vx]
    z = heightmap[zy][zx]
#    print(v, z)
    if v == 'S':
        v = 'a'
    if z == 'E':
        z = 'z'
    return ord(z) - ord(v) <= 1

def get_path(parents, origin, end):
    count = 0
    cur = end
    path = []
    while (origin != cur):
        path.append(cur)
        count += 1
        cur = parents[cur[1]][cur[0]]
    return path
        

def bfs(heightmap, start):
    q = []
    visited = make_matrix(len(heightmap[0]), len(heightmap), 0)
    parents = make_matrix(len(heightmap[0]), len(heightmap), (-1,-1))
    q.append(start)
    while q:
        vx, vy = q.pop(0)
        visited[vy][vx] = 1
        if heightmap[vy][vx] == 'E':
            path = get_path(parents, start, (vx, vy))
    
            draw = make_matrix(len(heightmap[0]), len(heightmap), '.')
            count = 0
            for (x,y) in path:
                draw[y][x] = str(count)
                count += 1
                count %= 10
            for j in range(len(draw)):
                s = ''
                for i in range(len(draw[0])):
                    s += draw[j][i]
#                print(s)
            return len(path)
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            zx = vx + i
            zy = vy + j
#            print('checking', (zx, zy))
            if valid_move(heightmap, vx, vy, zx, zy) and visited[zy][zx] == 0:
#                print('valid move', (vx, vy), 'to', (zx, zy))
                visited[zy][zx] = 1
                parents[zy][zx] = (vx, vy)
                q.append((zx, zy))
#            print(parents)
#    print(visited)



heightmap = load_map(sys.stdin.readlines())
#print(heightmap)
starts = find_starts(heightmap)
max = 10000
print(starts)
for start in starts:
    cur = bfs(heightmap, start)
    if cur is not None and cur < max:
        max = cur
print(max)
