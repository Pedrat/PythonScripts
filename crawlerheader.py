import requests,os,sys
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

def thread(num,num2):
    for num in range(num,(num2+1)):
        try:
            num=str(num)
            url = "http://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId="+num+"&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1520208000&end=1520812800&_=1520509039082"
            page = requests.get(url)
            page=str(page.content)
            print(num)
            if "como Formador" in page:
                for x in listaform:
                    if x in page:
                        cprint(x+" "+num,"red")
                        save(x,num)
                        num=int(num)
            else:
                continue
            sys.exit(1)
        except:
            num=int(num)
            num-=1
            continue

def write(nome):
    file = open("nomesprocurar.txt",'a')
    file.write(nome+'\n')
    file.close()
