import requests ; from bs4 import BeautifulSoup ; from time import sleep

search_item = "excel"
base = "http://www.google.pt"
url = "http://www.google.pt/search?q=inurl: "+ search_item
response = requests.get(url)
#for x in response: print(x)
soup = BeautifulSoup(response.text,"lxml")
for item in soup.select("body cite"):
    print(item.text)
for next_page in soup.select(".fl"):
    sleep(4)
    res = requests.get(base + next_page.get('href'))
    soup = BeautifulSoup(res.text,"lxml")
    for item in soup.select(".r a"):
        print(item.text)
