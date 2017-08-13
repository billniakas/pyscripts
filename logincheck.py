import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import sys
import re

if len(list(sys.argv))<1:
    print("\nMissing Arguments\n")
    quit()

file = list(sys.argv)[1]
site = list(sys.argv)[2]
r=0
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        username = "".join(re.findall(r'(.*)\:',line))
        password = "".join(re.findall(r'\:(.*)',line))
        result = requests.get(site, auth=HTTPBasicAuth(username, password))
        check = re.findall(r'\[(.*)\]',str(result))
        result1 = requests.get(site, auth=HTTPDigestAuth(username, password))
        check1 = re.findall(r'\[(.*)\]',str(result1))
        if check[0] == '200' or check1[0] == '200':
            print(username,password,"is valid")
            
            with open("validpasses.txt","a") as validpasses:
                if r==0:
                    validpasses.write("\n")
                    validpasses.write(site)
                    validpasses.write("\n")
                    validpasses.write(username)
                    validpasses.write(" ")
                    validpasses.write(password)
                    
                elif r>0:
                    validpasses.write("\n")
                    validpasses.write(username)
                    validpasses.write(" ")
                    validpasses.write(password)
                    
                r+=1
        elif check[0] =='400' or check1[0] == '400':
            print(username,password,"is invalid")
        elif check[0] =='401' or check1[0] == '401':
            print(username,password,"is invalid")
        elif check[0] =='403' or check1[0] == '403':
            print("Forbiden Access")
