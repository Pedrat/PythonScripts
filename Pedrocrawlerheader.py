import requests,os,sys,json,codecs,time
import threading
from time import sleep
from termcolor import colored,cprint

listaform=[]
valida=0
contagem=0
def read():
    del listaform[:]
    for x in open("nomesprocurar.txt",'r'):
        listaform.append(x.replace('\n',''))


for x in os.popen("ls"):
    if "IDs.txt" in x:
        valida = 1
        break
if valida == 0:
    file=open("IDs.txt",'w')
    file.write("Bom dia!\n")
    file.close()
else:
    print("File ja existe!")

def save(nome,num):
    if nome == "a Furtado Duarte":
        nome = "Graça Duarte"
    file=open("IDs.txt",'a')
    file.write(nome+' com o id de: '+num+'\n')
    file.close()

def Corrige(word):
    if "\\xc3\\xa1" in word: word=word.replace("\\xc3\\xa1","á")
    if "\\xc3\\xa2" in word: word=word.replace("\\xc3\\xa2","â")
    if "\\xc3\\xa3" in word: word=word.replace("\\xc3\\xa3","ã")
    if "\\xc3\\x82" in word: word=word.replace("\\xc3\\x82","Â")
    if "\\xc3\\x81" in word: word=word.replace("\\xc3\\x81","Á")
    if "\\xc3\\xa4" in word: word=word.replace("\\xc3\\xa4","ä")
    if "\\xc3\\xa9" in word: word=word.replace("\\xc3\\xa9","é")
    if "\\xc3\\xaa" in word: word=word.replace("\\xc3\\xaa","ê")
    if "\\xc3\\x89" in word: word=word.replace("\\xc3\\x89","É")
    if "\\xc3\\xad" in word: word=word.replace("\\xc3\\xad","í")
    if "\\xc3\\xb4" in word: word=word.replace("\\xc3\\xb4","ô")
    if "\\xc3\\xb3" in word: word=word.replace("\\xc3\\xb3","ó")
    if "\\xc3\\xb5" in word: word=word.replace("\\xc3\\xb5","õ")
    if "\\xc3\\x93" in word: word=word.replace("\\xc3\\x93","Ó")
    if "\\xc3\\xba" in word: word=word.replace("\\xc3\\xba","ú")
    if "\\xc3\\xa7" in word: word=word.replace("\\xc3\\xa7","ç")
    if "\\xc3\\xb1" in word: word=word.replace("\\xc3\\xb1","ñ")
    return word


def thread(num,num2):
    for num in range(num,(num2+1)):
        if 1==1:
        #try:
            num=str(num)
            url = "http://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId="+num+"&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1520208000&end=1520812800&_=1520509039082"
            page = requests.get(url)
            page=str(page.content)
            #print(num)
            if "como Formador" in page:
                #cprint("BOM DIA! ",'red')
                page = page[page.rfind("Formador"):]
                #cprint("CARALHO",'red')
                page = page.split("\\\\")
                #cprint("DEI SPLIT",'red')
                page = page[4][5:]
                page = Corrige(page)
                cprint("Encontrei o "+page+' com o id de '+num,'red')
                f = open("Formadores.txt","a")
                f.write(str(num) + " -" + str(page) + "\n")
                f.close()

            else:
                continue

        #except:
        #    num=int(num)
        #    num-=1
        #    continue
        sys.exit(1)

def calendar(num,date):
    lista=[]
    url = "http://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId="+num+"&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1520208000&end=1520812800&_=1520509039082"
    page = requests.get(url)
    jsonconv=json.loads(page.text)
    #print(jsonconv)
    for x in jsonconv:
        #print(x["title"])
        lista.append(x["title"]+'\n')

    file = codecs.open("teste.html", mode="w",encoding="utf-8-sig")
    for x in str(jsonconv):
        #print(x)
        file.write(x)
    file.close()
    os.system("clear")
    cprint("Concluido.",'red')

def User():

        #fckme=""
        os.system("clear")
        #ola = ""
        x = input("Qual o ID que quer procurar?\n")
        url = "http://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId="+x+"&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1520208000&end=1520812800&_=1520508461232"
        contents = requests.get(url)
        fckme=json.loads(contents.text)
        lista = []
        for x in fckme:
            ola = (str(x["title"])+' Start: '+str(time.ctime(float(x["start"])))+' End: '+str(time.ctime(float(x["end"]))))
            lista.append(ola)
        print(lista)
        while True:
            os.system("clear")
            opc = input("1. Procura por Hora\n2. Procura por Dia\n3. Procura por Mês\n4. Procura por Ano\n0. Sair\n")
            if opc == "1":
                os.system("clear")
                opc = input("Hora (00:00:00): ")
                for x in lista:
                    if opc in x:
                        print(x)
                exit = input("Press any key...")
            elif opc == "2":
                os.system("clear")
                opc = input("Dia (ex: Fri, Sun, Wed): ")
                for x in lista:
                    if opc in x:
                        print(x)
                exit = input("Press any key...")
            elif opc == "3":
                os.system("clear")
                opc = input("Mês (ex: Jul, Sep, Oct): ")
                for x in lista:
                    if opc in x:
                        print(x)
                exit = input("Press any key...")
            elif opc == "4":
                os.system("clear")
                opc = input("Ano (ex:2018): ")
                for x in lista:
                    if opc in x:
                        print(x)
                exit = input("Press any key...")
            elif opc == "0":
                break
            else:
                print("Insira uma opção valida!")
                exit = input("Press any key...")

def write(nome):
    file = open("nomesprocurar.txt",'a')
    file.write(nome+'\n')
    file.close()
