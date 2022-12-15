import sys, json, functools

def is_ordered(a, b):
#    print('comparing', a, b)
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return -1
        elif a < b:
            return 1
        else:
            return 0   
    elif isinstance(a, int) and isinstance(b, list):
        return is_ordered([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return is_ordered(a, [b])
    else:
        # both are lists
        ret = True
        for i, elem in enumerate(a):
            if len(b) == i:
                return -1
            ret = is_ordered(elem, b[i])
            if ret == 1:
                return 1
            elif ret == 0:
                continue
            else:
                return -1
        if len(a) < len(b):
            return 1
        return 0

two = [[2]]
six = [[6]]
lines = [two, six]
for line in sys.stdin.readlines():
    if line == '\n':
        continue
    lines.append(json.loads(line))

s = sorted(lines, key=functools.cmp_to_key(is_ordered), reverse=True)
#for i, line in enumerate(s):
#    print(i+1, line)
for i, line in enumerate(s):
    if line == two:
        tindex = i+1
    if line == six:
        sindex = i+1

print(tindex*sindex)

    
