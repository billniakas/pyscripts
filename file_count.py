import os
import os.path

print(os.getcwd())


def file_count(folder):
    while True:
        dir = "./"+folder
        if dir == '': break
        if os.path.isdir(dir):
            count_files = 0
            for r,d,f in os.walk(dir):
                level = r.replace(dir, '').count(os.sep)
                print(level*'\t',r)
                for fi in f:
                    if fi[0] not in '.~':
                        print((level+1)*'\t',fi)
                        count_files += 1
        print('{} files found'.format(count_files))
        break



# folder="1920x1080"

file_count(folder)
    
