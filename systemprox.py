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

def enable_proxy():
    try:
        key =  wreg.OpenKey(wreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0,wreg.KEY_WRITE)
        wreg.SetValue(key, "ProxyEnable", 0, wreg.REG_DWORD, 1)
        ctypes.windll.Wininet.InternetSetOPtionW(0, 81, 0, 0)

    except Exception as e:
        print("Error!!", e)

        