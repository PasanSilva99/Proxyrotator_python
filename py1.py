import requests
import random

proxy_list = [
    "http://154.70.107.81:3128",
    "https://85.112.193.37:8080",
    
]

url = "https://ipinfo.io/json"
url2 = "https://tecxick-soft.com"

def make_request(url, proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }

    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            
            print(response.json()['country'])
            print(response.json()['region'])
            print(response.json()['ip'])
            return response.text
        else:
            return None
        
    except Exception as e:
        print(f"Request error: {e}")
        return None
    
random.shuffle(proxy_list)

for proxy in proxy_list:
    response = make_request(url, proxy)
    if response:
        print(f"successful request from {proxy}")
        break
    else:
        print(f"unsuccesful from {proxy}")

for proxy in proxy_list:
    response = make_request(url2, proxy)
    if response:
        print(f"successful request from {proxy}")
        break
    else:
        print(f"unsuccesful from {proxy}")
