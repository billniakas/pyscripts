#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''A simple python script to center a given text
nothing more, nothing less
'''
import subprocess

Input = subprocess.getoutput("xrandr | grep -i '*'")
terminal = subprocess.getoutput("stty size")
resolution=Input.split()[0]
print("Your screen resolution is",resolution,"and your terminal resolution is",terminal[:2]+"x"+terminal[3:])


while True:
    text = input("Give me a text : ")
    if len(text) > int(terminal[3:]):
        print("Text too big to fit in one line")
        continue
    if text=="":break
    else:

        width = round((int(terminal[3:])/2-len(text)/2)-1)
        output = width*"-",text,width*"-"

        str_length=width+len(text)+width
        print(str_length)
        if str_length == int(terminal[3:])-2:
                    
                    print(int(terminal[3:])*"-")
                    print(" ".join(output))
                    print(int(terminal[3:])*"-")
                    break

        elif str_length < int(terminal[3:])-2:
                    
                    print(int(terminal[3:])*"-")
                    print(" ".join(output)+"-")
                    print(int(terminal[3:])*"-")
                    break

        elif str_length > int(terminal[3:])-2:
                    
                    print(int(terminal[3:])*"-")
                    print(" ".join(output)[:-1])
                    print(int(terminal[3:])*"-")
                    break
