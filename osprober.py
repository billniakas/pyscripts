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
      ######'           '######    
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
                                                          
''', "ubuntu":["Ubuntu Linux",'''                                     y#▓▓▓▓▓▄     
                                    #▓▓▓▓▓▓▓▓▓    
                      ¿╓╔###║###M╔  ▓▓▓▓▓▓▓▓▓▓    
                    ╙║║║║║║║║║║║║║░ └▓▓▓▓▓▓▓▓┘    
               ╔╠░    ║║║║║║║║║║║║║N, └╙╩╩╙└      
             ╔╠╠╠╠╠,   ╚║║║║║║║║║║║║║║M╔╓╓╓#N,    
           ╓╠╠╠╠╠╠╠╠∩   ╙╙      └╙╙║║║║║║║║║║║N             {}   
          #╠╠╠╠╠╠╠╠╠╚                ╙║║║║║║║║║║            {}
         ╔╠╠╠╠╠╠╠╠╚                    ╙║║║║║║║║║           Screen Resolution : {}
  .╓╔╔╓,  ╙╠╠╠╠╠╠╚                      ╙║║║║║║║║Γ          Operating System  : {}
.║║║║║║║║,  ╠╠╠╠╠                        ║║║║║║║║║          Kernel Version    : {} 
║║║║║║║║║║  ╠╠╠╠░                                           Desktop           : {}
╚║║║║║║║║╠  ╠╠╠╠░                        ╓»»»»»»»»          Total Memory      : {:1.2F} GB
 ╙╚║║║║╚╙  #╠╠╠╠╠∩                       ▓▓▓▓▓▓▓▓▒          Free Memory       : {:1.2F} GB
         ╔╠╠╠╠╠╠╠╠,                    \▓▓▓▓▓▓▓▓▓           Active Memory     : {:1.2F} GB 
         `╠╠╠╠╠╠╠╠╠∩                  #▓▓▓▓▓▓▓▓▓Ñ           System Uptime     : {}  
           ╠╠╠╠╠╠╠╠╠╠              ╓@▓▓▓▓▓▓▓▓▓▓╜            CPU               : {}
            ╙╠╠╠╠╠╠╚   ┌▓▓₧MmmM₧▓▓▓▓▓▓▓▓▓▓▓▓▓▓              Packages          : {}        
              ╙╠╠╠∩   ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▀░      └     
                `    #▓▓▓▓▓▓▓▓▓▓▓▓▓  ╓∩╠╠╠╠∩╔     
                    "▀▓▓▓▓▓▓▓▓▓▓▓▓  #╠╠╠╠╠╠╠╠░    
                          └└└└└└    ╠╠╠╠╠╠╠╠╠╠    
                                     ╚╠╠╠╠╠╠╠     
                                       └╙╙╙       '''],"linux mint":["Linux Mint",'''

                                       
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
       `/dMNmy+/:-------------:/yMMM   
          ./ydNMMMMMMMMMMMMMMMMMMMMM   
             \.MMMMMMMMMMMMMMMMMMM    
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
    
##    linuxtype=re.findall('\w{4,}',platform[2], re.I)
##    if len(linuxtype)==0 or linuxtype[0]=="generic":
##        linuxtype=re.findall('\w{4,}[^generic]',platform[3], re.I)
##        linuxtype[0]=linuxtype[0].strip(" ")
##    else:
##        pass
    ostype=("\nYou are using",os_dict[linuxtype[5:].lower()][0],platform[2],"\n")
    desktop=os.environ.get('DESKTOP_SESSION')
    memtotal = float(subprocess.getoutput("grep MemTotal /proc/meminfo |grep -oE '''[0-9]*'''"))/pow(10,6)
    memfree = float(subprocess.getoutput("grep MemFree /proc/meminfo |grep -oE '''[0-9]*'''"))/pow(10,6)
    memactive = (memtotal-memfree)
    uptime = subprocess.getoutput("uptime -p")
    cpu = subprocess.getoutput("cat /proc/cpuinfo | grep '''model name''' | head -n1").replace("          "," ").replace("  @ ","@")
    
    #print(" ".join(ostype))
    os.system("clear")		
    print("\n",os_dict[linuxtype[5:].lower()][1].format(computer,underline,resolution,os_dict[linuxtype[5:].lower()][0],platform[2],desktop,memtotal,memfree,memactive,uptime[3:],cpu[13:],packagelist[0]))
    #print("\n"*2)
    


