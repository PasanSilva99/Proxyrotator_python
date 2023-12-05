import os
import ctypes
import winreg

# Define your proxy server and port
proxy_server = '154.58.202.47'
proxy_port = '1337'

# Define the registry keys and values for HTTP and HTTPS proxy settings
http_proxy_key = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
https_proxy_key = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

# Function to set proxy settings
def set_proxy_settings(proxy_server, proxy_port):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, http_proxy_key, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'ProxyServer', 0, winreg.REG_SZ, proxy_server + ':' + proxy_port)
        winreg.SetValueEx(key, 'ProxyEnable', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, https_proxy_key, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'ProxyServer', 0, winreg.REG_SZ, proxy_server + ':' + proxy_port)
        winreg.SetValueEx(key, 'ProxyEnable', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)

        # Notify Windows to update proxy settings
        ctypes.windll.wininet.InternetSetOptionW(0, 39, 0, 0)
        print("Proxy settings updated successfully.")
    except Exception as e:
        print("Error setting proxy settings:", e)

# Function to disable proxy settings
def disable_proxy_settings():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, http_proxy_key, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, https_proxy_key, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)

        # Notify Windows to update proxy settings
        ctypes.windll.wininet.InternetSetOptionW(0, 39, 0, 0)
        print("Proxy settings disabled.")
    except Exception as e:
        print("Error disabling proxy settings:", e)

# Uncomment one of the following lines to set or disable proxy settings
set_proxy_settings(proxy_server, proxy_port)
#disable_proxy_settings()
