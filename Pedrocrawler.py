import threading,sys,os
from threading import Thread as th
from time import sleep
import Pedrocrawlerheader as ch
from termcolor import colored,cprint

class threads:

    def __init__(self):
        self.threads=[]

    def inicia(self,x,y):
        self.threads.append(th(target=ch.thread,args=(x,y)))

    def start(self):
        for x in self.threads:
            x.daemon=True
            x.start()

    def startthread(self):
        i=0
        ch.read()
        for x in range(6400,7700):
            i+=1
            if i==100:
                self.inicia(x,(x+100))
                i=0
            else:
                continue
        self.start()

while 1:
    thr=threads()
    cprint("Menu\n1-Adicionar pessoas para a pesquisa do ID\n2-Procurar\n3-Procura calendario por id","cyan")
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
    elif opc == "3":
        os.system("clear")
        cprint("Procurar por id o calendario",'cyan')
        ch.User()
        '''
        opcn=input("")
        while 1:
            cprint("Qual o dia? (01/01/2018)",'cyan')
            data = input("")
            datastrip = data.split("/")
            lista31=[1,3,5,7,8,10,12]
            lista30=[4,6,9,11]
            if (int(datastrip[1]) >= 1) or (int(datastrip[1]) <= 12):
                if int(datastrip[1]) in lista31:
                    print("AQUI31")
                    if (int(datastrip[0]) >= 1) or (int(datastrip[0]) <= 31):
                        ch.calendar(opcn,data)
                    else:
                        cprint("Data invalida!",'red')
                        continue
                elif int(datastrip[1]) in lista30:
                    print("AQUI30")
                    if (int(datastrip[0]) >= 1) or (int(datastrip[0]) <= 30):
                        ch.calendar(opcn,data)
                    else:
                        cprint("Data invalida!",'red')
                        continue
                elif int(datastrip[1]) == 2:
                    if (int(datastrip[0]) >= 1) or (int(datastrip[0]) <= 28):
                        ch.calendar(opcn,data)
                    else:
                        cprint("Data invalida!",'red')
                        continue
                else:
                    cprint("Data invalida!",'red')
                    continue

            else:
                cprint("Data invalida!",'red')
                continue

        #ch.calendar(opcn,date)
        '''
    else:
        os.system("clear")
        cprint("Invalido!",'red',attrs=["bold"])
        continue
