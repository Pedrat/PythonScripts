import requests,pyquery,spyder,scrapy,os
from bs4 import BeautifulSoup
from termcolor import cprint,colored
from threading import Thread as th

listadork=[]
listadork2=[]
listadorksvalidos=[]
listadorks=[listadork,listadork2]
valida=1
class HANDLER:

    def read():
        tamanho=0
        i=0
        for x in open("dorks.txt",'r'):
		          tamanho+=1
        for x in open("dorks.txt",'r'):
            if i<=(tamanho//2):
                listadork.append("/"+x.replace('\n',''))
                i+=1
            else:
                listadork2.append('/'+x.replace('\n',''))
                i+=1

    read()
    def crawler(url,lista):

        for x in lista:
            if valida == 1:
                #try:
                if 1==1:
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
            #    except:
                    #    cprint("Ocorreu um erro (Time out talvez?)",'red')
                    #    continue
            else:
                sys.exit(1)
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
