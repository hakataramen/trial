import sys

f=sys.argv[1]
w=sys.argv[2]
cp=open(w, "w")
for line in open(f):
       cp.write(line)

cp.close()
