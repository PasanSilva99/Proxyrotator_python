import os
import ctypes
import winreg as wreg

#Disabling proxy

def disable_proxy():
    try:
        key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0,wreg.KEY_WRITE)
        wreg.SetValueEx(key, "ProxyEnable", 0, wreg.REG_DWORD, 0)
        wreg.CloseKey(key)
        ctypes.windll.Wininet.InternetSetOptionW(0, 81, 0, 0)
    except Exception as e:
        print("Error!!", e)

#enabling proxy
def enable_proxy():
    try:
        key =  wreg.OpenKey(wreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0,wreg.KEY_WRITE)
        wreg.SetValue(key, "ProxyEnable", 0, wreg.REG_DWORD, 1)
        ctypes.windll.Wininet.InternetSetOPtionW(0, 81, 0, 0)

    except Exception as e:
        print("Error!!", e)

#rotating the enabling and disabling functions for proxies to be applied
def rotate_proxy_settings():
    is_proxy_enabled = check_proxy_enabled()
    if is_proxy_enabled:
        disable_proxy()
        print("Proxy Settings Disabled")
    else:
        enable_proxy()
        print("Proxy Settings enabled")


#checking whether proxy settings are enabled
def check_proxy_enabled():
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0,wreg.KEY_WRITE)
    proxy_enable, _= wreg.QueryValueEx(key, "ProxyEnable")
    wreg.CloseKey(key)
    return proxy_enable == 1

if __name__ == "__main__":
    rotate_proxy_settings()