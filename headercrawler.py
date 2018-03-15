import requests,pyquery,spyder,scrapy,os
from bs4 import BeautifulSoup
from termcolor import cprint,colored

listadork=[]
listadorksvalidos=[]

class HANDLER:

    def read():
        for x in open("dorks.txt",'r'):
            listadork.append("/"+x.replace('\n',''))
    read()
    def crawler(url):
        for x in listadork:
            try:
                url2 = url + x + "1'"
                page= requests.get(url2)
                contents=page.text
                print(url2)
                if 'deprecated' in contents  :
                    listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
                elif 'You have an error in your SQL syntax' in contents:
                    listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
                elif 'Query fail' in contents:
                    listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
            except:
                    cprint("Ocorreu um erro (Time out talvez?)",'red')
                    continue
    def pelica(url):
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
        if 'deprecated' in contents  :
            cprint("Vulneravel",'red')
        elif 'You have an error in your SQL syntax' in contents:
            cprint("Vulneravel",'red')
        elif 'Query fail' in contents:
            cprint("Vulneravel",'red')
        else:
            cprint("Não foi encontrada vulnerabilidade",'green')
