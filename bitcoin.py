import requests,os,json

url="https://api.coindesk.com/v1/bpi/currentprice/allcurrencies.json?showex=1&calc=1"
#jsond = json.loads(page.text)
contents = requests.get(url)
jsons = json.loads(contents.text)
'''
for x in contents:
    if b'class="symbol"' in x:
        print(x)
'''
jsons=str(jsons)
print(jsons)
#for x in jsons:
    #if "EUR" in x:
    #print(x)
