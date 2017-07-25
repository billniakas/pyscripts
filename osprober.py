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
                ######                 Screen Resolution : {}
               ; #####;                Operating System  : {}
              +##.#####                Kernel Version    : {} 
             +##########               Desktop           : {}
            #############;             Total Memory      : {:1.2F} GB
           ###############+            Free Memory       : {:1.2F} GB
          #######   #######            Active Memory     : {:1.2F} GB 
        .######;     ;###;`".          System Uptime     : {}
       .#######;     ;#####.           CPU               : {}
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
         ╔╠╠╠╠╠╠╠╠╚                    ╙║║║║║║║║║           Screen Resolution : {}
  .╓╔╔╓,  ╙╠╠╠╠╠╠╚                      ╙║║║║║║║║Γ          Operating System  : {}
.║║║║║║║║,  ╠╠╠╠╠                        ║║║║║║║║║          Kernel Version    : {} 
║║║║║║║║║║  ╠╠╠╠░                                           Desktop           : {}
╚║║║║║║║║╠  ╠╠╠╠░                        ╓»»»»»»»»          Total Memory      : {:1.2F} GB
 ╙╚║║║║╚╙  #╠╠╠╠╠∩                       ▓▓▓▓▓▓▓▓▒          Free Memory       : {:1.2F} GB
         ╔╠╠╠╠╠╠╠╠,                    \▓▓▓▓▓▓▓▓▓           Active Memory     : {:1.2F} GB 
         `╠╠╠╠╠╠╠╠╠∩                  #▓▓▓▓▓▓▓▓▓Ñ           System Uptime     : {}  
           ╠╠╠╠╠╠╠╠╠╠              ╓@▓▓▓▓▓▓▓▓▓▓╜            CPU               : {}
            ╙╠╠╠╠╠╠╚   ┌▓▓₧MmmM₧▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
              ╙╠╠╠∩   ╓▓▓▓▓▓▓▓▓▓▓▓▓▓▀░      └     
                `    #▓▓▓▓▓▓▓▓▓▓▓▓▓  ╓∩╠╠╠╠∩╔     
                    "▀▓▓▓▓▓▓▓▓▓▓▓▓  #╠╠╠╠╠╠╠╠░    
                          └└└└└└    ╠╠╠╠╠╠╠╠╠╠    
                                     ╚╠╠╠╠╠╠╠     
                                       └╙╙╙       '''],"linux mint":["Linux Mint",'''
  
     ...................................                
     .                                    ..            
     .                    ............       .          
     .    ...........................'''..     .        
     .    ........   ..............''''''''..   .           Screen Resolution : {}
     .       .....   .............'......',,,.   .          Operating System  : {}
     .         ...   ......               .,,,    .         Kernel Version    : {}
          .    ...   .'''    ...     ...   .,,.   .         Desktop           : {}
          .    ''.   .'''   .'''.   .,,,.   ,,.   .         Total Memory      : {:1.2F} GB
          .    ''.   .'''   .,,,.   .,,,.   ,,.   .         Free Memory       : {:1.2F} GB
          .    ''.   .,,'   .,,,.   .,,,.   ,,.   .         Active Memory     : {:1.2F} GB 
          .    ','   .,,,   .,,,'   .,,,.   ,,.   .         System Uptime     : {}
          .    ,,'   .,,,''',;;;,,,,,,,,....,,.   .         CPU               : {}
               ,,,    ,,;;;;;;;;;;;;;;,,....,,.   .     
           .   .,,'    ......'''''''''.....,,,.   .     
            .   .,;,.        ............',,,,.   .     
             .    .,;;;,',,,,,,,,,,,,,;;;;;;,,.   .     
              .     ..',;::::::::::::;;;;;;;,.    .     
                                                  .     
                                                  .     
                                                        
          d                    '.''..'       '          
          d   .'.;;,.:  ;',  :.' .;  ;.. ... ,'         
          d   ;:o. c:x  d,o':c.'  ;  ;.',. .',          
          o...;:o. ::d..d,o.;o.' .;  ;.',. .',          
          .::;'';  '..::.., .:..  .  '.... ...          
          .     .    .  . .  .                      ''']}                                                         
                                                                          

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
    memactive = memtotal-memfree
    uptime = subprocess.getoutput("uptime -p")
    cpu = subprocess.getoutput("cat /proc/cpuinfo | grep '''model name''' | head -n1").replace("\t","")
    
    #print(" ".join(ostype))
    os.system("clear")		
    print("\n",os_dict[linuxtype[5:].lower()][1].format(resolution,os_dict[linuxtype[5:].lower()][0],platform[2],desktop,memtotal,memactive,memfree,uptime[3:],cpu[12:].replace("   "," ")))
    print("\n"*2)
    


