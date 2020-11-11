# ************ display_sinus.py ****************

from  machine import Pin,I2C
import ssd1306
from time import sleep

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
#i2c  = machine.I2C( scl=machine.Pin(PIN_CLOCK), sda=machine.Pin(PIN_DATA) )
oled = ssd1306.SSD1306_I2C( 128, 64, i2c, 0x3c )

from math import pi, sin,cos


for grad in range ( 0,128):
    step= 6*pi/128
    y= 32+ 22*sin( grad*step)
    z= 32+ 31*cos( grad*step)
    oled.pixel(grad,int(y),1)
    oled.pixel(grad,int(z),1)
oled.text("Test von DK2JK",10,31)
oled.hline(0,44,127,1)
oled.show()


