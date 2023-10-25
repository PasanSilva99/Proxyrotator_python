import requests
import random
import os
import socket



def check_proxy(proxy):
    try:
        response = requests.get('target website address', proxies={'http': proxy, 'https': proxy}, timeout=10)
        if response.status_code == 200:
            return True
        else:
            return False
        
    except:
        return False

#insert the proxy server addresses and ports    
proxies = ['example.com:port', ]
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

response =  requests.get("target website address", timeout = 5)

print(response.status_code)
