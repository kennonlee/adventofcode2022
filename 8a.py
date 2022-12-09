import sys, numpy

def tree_diff_lr(row):
    ret = []
    max_height = 0
    for t in row:
        cur = t - max_height
        ret.append(t - max_height)
        if max_height < t:
            max_height = t
    return ret

def tree_diff(rows):
    diffs = []
    for row in rows:
        left = tree_diff_lr(row)
        row.reverse()
        right = tree_diff_lr(row)
        row.reverse()
        right.reverse()
        combined = [max(a, b) for a, b in zip(left, right)]
        diffs.append(combined)
    return diffs

trees = []
for line in sys.stdin:
    trees.append([int(i) for i in line.strip()])

horiz_diffs = tree_diff(trees)
transposed = numpy.array(trees).T
vert_diffs = numpy.array(tree_diff(transposed.tolist())).T

print(numpy.matrix(horiz_diffs))
print(numpy.matrix(vert_diffs))

width = len(trees[0])
height = len(trees)
count = (width*2) + (height*2) - 4
print(count)

for j in range(1, height-1):
    for i in range(1, width-1):
        if max(horiz_diffs[i][j], vert_diffs[i,j]) > 0:
            count += 1
print(count)
