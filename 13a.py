import sys, json

def parse_input(s):
    pairs = []
    for i in range(0, len(s), 3):
        a = s[i]
        b = s[i+1]
        pairs.append((a.strip(), b.strip()))

    parsed = []
    for a, b in pairs:
        parsed.append((json.loads(a), json.loads(b)))
    return parsed

def is_ordered(a, b):
#    print('comparing', a, b)
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return False
        elif a < b:
            return True
        else:
            return None   
    elif isinstance(a, int) and isinstance(b, list):
        return is_ordered([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return is_ordered(a, [b])
    else:
        # both are lists
        ret = True
        for i, elem in enumerate(a):
            if len(b) == i:
                return False
            ret = is_ordered(elem, b[i])
            if ret:
                return True
            elif ret is None:
                continue
            else:
                return False
        if len(a) < len(b):
            return True
        return None

pairs = parse_input(sys.stdin.readlines())
sum = 0
for i, pair in enumerate(pairs):
    val = is_ordered(pair[0], pair[1])
#    print(i+1, val)
    if val is None or val:
        sum += i+1 
print(sum)
    
