import sys
import re

if len(list(sys.argv))<1:
    print("\nMissing Arguments\n")
    quit()

file = list(sys.argv)[1]
#site = list(sys.argv)[2]

with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        username = "".join(re.findall(r'(.*)\:',line))
        password = "".join(re.findall(r'\:(.*)',line))
        print(username,password)
        

    
