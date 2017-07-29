import os
import os.path

print(os.getcwd())

folder=input("Give a path : ")
def file_count(folder):
    homefolder="~/"
    if folder == "~/" and len(folder)==2:
            folder = "/home/"
    if homefolder in folder:
            folder="/home/"+folder.replace("~/","")
    
    
    while True:
        dir = folder
               
        if dir == '': break
        
        else:
            if os.path.isdir(dir):
                count_files = 0
                for r,d,f in os.walk(dir):
                    level = r.replace(dir, '').count(os.sep)
                    
                    print(level*'\t',r)
                    for fi in f:
                        if fi[0] not in '.~':
                            print((level+1)*'\t',fi,"\r")
                            count_files += 1
        print('{} files found'.format(count_files))
        break





file_count(folder)
    
