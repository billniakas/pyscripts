import time
import random
from random import randint
import subprocess
chars = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+?><|: "
clist=list(chars)
list1 = [" ",clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]
list2 = [clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]
list3 = [clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]
list4 = [clist[randint(0,len(clist)-1)]," ",clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]
list5 = [clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]," ",clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]
list6 = [clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]
list7 = [clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)],clist[randint(0,len(clist)-1)]]

terminal = subprocess.getoutput("stty size")

t_len=int(terminal[3:])
print(t_len)
while True:
    for j,k,l,m,n,o,p in zip(list1,list2,list3,list4,list5,list6,list7):
        time.sleep(0.035)
        matrix = [j,k,l,m,n,o,p]*round((t_len)/14)
        new_matrix = "".join(str(matrix).replace(",","").replace("[","").replace("]","").replace("'",""))
        #print("\n")
        #print("".join(str(matrix).replace(",","").replace("[","").replace("]","").replace("'","")),end="\r")
        print(" "+new_matrix)
        

    #break
