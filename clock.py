import time
import subprocess
import os
import sys
import curses
timedict = {
    '0': ["  #####   ", " ##   ##  ", "##     ## ", "##     ## ", "##     ## ",
          " ##   ##  ", "  #####   "],
    '1': ["    ##    ", "  ####    ", "    ##    ", "    ##    ", "    ##    ",
          "    ##    ", "  ######  "],
    '2': [" #######  ", "##     ## ", "       ## ", " #######  ", "##        ",
          "##        ", "######### "],
    '3': [" #######  ", "##     ## ", "       ## ", " #######  ", "       ## ",
          "##     ## ", " #######  "],
    '4': ["##        ", "##    ##  ", "##    ##  ", "##    ##  ", "######### ",
          "      ##  ", "      ##  "],
    '5': [" ######## ", " ##       ", " ##       ", " #######  ", "       ## ",
          " ##    ## ", "  ######  "],
    '6': [" #######  ", "##     ## ", "##        ", "########  ", "##     ## ",
          "##     ## ", " #######  "],
    '7': [" ######## ", " ##    ## ", "     ##   ", "    ##    ", "   ##     ",
          "   ##     ", "   ##     "],
    '8': [" #######  ", "##     ## ", "##     ## ", " #######  ", "##     ## ",
          "##     ## ", " #######  "],
    '9': [" #######  ", "##     ## ", "##     ## ", " ######## ", "       ## ",
          "##     ## ", " #######  "],
    ':': ["   ", "   ", " # ", "   ", " # ", "   ", "   "]
}

stdscr = curses.initscr()
q=-1

while q not in [ord('q'),ord('Q')]:
    stdscr.nodelay(1)
    q = stdscr.getch()
    x,y=5,5
    dims = stdscr.getmaxyx()
    x,y=int(dims[1]/2)-5*int(len(timedict["0"])/2),int(dims[0]/2)-int(len(timedict["0"])/2)
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(0)
    clock=subprocess.getoutput("date -R")
    stdscr.addstr(1, 1, "The terminal resolution is "+str(dims[0])+" "+str(dims[1]))
    stdscr.addstr(int(dims[0]-1),int(dims[1]-len("Press Q or q to quit"))-1, "Press Q or q to quit")
    stdscr.addstr(int(dims[0]-1), 1, ("Today is "+clock[:16]).replace(",",""))
    for i in range(0,len(timedict["0"])):
        stdscr.addstr(y, x-20,timedict[str(clock[17])][i],curses.A_BOLD)
        stdscr.addstr(y, x-10,timedict[str(clock[18])][i],curses.A_BOLD)
        stdscr.addstr(y, x,timedict[str(clock[19])][i],curses.A_BOLD)
        stdscr.addstr(y, x+5,timedict[str(clock[20])][i],curses.A_BOLD)
        stdscr.addstr(y, x+15,timedict[str(clock[21])][i],curses.A_BOLD)
        stdscr.addstr(y, x+25,timedict[str(clock[22])][i],curses.A_BOLD)
        stdscr.addstr(y, x+30,timedict[str(clock[23])][i],curses.A_BOLD)
        stdscr.addstr(y, x+40,timedict[str(clock[24])][i],curses.A_BOLD)
       


        y+=1
        



    stdscr.refresh()
os.system("clear")

    
    
    
       
