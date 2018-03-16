import requests,pyquery,spyder,scrapy,os,sys
from bs4 import BeautifulSoup
from termcolor import cprint,colored
from headercrawler import HANDLER
from threading import Thread as th
import urlfinder
import headercrawler as hc
listad=[]
class THREAD:
    def __init__(self):
        self.threads=[]

    def inicia(self,y,x):
        for i in range(0,2):
            self.threads.append(th(target=HANDLER.crawler,args=(y,x[i])))

    def start(self):
        for x in self.threads:
            x.daemon = True
            x.start()

    def startthread(self,y,x):
        i=0
        self.inicia(y,x)
        #self.start()


def menu():
    threads=THREAD()
    while 1:
        #cprint("1- Crawler \n2- Pelica\n3-Sair\n4-googledork searcher",'blue')
        opc=input(colored("1- Crawler \n2- Pelica\n3- Google Dorks Searcher\n4- Crawler pelo ficheiro\nEscreva sair\nOpção: ",'blue'))
        if opc == "1":
            url=input("Qual o url?")
            threads.startthread(url,hc.listadorks)
            threads.start()
            os.system("clear")
            print("Dorks Validos para o url: "+url+": ")
            for x in hc.listadorksvalidos:
                print(x)

        elif opc =="2":
            print("Bom dia!")
            url=input("Qual é o url?\nUrl: ")
            os.system("clear")
            HANDLER.pelica(url)

        elif opc.lower() =="sair":
            os.system("clear")
            print("Adeus")
            sys.exit(1)

        elif opc == "3":
            urlfinder.menu()

        elif opc == "4":
            for x in open("dorks.txt",'r'):
                listad.append(x)
            for x in open("urlsdorks.txt",'r'):
                if x[(len(x)-1):] == "/":
                    threads.startthread(x,listad)
                else:
                    threads.startthread(x+"/",listad)
            threads.start()
        elif opc == "5":
            print("Bom dia!")

        else:
            os.system("clear")
            cprint("Invalido",'red')
            continue
if __name__=="__main__":
    menu()
