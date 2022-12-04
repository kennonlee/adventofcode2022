import sys

def score(s):
    if s.isupper():
        return ord(s) - 64 + 26
    elif s.islower():
        return ord(s) - 96
    else:
        print("error! bad input for score(): " + s)
        exit()

letters = []
for line in sys.stdin:
    first, second = line[:len(line)//2], line[len(line)//2:]
    first_set = [i for i in first]
    second_set = [i for i in second] 
    intersect = set(first_set) & set(second_set)
    if len(intersect) > 1:
        print("error! more than 1 intersection for: " + line)
        exit()
    letters.extend(intersect)

scores = list(map(score, letters))
print(letters)
print(scores)
print(sum(scores))
