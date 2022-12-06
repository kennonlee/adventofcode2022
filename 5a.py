import sys, operator

stacks = {}

def add_to_stack(index, c):
    if index not in stacks:
        stacks[index] = []
    stacks[index].insert(0, c)

parse_stacks = True
for line in sys.stdin:
    if line == '\n':
        parse_stacks = False
        print("Stacks parsed, now moving items\n\n")
        continue

    if parse_stacks:
        for i, c in enumerate(line):
            if c.isalpha():
                add_to_stack(int(i/4) + 1, c)

    if not parse_stacks:
        gets = [1, 3, 5]
        count, fr, to = [int(i) for i in operator.itemgetter(*gets)(line.split(' '))]
        for i in range(count):
            c = stacks[fr].pop()
            stacks[to].append(c)

a = ''
for i in range(len(stacks)):
    a += stacks[i+1].pop()
print(a)
