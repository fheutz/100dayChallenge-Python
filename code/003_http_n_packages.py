import requests 
import time
from colorama import init, Fore

proxy = {
    "http":"",
    "https":""
}

urls = [
    "https://google.com",
    "https://github.com",
]

statusCodes = {
    "20" : Fore.GREEN + "Success \t" + Fore.WHITE,
    "40" : Fore.YELLOW + "Client Error \t" + Fore.WHITE,
    "50" : Fore.RED + "Server Error \t" + Fore.WHITE
}

init()

requests.packages.urllib3.disable_warnings()

def prettyprint(statusCode, requestTime):
    re = statusCodes[str(statusCode)[0:2]]
    re += "Status " + str(statusCode) + " \t"
    if requestTime < 1:
        re += Fore.GREEN + str(requestTime)[0:4] + "s \t" + Fore.WHITE
    elif requestTime >= 1 and requestTime<= 5:
        re += Fore.YELLOW + str(requestTime)[0:4] + "s \t" + Fore.WHITE
    else:
        re += Fore.RED + str(requestTime)[0:4] + "s \t" + Fore.WHITE
    return re
print("Internet")
for url in urls:
    start = time.time()
    #r = requests.get(url, proxies=proxy, verify=False)
    r = requests.get(url, verify=False)
    end = time.time()
    print (prettyprint(r.status_code, end-start), url)