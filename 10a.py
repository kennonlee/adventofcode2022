import sys

cycle = 1
x = 1
pairs = []
check_cycles = [i for i in range(20, 221, 40)]

for line in sys.stdin:
    if cycle in check_cycles:
        pairs.append((cycle, x))
    if line.strip() == 'noop':
        cycle += 1
    else:
        val = int(line.strip().split()[1])
        cycle += 2
        if cycle-1 in check_cycles:
            pairs.append((cycle-1, x))                        
        x += val

print(pairs)
print(sum([i*j for i, j in pairs]))
