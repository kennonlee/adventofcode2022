import sys

def intersect (x1, x2, y1, y2):
    if x1 < y2 and x2 < y1:
        return False
    if y1 < x2 and y2 < x1:
        return False
    return True

def superset (x1, x2, y1, y2):
    if x1 == y1 and x2 == y2:
        print("not superset: " + str(x1) + "-" + str(x2) + "," + str(y1) + "-" + str(y2))
        return False
    if x1 <= y1 and x2 >= y2:
#        print("superset: " + str(x1) + "-" + str(x2) + "," + str(y1) + "-" + str(y2))
        return True
    if y1 <= x1 and y2 >= x2:
#        print("superset: " + str(x1) + "-" + str(x2) + "," + str(y1) + "-" + str(y2))
        return True
    return False

count = 0
for line in sys.stdin:
#    print(line)
    a, b = line.split(',')
    a1, a2 = [int(i) for i in a.split('-')]
    b1, b2 = [int(i) for i in b.split('-')]
    if intersect(a1, a2, b1, b2):
        count += 1

print(count)
        
