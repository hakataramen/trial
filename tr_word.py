import re
import sys

print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))

f = sys.argv[1]

        
fo = open(f, "r")

if (len(sys.argv) <2 ):
        print("引数が足りません")

        exit()

else:
        print("引数の数OK")
        for line in fo:
                line=line.strip()
                print(line)
                words=re.split(" +",line)
                print(words)
                for word in words:
                            print(word)
