import pymem
import win32api
import time
import os
import subprocess

from pymem import *
from pathlib import Path

print("""

██████╗░██╗░░░░░██╗░░░░░  ██████╗░██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░░░░██║░░░░░  ██║░░██║██║░░░██║██╔████╔██║██████╔╝█████╗░░██████╔╝
██║░░██║██║░░░░░██║░░░░░  ██║░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝███████╗███████╗  ██████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░███████╗██║░░██║
╚═════╝░╚══════╝╚══════╝  ╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                                    Dll Dumper
                              Author 1ntrovertskrrt
                    Github: https://github.com/1ntrovertskrrt
""")

def mainMenu():
    print('Enter App Process Name \nExample = csgo.exe')

mainMenu()

def main():
    try:
        gameProcess = input("Input Game Process: ")
        pm = pymem.Pymem(gameProcess)
    except:
        print("Can't find the app process")
        return

    modules = list(pm.list_modules())
    print('Collecting DLL List...')
    time.sleep(3)

    file = open('dllList.txt', 'w')
    for module in modules:
        #time.sleep(1)
        global dllList
        dllList = print(str(module.name))
        dllList = file.write(str(module.name + '\n'))
    file.close()

    print('All dll files Successfully Dumped')

    os.system('pause')
    os.startfile('dllList.txt')

main()
