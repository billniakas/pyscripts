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
            ######           
           ; #####;          
          +##.#####          
         +##########         
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
         ╔╠╠╠╠╠╠╠╠╚                    ╙║║║║║║║║║ 
  .╓╔╔╓,  ╙╠╠╠╠╠╠╚                      ╙║║║║║║║║Γ
.║║║║║║║║,  ╠╠╠╠╠                        ║║║║║║║║║
║║║║║║║║║║  ╠╠╠╠░                                 
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
      
    linuxtype=re.findall('\w{4,}',platform[2], re.I)
    if len(linuxtype)==0:
        linuxtype=re.findall('\w{4,}[^generic]',platform[3], re.I)
        linuxtype[0]=linuxtype[0].strip(" ")
    else:
        pass
    ostype=("\nYou are using",os_dict[linuxtype[0].lower()][0],platform[2],"\n")
    print(" ".join(ostype))
    print(os_dict[linuxtype[0].lower()][1])
    Input = subprocess.getoutput("xrandr | grep -i '*'")
    resolution=Input.split()[0]


