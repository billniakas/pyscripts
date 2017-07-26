from getpass import getpass
import time
import os

def pause():
    pause = input("Press <ENTER> to continue...")
    
while True:
    
    os.system("clear")
    choice = input('''What's your choice?

    1. Password prompt
    --------------------
    2. Keylogger
    --------------------
    (press <ENTER> to quit)

    choice No : ''')

    if choice == "":quit()

    if int(choice) == 1:

        while True:
            password = getpass()
            if password == "salihcerebrux":
                time.sleep(0.5)
                print("Correct!!!")
                pause()
                break
            else:
                time.sleep(0.5)
                print("invalid password","\r")
                continue
    if int(choice) == 2:
        while True:
            print('''\nThis is a keylogger, everything you type
will be recorded in a text file. Exit the keylogger
by pressing <ENTER> 2 times\n''')
            pause()
            os.system("clear")
            something = getpass(prompt=' ', stream=None)
            if something == "":
                for i in range(5):
                    time.sleep(0.5)
                    print("Exiting"+i*".",end="\r")
                print("\n")
                quit()
            
            with open('log.txt','a') as f:
                f.write(something+"\n")
                f.close
                continue

    

