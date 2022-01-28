import esp
try:
  import usocket as socket
except:
  import socket

import network
import machine

esp.osdebug(None)

import gc
gc.collect()


M1 = machine.Pin(12, machine.Pin.OUT)
M2 = machine.Pin(13, machine.Pin.OUT)
M3 = machine.Pin(16, machine.Pin.OUT)
M4 = machine.Pin(14, machine.Pin.OUT)
parking = machine.Pin(4, machine.Pin.OUT)
horn = machine.Pin(5, machine.Pin.OUT)
led = machine.Pin(2, machine.Pin.OUT)
led.value(1)
ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
#   print('Content = %s' % str(request))
  data = str(request)
#   print(data)
  res = data.split()
  res = res[1]
  print(res)
  if res == "/?State=F":
      led.value(0)
      M1.value(0)
      M2.value(1)
      M3.value(0)
      M4.value(1)
  if res == "/?State=B":
      led.value(0)
      M1.value(1)
      M2.value(0)
      M3.value(1)
      M4.value(0)
      
  if res == "/?State=L":
      led.value(0)
      M1.value(1)
      M2.value(1)
      M3.value(1)
      M4.value(0)
      
  if res == "/?State=R":
      led.value(0)
      M1.value(0)
      M2.value(1)
      M3.value(1)
      M4.value(1)
      
  if res == "/?State=S":
      led.value(1)
      M1.value(1)
      M2.value(1)
      M3.value(1)
      M4.value(1)
      
      
  conn.close()