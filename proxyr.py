import requests
import random
import os
import socket



def check_proxy(proxy):
    try:
        response = requests.get('https://google.com', proxies={'http': proxy, 'https': proxy}, timeout=10)
        if response.status_code == 200:
            return True
        else:
            return False
        
    except:
        return False

#insert the proxy server addresses and ports this includes open proxy servers    
proxies = ['167.172.238.6:10000','110.232.67.43:55443', '67.43.236.20:19453', '78.107.235.8:3131', '165.0.136.30:8080', '80.64.142.115:31337', '134.19.254.2:21231', '80.64.142.115:31337', '64.225.8.132:10002', '154.58.202.47:1337', '202.86.138.18:8080', '20.205.61.143:80']
working_proxies = []

for proxy in proxies:
    if check_proxy(proxy):
        working_proxies.append(proxy)

for proxy in working_proxies:
    print(proxy)


def rotate_proxy(proxies):
    proxy = random.choice(proxies)
    return proxy

proxy = rotate_proxy(working_proxies)

os.environ['HTTP_PROXY'] = proxy
os.environ['HTTPS_PROXY'] = proxy

response =  requests.get("https://tecxick-soft.com", timeout = 5)

print(response.status_code)
