import pymem
import win32api
import time
import os
import subprocess
import colorama

from pymem import *
from colorama import Fore
from pathlib import Path

colorama.init()
print(Fore.WHITE + """

██████╗░██╗░░░░░██╗░░░░░  ██████╗░██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░░░░██║░░░░░  ██║░░██║██║░░░██║██╔████╔██║██████╔╝█████╗░░██████╔╝
██║░░██║██║░░░░░██║░░░░░  ██║░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝███████╗███████╗  ██████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░███████╗██║░░██║
╚═════╝░╚══════╝╚══════╝  ╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                                    Dll Dumper
                              Author 1ntrovertskrrt
""")
print(Fore.BLUE + '                   Github: https://github.com/RizkyNugroho666\n')                    

def mainMenu():
    print(Fore.WHITE + 'Enter App Process Name \nExample = csgo.exe')

mainMenu()

def main():
    try:
        gameProcess = input("Input App Process: ")
        pm = pymem.Pymem(gameProcess)
    except:
        print("Can't find the app process")
        os.system('pause')
        return

    modules = list(pm.list_modules())
    print(Fore.GREEN + 'Collecting DLL List...')
    time.sleep(3)

    file = open('dllList.txt', 'w')
    for module in modules:
        time.sleep(1)
        global dllList
        dllList = print(str(Fore.WHITE + 'Collected '+module.name))
        dllList = file.write(str(module.name + '\n'))
    file.close()

    print(Fore.GREEN + 'All dll files Successfully Dumped')

    os.system('pause')
    os.startfile('dllList.txt')

main()
