# -*- coding: utf-8 -*-
import platform
import time
import os
import ctypes
import subprocess
import re
platform=platform.uname()

os_dict = {"arch linux":['Arch Linux','''
                 +              
                  #              
                 ###                   {}
                #####                  {}
                ######                 Screen Resolution : {}
               ; #####;                Operating System  : {}
              +##.#####                Kernel Version    : {} 
             +##########               Desktop           : {}
            #############;             Total Memory      : {:1.2F} GB
           ###############+            Free Memory       : {:1.2F} GB
          #######   #######            Active Memory     : {:1.2F} GB 
        .######;     ;###;`".          System Uptime     : {}
       .#######;     ;#####.           CPU               : {}
       #########.   .########`         Packages          : {}
      ######'           '######        GPU               : {}
     ;####                 ####;   
     ##'                     '##   
    #'                         `#'''] ,                       
"windows":'''

██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗
██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝
██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗
██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║
╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝
                                                          
''', "ubuntu":["Ubuntu Linux",'''                           ./+o+-      
                  yyyyy- -yyyyyy+         {}
               ://+//////-yyyyyyo         {}
           .++ .:/++++++/-.+sss/`         Screen Resolution : {}
         .:++o:  /++++++++/:--:/-         Operating System  : {}
        o:+o+:++.`..```.-/oo+++++/        Kernel Version    : {}
       .:+o:+o/.          `+sssoo+/       Desktop           : {}
  .++/+:+oo+o:`             /sssooo.      Total Memory      : {}
 /+++//+:`oo+o               /::--:.      Free Memory       : {}
 \+/+o+++`o++o               ++////.      Active Memory     : {}
  .++.o+++oo+:`             /dddhhh.      System Uptime     : {}
       .+.o+oo:.          `oddhhhh+       CPU               : {}
        \+.++o+o``-````.:ohdhhhhh+        Packages          : {}  
         `:o+++ `ohhhhhhhhyo++os:         GPU               : {}
           .o:`.syhhhhhhh/.oo++o`     
               /osyyyyyyo++ooo+++/    
                   ````` +oo+++o\:    
                          `oo++.  '''],"linux mint":["Linux Mint",'''

                                       
 MMMMMMMMMMMMMMMMMMMMMMMMMmds+.        
 MMm----::-://////////////oymNMd+`        {}
 MMd      /++                -sNMd:       {}
 MMNso/`  dMM    `.::-. .-::.` .hMN:      Screen Resolution : {}
 ddddMMh  dMM   :hNMNMNhNMNMNh: `NMm      Operating System  : {}
     NMm  dMM  .NMN/-+MMM+-/NMN` dMM      Kernel Version    : {}
     NMm  dMM  -MMm  `MMM   dMM. dMM      Desktop           : {}
     NMm  dMM  -MMm  `MMM   dMM. dMM      Total Memory      : {:1.2F} GB
     NMm  dMM  .mmd  `mmm   yMM. dMM      Free Memory       : {:1.2F} GB
     NMm  dMM`  ..`   ...   ydm. dMM      Active Memory     : {:1.2F} GB 
     hMM- +MMd/-------...-:sdds  dMM      System Uptime     : {}  
     -NMm- :hNMNNNmdddddddddy/`  dMM      CPU               : {}
      -dMNs-``-::::-------.``    dMM      Packages          : {}
       `/dMNmy+/:-------------:/yMMM      GPU               : {}  
          ./ydNMMMMMMMMMMMMMMMMMMMMM   
             \.MMMMMMMMMMMMMMMMMMM    
            '''],'linux':['Linux','''

                 .88888888:.              {}
                88888888.88888.           {}
              .8888888888888888.          Screen Resolution : {}
              888888888888888888          Operating System  : {}
              88' _`88'_  `88888          Kernel Version    : {} 
              88 88 88 88  88888          Desktop           : {}  
              88_88_::_88_:88888          Total Memory      : {:1.2F} GB
              88:::,::,:::::8888          Free Memory       : {:1.2F} GB
              88`:::::::::'`8888          Active Memory     : {:1.2F} GB
             .88  `::::'    8:88.         System Uptime     : {} 
            8888            `8:888.       CPU               : {} 
          .8888'             `888888.     Packages          : {} 
         .8888:..  .::.  ...:'8888888:.   GPU               : {} 
        .8888.'     :'     `'::`88:88888 
       .8888        '         `.888:8888. 
      888:8         .           888:88888 
    .888:88        .:           888:88888: 
    8888888.       ::           88:888888 
    `.::.888.      ::          .88888888 
   .::::::.888.    ::         :::`8888'.:. 
  ::::::::::.888   '         .:::::::::::: 
  ::::::::::::.8    '      .:8::::::::::::. 
 .::::::::::::::.        .:888::::::::::::: 
 :::::::::::::::88:.__..:88888:::::::::::' 
  `'.:::::::::::88888888888.88:::::::::' 
        `':::_:' -- '' -'-' `':_::::'`
        ''']}                                                         
                                                                          

if platform[0] == 'Windows':
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    ostype=("You are using",platform[0],platform[3])
    
    print(" ".join(ostype))
    print(os_dict[platform[0].lower()])
    time.sleep(0.5)
    resolution=str(screensize[0])+"x"+str(screensize[1])
else:
    
    Input = subprocess.getoutput("xrandr | grep -i '*'")
    resolution=Input.split()[0]
    linuxtype=subprocess.getoutput("cat /etc/os-release | grep '^NAME'").replace('''"''','')
    
    packages = subprocess.getoutput("$(pacman -Q | wc -l) || $(dpkg -l | grep -c '^ii')")
    packagelist=re.findall('\d{3,}',packages)
    user = subprocess.getoutput("echo $USER")
    hostname = subprocess.getoutput("hostname")
    computer=user+"@"+hostname
    underline=str(len(computer)*"-")
    gpu = subprocess.getoutput("glxinfo -B | grep -i '''opengl renderer string:'''")
    gpu = re.findall(r': (.*)',gpu)
    gpu = " ".join(gpu)
    if len(gpu) == 0:
        gpu = subprocess.getoutput("lspci -k | grep -iEA3 '3d|vga compatible controller' | head -n1")
        gpu = re.findall(r'\[(.*?)\]',gpu) 
        gpu = " ".join(gpu)
    
##    linuxtype=re.findall('\w{4,}',platform[2], re.I)
##    if len(linuxtype)==0 or linuxtype[0]=="generic":
##        linuxtype=re.findall('\w{4,}[^generic]',platform[3], re.I)
##        linuxtype[0]=linuxtype[0].strip(" ")
##    else:
##        pass
    os_type = linuxtype[5:].lower()
    if os_type not in os_dict.keys():
        os_type = 'linux'
    #ostype=("\nYou are using",os_dict[os_type][0],platform[2],"\n")
    desktop=os.environ.get('DESKTOP_SESSION')
    memtotal = float(subprocess.getoutput("grep MemTotal /proc/meminfo |grep -oE '''[0-9]*'''"))/pow(10,6)
    memfree = float(subprocess.getoutput("grep MemFree /proc/meminfo |grep -oE '''[0-9]*'''"))/pow(10,6)
    memactive = (memtotal-memfree)
    uptime = subprocess.getoutput("uptime -p")
    cpu = subprocess.getoutput("cat /proc/cpuinfo | grep '''model name''' | head -n1").replace("  @ ","@")
    cpu = " ".join(re.findall(r': (.*)',cpu)).replace("    "," ")
    
    #print(" ".join(ostype))
    os.system("clear")

    print("\n",os_dict[os_type][1].format(computer,underline,resolution,os_dict[os_type][0],platform[2],desktop,memtotal,memfree,memactive,uptime[3:],cpu,packagelist[0],gpu))
    #print("\n"*2)
    


