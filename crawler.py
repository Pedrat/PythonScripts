import requests,pyquery,spyder,scrapy
from bs4 import BeautifulSoup
from termcolor import cprint,colored
listadork=[]

def read():
    for x in open("dorks.txt",'r'):
        listadork.append(x.replace('\n',''))

read()

url = "http://www.sukkeespa.com/"

while 1:
    cprint("1- Crawler \n2- Pelica",'blue')
    opc=input("Opção: ")
    if opc == "1":
        for x in listadork:
            #for y in range(1,10):
            url2 = url + x + "1'"
            page= requests.get(url2)
            for z in page:
                print(z)

    elif opc =="2":
        print("Bom dia!")
        url=input("Qual é o url?\nUrl: ")
        if 'https' not in url:
            if 'http' not in url:
                while 1:
                    prefix=input("É http ou https?\n")
                    if prefix == "http":
                        prefix='http://'
                        url = prefix + url
                        break
                    elif prefix == "https":
                        prefix ='https://'
                        url = prefix + url
                        break
                    else:
                        cprint("Invalido!",'red')
        cprint(url,'magenta')
        page=requests.get(url+"'")
        contents=page.text
        if 'deprecated' in contents:
            cprint("Vulneravel",'red')

    else:
        cprint("Invalido",'red')
        continue
