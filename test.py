import requests

proxies = {
    'https': "https//52.1583.8.192:3128"
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)