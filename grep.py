import sys

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(len(sys.argv))

f = sys.argv[1]
g = sys.argv[2]

fo = open(f, "r")

if (len(sys.argv) < 3):
    print("引数が足りません")

    exit()

else:
    print("引数の数OK")
    for line in fo:
        if (line.find(g) >=0):
           # print(line.find(g))
            print(line[:-1])    

    
