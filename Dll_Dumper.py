import pymem
import time

print("""

██████╗░██╗░░░░░██╗░░░░░  ██████╗░██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░░░░██║░░░░░  ██║░░██║██║░░░██║██╔████╔██║██████╔╝█████╗░░██████╔╝
██║░░██║██║░░░░░██║░░░░░  ██║░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝███████╗███████╗  ██████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░███████╗██║░░██║
╚═════╝░╚══════╝╚══════╝  ╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                                    Dll Dumper
                              Author 1ntrovertskrrt
""")

print('Enter App Process Name \nExample = csgo.exe')
gameProcess = input("Input Game Process: ")

pm = pymem.Pymem(gameProcess)
modules = list(pm.list_modules())
print('Collecting DLL Names')
for module in modules:
    time.sleep(1)
    print(module.name)

print('All dll files Successfully Dumped')
