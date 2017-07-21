import time, curses
import sys
from time import sleep
import os
from random import randrange
import re

sys.stdout.write("Loading")
sys.stdout.flush()
for _ in range(5):
    time.sleep(0.05)
    sys.stdout.write('.')
    sys.stdout.flush()

    
while True:
    try:
        os.system("clear")
        pages = input("Give a page number between 1 and 100 (Enter if you want to quit) : ")
        if int(pages) not in range(1,101):
            print(" "*len(pages),end="\r")
            print("Number not in range",end="\r")
            time.sleep(2)
            continue
        else:
            for i in range(0,int(pages)+1):
                print(" "*len(pages),end="\r")
                print(int(pages)-i,end="\r")
                time.sleep(0.05)
                
        print("\n")
        sys.stdout.write("Done")
        sys.stdout.flush()
        for _ in range(5):
            time.sleep(0.01)
            sys.stdout.write('.')
            sys.stdout.flush()
        print("\n")
        break
    except ValueError as e:
        if pages=="":break
        else:
            print("Error",e)
            time.sleep(2)
