import sys, numpy, math

trees = []
for line in sys.stdin:
    trees.append([int(i) for i in line.strip()])
print(numpy.matrix(trees), "trees")

width = len(trees[0])
height = len(trees)

max = 0
for j in range(height):
    for i in range(width):
        n, s, e, w = (0,0,0,0)
        cur_height = trees[i][j]
        #north
        for k in reversed(range(j)):
            n += 1
            if trees[i][k] >= cur_height:
                break
        #south
        for k in range(j+1, height):
            s += 1
            if trees[i][k] >= cur_height:
                break
        #west
        for k in reversed(range(i)):
            w += 1
            if trees[k][j] >= cur_height:
                break
        #east
        for k in range(i+1, width):
            e += 1
            if trees[k][j] >= cur_height:
                break

        score =  math.prod((n, s, w, e))
        if score > max:
            max = score

print(max)
        
