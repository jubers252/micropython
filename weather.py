
import urequests as requests
import json
from machine import Pin, SoftI2C
import ssd1306
import connectwifi
import time

connectwifi.connect()

i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
api_key = "0fcc6376f6248315ba10de40892af002"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "Pune"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
while True:
    if x["cod"] != "404":

        y = x["main"]

        current_temperature = (y["temp"]-273.15)

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]
            
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

    else:
        print(" City Not Found ")
    oled.fill(0)
    oled.text("City ="+city_name,0,11)
    oled.text("Temp =.{:.2f} C".format(current_temperature),0,22)
    oled.text("Pressure ="+str(current_pressure)+"hpa",0,33)
    oled.text("Humidity ="+str(current_humidity)+"%",0,44)
    oled.text("Desc.="+str(weather_description),0,55)
    oled.show()
    time.sleep(0.5)
