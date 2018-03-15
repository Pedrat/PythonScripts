import requests,pyquery,spyder,scrapy,os
from bs4 import BeautifulSoup
from termcolor import cprint,colored
from headercrawler import HANDLER


while 1:
    cprint("1- Crawler \n2- Pelica",'blue')
    opc=input("Opção: ")
    if opc == "1":
        url=input("Qual o url?")
        HANDLER.crawler(url)
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
