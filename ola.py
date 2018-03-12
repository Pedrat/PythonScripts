from time import sleep
import os,shutil,random
from termcolor import cprint, colored

listacores=['magenta','blue','cyan','white']
listacores2=['grey','red','green','yellow']

while 1:
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    cara1="*.*"
    cara2="*-*"
    espacos="\n"*(lines//2)
    cara1=cara1.center(columns)
    cara2=cara2.center(columns)
    os.system("clear")
    cprint(espacos+cara1,random.choice(listacores))
    sleep(0.15)
    os.system("clear")
    cprint(espacos+cara2,random.choice(listacores2))
    sleep(0.15)
