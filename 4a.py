import sys

def superset (x1, x2, y1, y2):
    if x1 <= y1 and x2 >= y2:
        return True
    if y1 <= x1 and y2 >= x2:
        return True
    return False

count = 0
for line in sys.stdin:
    a, b = line.split(',')
    a1, a2 = [int(i) for i in a.split('-')]
    b1, b2 = [int(i) for i in b.split('-')]
    if superset(a1, a2, b1, b2):
        count += 1

print(count)
        
