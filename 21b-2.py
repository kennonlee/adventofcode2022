import sys, operator

class Monkey:

    def __init__(self, s):
        name, tokens = [t.strip() for t in s.split(':')]
        self.name = name
        if tokens.isnumeric():
            self.val = int(tokens)
        else:
            tokens = tokens.split()
            self.val = None
            self.a = tokens[0]
            self.b = tokens[2]
            self.op_string = tokens[1]
            self.op = Monkey.map_op(self.op_string)

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

def read_monkeys(lines):
    monkeys = []
    for line in lines:
        monkeys.append(Monkey(line))
    return monkeys

def run():
    val = 3243420789500
    lines = sys.stdin.readlines()
    for humn in range(val, val*2, 1):
        if humn % 1000 == 0:
            print(humn)
            
        monkeys = read_monkeys(lines)
        solved = dict()
        for m in monkeys:
            if m.name == 'humn':
                m.val = humn
            if m.val is not None:
                solved[m.name] = m.val

        while 'root' not in solved:
            for m in monkeys:
                if m.val is None and m.a is not None and m.b is not None:
                    if m.a in solved and m.b in solved:
                        if m.name == 'root':
                            if solved[m.a] == solved[m.b]:
                                print('solved! humn = ', humn)
                                exit()
                            else:
                                if humn % 1000 == 0:
                                    print('not equal!', humn, solved[m.a], solved[m.b], solved[m.a]-solved[m.b])
                                m.val = True
                                solved[m.name] = True
                                break
                        else:
                            m.solve(solved[m.a], solved[m.b])
                            solved[m.name] = m.val
run()
