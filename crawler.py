import threading,sys,os
from threading import Thread as th
from time import sleep
import crawlerheader as ch
from termcolor import colored,cprint

class threads:

    def __init__(self):
        self.threads=[]

    def inicia(self,x,y):
        #print("AQUI2")
        self.threads.append(th(target=ch.thread,args=(x,y)))

    def start(self):
        #print("AQUI")
        for x in self.threads:
            x.daemon=True
            x.start()
    def startthread(self):
        i=0
        #print("AQUI#")
        ch.read()
        for x in range(5900,8001):
            i+=1
            if i==100:
                self.inicia(x,(x+100))
                i=0
            else:
                continue
        self.start()

while 1:
    thr=threads()
    #cprint("sad ","red")
    #os.system("clear")
    cprint("Menu\n1-Adicionar pessoas para a pesquisa do ID\n2-Procurar","cyan")
    opc=input("")
    if opc == "1":
        os.system("clear")
        cprint("Qual é o nome?\n","cyan")
        opcn=input("")
        ch.write(opcn)
    elif opc == "2":
        os.system("clear")
        thr.startthread()
        cprint("Processos a correr em Background!",'red')
