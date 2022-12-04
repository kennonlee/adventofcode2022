import sys

def intersect (x1, x2, y1, y2):
    if x1 < y2 and x2 < y1:
        return False
    if y1 < x2 and y2 < x1:
        return False
    return True

count = 0
for line in sys.stdin:
    a, b = line.split(',')
    a1, a2 = [int(i) for i in a.split('-')]
    b1, b2 = [int(i) for i in b.split('-')]
    if intersect(a1, a2, b1, b2):
        count += 1

print(count)
        
