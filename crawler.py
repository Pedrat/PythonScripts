import requests,pyquery,spyder,scrapy,os
from bs4 import BeautifulSoup
from termcolor import cprint,colored
from headercrawler import HANDLER
from threading import Thread as th
import headercrawler as hc

class THREAD:
    def __init__(self):
        self.threads=[]

    def inicia(self,y,x):
        self.threads.append(th(target=ch.thread,args=(y,x)))

    def start(self):
        for x in self.threads:
            x.daemon = True
            x.start()

    def startthread(self,y,x):
        i=0
        self.inicia(y,x)
        self.start()

threads=THREAD
while 1:
    cprint("1- Crawler \n2- Pelica",'blue')
    opc=input("Opção: ")
    if opc == "1":
        url=input("Qual o url?")
        threads.startthread(url,hc.listadork2)
        threads.startthread(url,hc.listadork)
        os.system("clear")
        print("Dorks Validos para o url: "+url+": ")
        for x in HANDLER.listadorksvalidos:
            print(x)

    elif opc =="2":
        print("Bom dia!")
        url=input("Qual é o url?\nUrl: ")
        os.system("clear")
        HANDLER.pelica(url)

    else:
        cprint("Invalido",'red')
        continue
