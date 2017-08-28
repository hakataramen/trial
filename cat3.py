import sys

f = sys.argv[1]

print(len(sys.argv))

print(sys.argv[0])
print(sys.argv[1])

if (len(sys.argv) < 1):
    print("引数が足りません")

else:
    print("引数の数OK")    
    for line in open(f):
        print(line, end =" ")

    f.close
        
