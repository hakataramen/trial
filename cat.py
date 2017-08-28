import sys

f=sys.argv[1]
for line in open(f):
    print(line, end=" ")
