import os
import winreg
import requests

proxy_server = "154.58.202.47"
proxy_port = "1337"


def set_proxy_settings():
    try:
        # Open the Internet Settings key in the Windows Registry
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_WRITE)

        # Set the proxy server and port for HTTP and HTTPS
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, f"{proxy_server}:{proxy_port}")
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)

        # Notify Internet Explorer settings change
        os.system('rundll32.exe' ' url.dll,FileProtocolHandler' ' "file://"%LocalAppData%\Microsoft\Windows\INetCache\IE\cvw864E6\content.htm""')

        print("Proxy settings changed successfully.")
       
    except Exception as e:
        print("Error: ", str(e))

# Reset proxy settings
def reset_proxy_settings():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)

        print("Proxy settings reset successfully.")
    except Exception as e:
        print("Error: ", str(e))


set_proxy_settings()  # Uncomment to set proxy settings
#reset_proxy_settings()  # Uncomment to reset proxy settings
