import sys
from itertools import islice

def score(s):
    if s.isupper():
        return ord(s) - 64 + 26
    elif s.islower():
        return ord(s) - 96
    else:
        print("error! bad input for score(): " + s)
        exit()

def intersect(a, b, c):
    a_set = [i for i in a]
    b_set = [i for i in b] 
    c_set = [i for i in c] 
    intersect = set(a_set) & set(b_set) & set(c_set)
    intersect.remove('\n')
    if len(intersect) > 1:
        print("error! more than 1 intersection for: " + a + " " + b + " " + c)
        print(intersect)
        exit()
    return intersect.pop()
        
letters = []
with open('3a-test.txt', 'r') as infile:
    for x in range(100):
        a, b, c = list(islice(infile, 3))
        letters.extend(intersect(a, b, c))
        print(letters)

scores = list(map(score, letters))
print(letters)
print(scores)
print(sum(scores))
