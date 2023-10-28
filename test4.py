import subprocess
import winreg

def get_current_proxy_settings():
  

  reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_READ)

  proxy_enable = winreg.QueryValueEx(reg_key, 'ProxyEnable')[0]
  proxy_host = winreg.QueryValueEx(reg_key, 'ProxyServer')[0]

  winreg.CloseKey(reg_key)

  return proxy_enable, proxy_host

def set_proxy_settings(proxy_enable, proxy_host):


  reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_WRITE)

  winreg.SetValueEx(reg_key, 'ProxyEnable', 0, winreg.REG_DWORD, proxy_enable)
  winreg.SetValueEx(reg_key, 'ProxyServer', 0, winreg.REG_SZ, proxy_host)

  winreg.CloseKey(reg_key)

def activate_proxy_settings():


  subprocess.Popen(['netsh', 'winhttp', 'reset', 'proxy'])

# Get the current proxy settings.
#proxy_enable, proxy_host = get_current_proxy_settings()

# Set the new proxy settings.
set_proxy_settings(proxy_enable, '154.58.202.47:1337')

# Activate the proxy settings.
activate_proxy_settings()