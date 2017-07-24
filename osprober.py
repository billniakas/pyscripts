# -*- coding: utf-8 -*-
import platform
import time
import os
import ctypes
import subprocess
import re
platform=platform.uname()

os_dict = {"arch":['Arch Linux','''
              +              
              #              
             ###             
            #####            
            ######                       Screen Resolution : {}
           ; #####;                      Operating System  : {}
          +##.#####                      Kernel Version    : {} 
         +##########                     Desktop           : {}
        #############;       
       ###############+      
      #######   #######      
    .######;     ;###;`".      
   .#######;     ;#####.       
   #########.   .########`     
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
           ╓╠╠╠╠╠╠╠╠∩   ╙╙      └╙╙║║║║║║║║║║║N   
          #╠╠╠╠╠╠╠╠╠╚                ╙║║║║║║║║║║  
         ╔╠╠╠╠╠╠╠╠╚                    ╙║║║║║║║║║                   Screen Resolution : {}
  .╓╔╔╓,  ╙╠╠╠╠╠╠╚                      ╙║║║║║║║║Γ                  Operating System  : {}
.║║║║║║║║,  ╠╠╠╠╠                        ║║║║║║║║║                  Kernel Version    : {} 
║║║║║║║║║║  ╠╠╠╠░                                                   Desktop           : {}
╚║║║║║║║║╠  ╠╠╠╠░                        ╓»»»»»»»»
 ╙╚║║║║╚╙  #╠╠╠╠╠∩                       ▓▓▓▓▓▓▓▓▒
         ╔╠╠╠╠╠╠╠╠,                    \▓▓▓▓▓▓▓▓▓ 
         `╠╠╠╠╠╠╠╠╠∩                  #▓▓▓▓▓▓▓▓▓Ñ 
           ╠╠╠╠╠╠╠╠╠╠              ╓@▓▓▓▓▓▓▓▓▓▓╜  
            ╙╠╠╠╠╠╠╚   ┌▓▓₧MmmM₧▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
              ╙╠╠╠∩   ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▀░      └     
                `    #▓▓▓▓▓▓▓▓▓▓▓▓▓  ╓∩╠╠╠╠∩╔     
                    "▀▓▓▓▓▓▓▓▓▓▓▓▓  #╠╠╠╠╠╠╠╠░    
                          └└└└└└    ╠╠╠╠╠╠╠╠╠╠    
                                     ╚╠╠╠╠╠╠╠     
                                       └╙╙╙       '''] }                                                         
                                                                          

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
    linuxtype=re.findall('\w{4,}',platform[2], re.I)
    if len(linuxtype)==0 or linuxtype[0]=="generic":
        linuxtype=re.findall('\w{4,}[^generic]',platform[3], re.I)
        linuxtype[0]=linuxtype[0].strip(" ")
    else:
        pass
    ostype=("\nYou are using",os_dict[linuxtype[0].lower()][0],platform[2],"\n")
    desktop=os.environ.get('DESKTOP_SESSION')
    #print(" ".join(ostype))
    print(os_dict[linuxtype[0].lower()][1].format(resolution,os_dict[linuxtype[0].lower()][0],platform[2],desktop.capitalize()))
    


