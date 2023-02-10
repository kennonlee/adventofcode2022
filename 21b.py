import sys, operator

class Monkey:
    monkeys = dict()
    
    def __init__(self, s):
        name, tokens = [t.strip() for t in s.split(':')]
        self.name = name
        self.visited = False
        if tokens.isnumeric():
            self.val = int(tokens)
        else:
            tokens = tokens.split()
            self.val = None
            self.a = tokens[0]
            self.b = tokens[2]
            self.op_string = tokens[1]
            self.op = Monkey.map_op(self.op_string)
        Monkey.monkeys[self.name] = self

    def map_op(op_string):
        match op_string:
            case '+':
                return operator.add
            case '-':
                return operator.sub
            case '*':
                return operator.mul
            case '/':
                return operator.floordiv
        
    def solve(self, a, b):
        self.val = self.op(a, b)

    def expand(self, a, b):
        if self.val is not None:
            return self.val
        else:
            pass

def read_monkeys(lines):
    monkeys = dict()
    for line in lines:
        m = Monkey(line)
        monkeys[m.name] = m
    return monkeys

def run():
    monkeys = read_monkeys(sys.stdin.readlines())
    root = monkeys['root']
    queue = [root]
    relevant = []
    while queue:
        cur = queue.pop(0)
        if cur.visited == False:
            if hasattr(cur, 'a'):
                queue.append(monkeys[cur.a])
            if hasattr(cur, 'b'):
                queue.append(monkeys[cur.b])
            relevant.append(cur)
            cur.visited = True
    print([i.name for i in relevant])

    for i in range(500):
        solved = dict()
        root.val = None
        while root.val is None:
            for m in relevant:
                if m.name == 'humn':
                    m.val = i
                if m.val is not None:
                    solved[m.name] = m.val
#            print(solved.keys())
#            print([i.name for i in relevant])
            for m in relevant:
                if m.val is None and m.a is not None and m.b is not None:
                    if m.a in solved and m.b in solved:
                        if m.name == 'root':
                            if solved[m.a] == solved[m.b]:
                                print('root matches! humn = ', i)
                                root.val = False
                            else:
                                print('root doesnt match:', solved[m.a], solved[m.b], i)
                                root.val = False 
                        else:
                            print('solving', m.a, m.op_string, m.b)
                            m.solve(solved[m.a], solved[m.b])
                            solved[m.name] = m.val

run()
