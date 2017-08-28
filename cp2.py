import sys

print(len(sys.argv))

print(sys.argv[1])
print(sys.argv[2])

f=sys.argv[1]
t=sys.argv[2]
cp = open(t, "w")
for line in open(f):
    print(line, end=" ")

    cp.write(line)

cp.close
