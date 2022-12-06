import sys

input = sys.stdin.readline()
for i in range(0, len(input) - 14 + 1):
    sub = input[i:i+14]
    if len(set(sub)) == len(sub):
        print(i+14, sub)
        exit()
