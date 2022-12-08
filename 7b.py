import sys
from anytree import AnyNode, RenderTree, PreOrderIter

root = None

cur = None
in_list = False
for line in sys.stdin:
    if line[0] == '$':
        in_list = False
        tokens = line.split()
        if tokens[1] == 'cd':
            loc = tokens[2]
            if loc == '/':
                root = AnyNode(id='/', type='dir', size=0)
                cur = root
            elif loc == '..':
                cur = cur.parent
            else:
                for n in cur.children:
                    if loc == n.id:
                        cur = n
        elif tokens[1] == 'ls':
            in_list = True
        else:
            print("error!!")
            exit()
    elif in_list:
        a, b = line.split()
        if a == 'dir':
            node = AnyNode(id=b, parent=cur, type='dir', size=0)
        else:
            node = AnyNode(id=b, parent=cur, type='file', size=int(a))

def sums(cur):
    if cur.is_leaf:
        return cur.size
    else:
        for child in cur.children:
            cur.size += sums(child)
    return cur.size

sums(root)
print(RenderTree(root))
print([(node.id, node.size) for node in PreOrderIter(root, filter_=lambda n: n.type == 'dir')])

required_to_delete = root.size - 70000000 + 30000000
sizes = [node.size for node in PreOrderIter(root, filter_=lambda n: n.type == 'dir' and n.size > required_to_delete)]
print(min(sizes), sizes)
