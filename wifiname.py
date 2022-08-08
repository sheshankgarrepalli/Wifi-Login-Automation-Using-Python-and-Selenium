import subprocess
import os 

wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
data = wifi.decode('utf-8')

# replace Bingbing@2.4G and Bingbing@5G with your wifi ssid names. 
if "Bingbing@2.4G" or "Bingbing@5G" in data:
    os.system('web.py')
    print("Successfully logged in")
else:
    print("not connected")


