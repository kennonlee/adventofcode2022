import sys

input = sys.stdin.readline()
for i in range(0, len(input) - 4 + 1):
    sub = input[i:i+4]
    if len(set(sub)) == len(sub):
        print(i+4, sub)
        exit()
