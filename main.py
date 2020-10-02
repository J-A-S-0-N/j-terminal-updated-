# all import 
import psutil
from datetime import datetime
import platform
import os
from time import sleep
from os import system

# for colored text
greentext = '\033[32m'
redtext = '\033[31m'
yellowtext = '\33[33m'
whitetext = '\33[37m'


# change the diractory to the main 
os.chdir("C:\\Users\\jason\\Desktop")

# get the current direcory for printing it
current_dir = os.getcwd()
# variable for sleeping sleep(2)
timeToSleep = 2

#master key which will unluck more function
master_key = None

global current_dir_str
# this is the current dirctory its for changing dircory later it will append it and then chdir
current_dir_str = 'C:\\Users\\jason\\Desktop'

#function for changing diracotry
def chdir(dir):
    os.chdir(dir)

def get_master_key():
    os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\j terminal")
    masterkeyfile = open("masterkey.txt")
    master_key = masterkeyfile.readline()
    masterkeyfile.close()
    master_key.strip()
    os.chdir(current_dir_str)
    return master_key

def write_new_master_key(new_key):
    os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\j terminal")
    masterkeyfile = open("masterkey.txt", "w")
    masterkeyfile.truncate()
    masterkeyfile.write(new_key)
    masterkeyfile.close()

    masterkeyfile = open('masterkey.txt', 'r')
    master_key = masterkeyfile.readline()
    os.chdir(current_dir_str)
    masterkeyfile.close()
    return master_key


#function for deliting a folder *not file
def del_folder(foldername):
    os.remove(current_dir_str + "\\" + foldername)
    # print("it has been successfully deleted")
    # sleep(timeToSleep)


def del_file(filename):
    pass

#function for reading text file not yet docs or pdf 
def read_file(filename):
    while True:
        system("cls")
        file_to_read = open(filename, mode="r")

        contents = file_to_read.read()
        print(contents)

        print("enter 'yes' if you are done")
        read_file_inp = input("")
        if read_file_inp in ["yes", "yup", "y", "Y", "YES"]:
        #if read_file_inp == "yes" or read_file_inp == "Yes" or read_file_inp == "YES":
            file_to_read.close()
            break
        else:
            system("cls")
            print("please enter 'yes'")
            sleep(timeToSleep)

def change_dir_name(additional, current_dirarort = current_dir_str):
    current_dir = current_dir_str + "\\" + additional
    print(current_dir_str)
    # current_dir = current_dir_str
    return current_dir

# get the computer status
def comstatus():
    print("="*30, "System Information", "="*30)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

# print out the help which contains all the command
def tutorial(master):
    if master == True:
        print("res = reset the terminal")
        print("cs = conputer status")
        print("help = print out the tutorial")
        print("echo;string = this will print the string")
        print("time = print out the current time")
        print("help = print out the tutorial")
        print("ls;ff = list the file/folder")
        print("ls;p = list all the path")
        print("cs = get the info about the computer")
        print("cls = clear the screen")
        print("ver = print out the version of you os")
        print("cpuinfo = print out the cpuinfo")
        print("cpuinfo;use")
        print("c;path = change dir")
        print("cr;path = reletive path")
        print("mkfil;name = make an file")
        print("mkfol;name  = make an folder")
        print("delfol;name = delete filder")
        print("delfil;name = delete file")
        print("rnfil;name;newname = rename the name to new name")
        print("rnfol;name;newname = rename the name to new name")
        print("color;help = get all the color")
        print("color;name = change the text color")
        print("exe;name = run the exe file")
        print("changemas(change master) = change the master key")
        print("prmas(print master) = print the master key")
    else:
        print("help = print out the tutorial")
        print("res = reset the terminal")
        print("cs = conputer status")        
        print("c;path = change dir")
        print("help = print out the tutorial")
        print("cpuinfo = print out the cpuinfo")
        print("cpuinfo;use")
        print("cls = clear the screen")
        print("ls;p = list all the path")
        print("echo;string = this will print the string")
        print("master = this will make you the master")

def color_help():
    print("color;1 = green")
    print("color;2 = yellow")
    print("color;3 = white")
    print('color;4 = red')
        

# this creates a file 
def create_file(filename):
    os.mkdir(filename)
    # print("the file has been successfully made")

# not used

# def start():
#     return 0
#     print("J terminal by Jason")
#     sleep(timeToSleep)
#     system("cls")
#     print("* read file can only be txt file")
#     sleep(timeToSleep + 4)
#     system("cls")

# not used

# this get all the available direcoty reletive to your path
def dir_list():
    # print("available directory")
    available_dir = os.listdir()
    for i in range(0,len(available_dir)):
        i_list = list(available_dir[i])
        if "." in i_list:
            i+=1
        else:
            print(available_dir[i])

# this prints current diractoy 
def current_directory():
    print(os.getcwd())

# main loop
def main():
    while True:
        '''
        res = reset the terminal
        cs = conputer status
        help = print out the tutorial
        ls:ff = list the file/folder
        ls = list all the path
        c:path = change dir
        cr:path = reletive path
        mkfil:name = make an file
        mkfol:name  = make an folder
        delfol:name = delete folder
        delfil:name = delete file
        rnfil:name:newname = rename the name to new name
        rnfol:name:newname = rename the name to new name
        echo:string = this i will print the string
        time = print out the current time
        '''
        system("cls")
        print("Jason terminal [Version 0.9 beta]")
        print("(c) 2020 Jason Corporation. All rights reserved.")
        print("\nyou can enter \"help\" to get all the command line")
        print("\n")
        master_key = get_master_key()
        master = False
        textcolor = whitetext
        while True:
            if master == True:
                inpSplitFirst = None
                inpSplitSeccond = None
                inpSplitThird = None
                current_dir = os.getcwd()
                inp = input(textcolor + current_dir + yellowtext + "$" + redtext + "root" + whitetext + ">")
                inpSplit = inp.split(";")
                inpSplitFirst = inpSplit[0]
                if len(inpSplit) == 3:
                    inpSplitSeccond = inpSplit[1]
                    inpSplitThird = inpSplit[2]
                elif len(inpSplit) == 2:
                    inpSplitSeccond = inpSplit[1]
                if inpSplitFirst == "c" and inpSplitSeccond != None:
                    current_dir_str = change_dir_name(inpSplitSeccond)
                    # print(current_dir_str)
                    chdir(current_dir_str)
                if inpSplitFirst == "color" and inpSplitSeccond != None:
                    if inpSplitSeccond == "help":
                        color_help()
                    elif inpSplitSeccond == "1":
                        textcolor = greentext
                    elif inpSplitSeccond == "2":
                        textcolor = yellowtext 
                    elif inpSplitSeccond == "3":
                        textcolor = whitetext
                    elif inpSplitSeccond == "4":
                        textcolor = redtext
                    else:
                        pass
                elif inpSplitFirst == "mkfil" and inpSplitSeccond != None:
                    pass
                elif inpSplitFirst == "mkfol" and inpSplitSeccond != None:
                    create_file(inpSplitSeccond)
        
                elif inpSplitFirst == "delfol" and inpSplitSeccond != None:
                    del_folder(inpSplitSeccond)
        
                elif inpSplitFirst == "delfil":
                    pass
            
                elif inpSplitFirst == "rnfil":
                    pass
    
                elif inpSplitFirst == "rnfol":
                    pass
                
                elif inpSplitFirst == "help":
                    tutorial(True)
    
                elif inpSplitFirst == "ls":
                    if inpSplitSeccond == "ff":
                        pass
                    elif inpSplitSeccond == None:
                        dir_list()
    
                elif inpSplitFirst == "cls":
                    system("cls")
    
                elif inpSplitFirst == "help":
                    tutorial(True)
    
                elif inpSplitFirst == "cs":
                    comstatus()
    
                elif inpSplitFirst == "echo":
                    print(inpSplitSeccond)
    
                elif inpSplitFirst == "time":
                    currentTime = str(datetime.now())
                    print("current time is \"" + currentTime + "\"")
    
                elif inpSplitFirst == "ver":
                    print(platform.system() + " " +platform.release())
    
                elif inpSplitFirst == "cpuinfo":
                    if inpSplitSeccond == "use":
                        print("cup useage : " + str(psutil.cpu_percent()))
                        print("physical memory useage : " + str(psutil.virtual_memory()))
                    elif inpSplitSeccond == None:
                        pass
    
                elif inpSplitFirst == "quit":
                    system("cls")
                    print("are you sure?")
                    quitinp = input("> ")
                    if quitinp in ["y", "yes", "Yes"]:
                        quit()
                    else:
                        pass

                elif inpSplitFirst == "changemas":
                    breakchecker2 = False

                    while True:
                        if breakchecker2 == True: break
                        print("enter the new password")
                        inp = input("> ")
                        while True:
                            print("enter the original password")
                            inp2 = input("> ")
                            if inp2 == master_key:
                                break
                            else:
                                print("retry")
                        while True:
                            print('are you sure its \"' + inp + "\"")
                            inp2 = input("> ")
                            if inp2 in ["yes", "y"]:
                                master_key = write_new_master_key(inp)
                                breakchecker2 = True
                                break
                            else:
                                print("please enter yes")

                elif inpSplitFirst == "prmas":
                    print("master key "+master_key)

    
                elif inpSplitFirst == "res":
                    system("cls")
                    print("reseting")
                    print("[::              ]")
                    sleep(1.5)
                    system("cls")
                    print("reseting")
                    print("[::::::          ]")
                    sleep(1.3)
                    system("cls")
                    print("reseting")
                    print("[::::::::::      ]")
                    sleep(1.3)
                    system("cls")
                    print("reseting")
                    print("[::::::::::::::  ]")
                    sleep(1)
                    system("cls")
                    print("reseting")
                    print("[::::::::::::::::]")
                    sleep(0.4)
                    break
                else:
                    print(textcolor+"\"" + textcolor + inp + textcolor + "\" is not recognized as a command")
            else:
                #no master key 
                inpSplitFirst = None
                inpSplitSeccond = None
                inpSplitThird = None
                current_dir = os.getcwd()
                inp = input(textcolor + current_dir + whitetext +">")
                inpSplit = inp.split(";")
                inpSplitFirst = inpSplit[0]
                if len(inpSplit) == 3:
                    inpSplitSeccond = inpSplit[1]
                    inpSplitThird = inpSplit[2]
                elif len(inpSplit) == 2:
                    inpSplitSeccond = inpSplit[1]
                if inpSplitFirst == "c" and inpSplitSeccond != None:
                    current_dir_str = change_dir_name(inpSplitSeccond)
                    print(current_dir_str)
                    chdir(current_dir_str)
                elif inpSplitFirst == "help":
                    tutorial(False)
    
                elif inpSplitFirst == "ls":
                    if inpSplitSeccond == "ff":
                        pass
                    elif inpSplitSeccond == None:
                        dir_list()
    
                elif inpSplitFirst == "cls":
                    system("cls")
    
                elif inpSplitFirst == "help":
                    tutorial()
    
                elif inpSplitFirst == "cs":
                    comstatus()
    
                elif inpSplitFirst == "echo":
                    print(inpSplitSeccond)
    
                elif inpSplitFirst == "time":
                    currentTime = str(datetime.now())
                    print("current time is \"" + currentTime + "\"")
    
                elif inpSplitFirst == "ver":
                    print(platform.system() + " " +platform.release())
    
                elif inpSplitFirst == "cpuinfo":
                    if inpSplitSeccond == "use":
                        print("cup useage : " + str(psutil.cpu_percent()))
                        print("physical memory useage : " + str(psutil.virtual_memory()))
                    elif inpSplitSeccond == None:
                        pass
                elif inpSplitFirst== "master":
                    breakchecker1 = False
                    # if master_key == None:
                    #     while True:
                    #         system("cls")
                    #         print("you dont have a master key would you like to set one up?")
                    #         inp = input("> ")
                    #         if inp in ["yes", "y"]:
                    #             print("enter the new password")
                    #             inp = input("> ")
                    #         elif inp in ["no", "n"]:
                    #             break
                        
                    system("cls")
                    for i in range(0,3):
                        if breakchecker1 == True:break
                        if master_key == "None":
                            while True:
                                system("cls")
                                print("you dont have a master key would you like to set one up?")
                                inp = input("> ")
                                if inp in ["yes", "y"]:
                                    print("enter the new password")
                                    inp = input("> ")
                                    while True:
                                        print('are you sure its \"' + inp + "\"")
                                        inp2 = input("> ")
                                        if inp2 in ["yes", "y"]:
                                            break
                                    master_key = write_new_master_key(inp)
                                    breakchecker1 = True
                                    break
                                elif inp in ["no", "n"]:
                                    breakchecker1 = True   
                                    break

                        print("password")
                        passinp = input("> ")
                        if passinp == master_key:
                            master = True
                            break
                        print("retry")
                        print("\n")
    
                elif inpSplitFirst == "quit":
                    system("cls")
                    print("are you sure?")
                    quitinp = input("> ")
                    if quitinp in ["y", "yes", "Yes"]:
                        quit()
                    else:
                        pass
    
                elif inpSplitFirst == "res":
                    system("cls")
                    print("reseting")
                    print("[::              ]")
                    sleep(1.5)
                    system("cls")
                    print("reseting")
                    print("[::::::          ]")
                    sleep(1.3)
                    system("cls")
                    print("reseting")
                    print("[::::::::::      ]")
                    sleep(1.3)
                    system("cls")
                    print("reseting")
                    print("[::::::::::::::  ]")
                    sleep(1)
                    system("cls")
                    print("reseting")
                    print("[::::::::::::::::]")
                    sleep(0.4)
                    break
                else:
                    print("\"" + inp + "\" is not recognized as a command")
            print("\n")
        

if __name__ == "__main__":
    system("cls")
    main()