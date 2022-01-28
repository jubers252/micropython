import network, urequests, utime, machine
from machine import RTC, I2C, Pin
from ssd1306 import SSD1306_I2C
try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

ssid = 'JioFi3'
password = 'Sofi@31193'

api_key = "287866ccd73a43669b6d986d63155b0a"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

ip =station.ifconfig()
print(ip)

url = "https://timezone.abstractapi.com/v1/current_time/?api_key="+api_key+"&location=India, Pune"

response = urequests.get(url)
if response.status_code == 200: # query success
    print(response.text)
    parsed = response.json()
    datetime_str = str(parsed["datetime"])
    
    print(datetime_str)