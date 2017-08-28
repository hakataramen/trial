import re
import sys
import difflib
from collections import OrderedDict

print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))

dic = OrderedDict()
count = 0
g=sys.argv[1]

f = open(g,"r")



if(len(sys.argv) <2):
    print("引数の数が足りません")
    exit()

else:
    print("引数の数OK")
    for line in f:
        line=line.strip()
        print(line)
        words=re.split(" +",line)
        print(words)

        for word in words:
            if( word in dic):
                dic[word] += 1
            else:
                dic[word] = 1

        for a, b in sorted(dic.items(), reverse=True, key=lambda x:x[1]):
            count += 1
            if(count <= 10):
                print(a, b)
                        
                    
                
                
                
            
        
    
