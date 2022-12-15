import sys

class Monkey:
    monkeys = []
    
    def __init__(self, id, items, arga, op, argb, test, test_true, test_false):
        self.id = id
        self.items = items
        self.arga = arga
        self.op = op
        self.argb = argb
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0

    def do_round(self):
        while len(self.items) > 0:
            self.inspected += 1
            item = self.items.pop(0)
            a = self.eval_arg(self.arga, item)
            b = self.eval_arg(self.argb, item)
            if self.op == '+':
                worry = a + b
            elif self.op == '*':
                worry = a * b
            worry = int(worry/3)
            if worry % self.test == 0:
                Monkey.monkeys[self.test_true].add_item(worry)
            else:
                Monkey.monkeys[self.test_false].add_item(worry)
            

    def eval_arg(self, arg, item):
        if arg == 'old':
            return item
        else:
            return int(arg)

    def add_item(self, item):
        self.items.append(item)

def init_monkeys(s):
    for m in s.split('\n\n'):
        lines = m.split('\n')
        id = int(lines[0].split()[1][:-1])
        items = [int(i.strip()) for i in lines[1].split(':')[1].split(',')]
        arga, op, argb = lines[2].split('=')[1].split()
        test = int(lines[3].split()[-1])  
        test_true = int(lines[4].split()[-1])
        test_false = int(lines[5].split()[-1])
        Monkey.monkeys.append(Monkey(id, items, arga, op, argb, test, test_true, test_false))
        
init_monkeys(sys.stdin.read())

for monkey in Monkey.monkeys:
    print(vars(monkey))

for r in range(20):
    print('*** ROUND', r, '***')
    for monkey in Monkey.monkeys:
        monkey.do_round()
    for monkey in Monkey.monkeys:
        print(vars(monkey))

inspecteds = sorted([m.inspected for m in Monkey.monkeys])
print(inspecteds, inspecteds.pop() * inspecteds.pop())
