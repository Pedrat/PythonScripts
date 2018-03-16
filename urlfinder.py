import requests,sys,os
from time import sleep
from termcolor import colored,cprint
from bs4 import BeautifulSoup
atencao=colored('ATENÇÃO!', 'red', attrs=['bold', 'underline'])
def limpa():
    os.system("clear")

def save(cena):
    file = open("urlsdorks.txt",'a')
    file.write(cena+'\n')
    file.close()

def listadorks():
    limpa()
    for x in open("dorks.txt",'r'):
        print(x)

def googlesearcher(search_item):
    base = "http://www.google.pt"
    url = "http://www.google.pt/search?q=inurl:"+ search_item
    print("A procurar em: "+ url)
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text,"lxml")
    for item in soup.select("body cite"):
        if "www" in item.text:
            save(item.text)
            print(item.text)
    for next_page in soup.select(".fl"):
        sleep(10)
        res = requests.get(base + next_page.get('href'))
        soup = BeautifulSoup(res.text,"lxml")
        for item in soup.select("body cite"):
            if "www" in item.text:
                save(item.text)
                print(item.text)

def menu():
    while 1:
        #limpa()
        opc=input("1-Procura websites com vulnerabilidades possiveis.\n2-Listar os Dorks ("+atencao+" é uma lista muito grande!)\nDiga sair para sair\n")
        if opc=="1":
            dork=input("Qual é o dork que quer pesquisar?\n"+colored("Dork",'yellow',attrs=["bold"])+':')
            googlesearcher(dork)
        elif opc == "2":
            listadorks()
        elif opc.lower() == "sair":
            limpa()
            print("Até a proxima!")
            break
        else:
            limpa()
            continue
if __name__ == "__main__":
    menu()
