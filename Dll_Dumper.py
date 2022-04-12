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

def Ascii():
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

while True:
    def main():
        Ascii()
        mainMenu()
        try:
            gameProcess = input("Input App Process: ")
            pm = pymem.Pymem(gameProcess)
        except:
            print(Fore.RED + "Can't find the app process")
            time.sleep(2)
            os.system('cls')
            return main()

        modules = list(pm.list_modules())
        print(Fore.GREEN + 'Collecting DLL List...')
        time.sleep(3)

        file = open('dllList.txt', 'w')
        for module in modules:
            time.sleep(0.5)
            global dllList
            dllList = print(str(Fore.WHITE + 'Collected '+module.name))
            dllList = file.write(str(module.name + '\n'))
        file.close()

        print(Fore.GREEN + 'All dll files Successfully Dumped')

        os.system('pause')
        os.system('cls')
        os.startfile('dllList.txt')
    
    main()

