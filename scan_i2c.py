# ************ scan_i2c.py ****************
from machine import Pin,I2C
import ssd1306

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

print('Scan I2C bus for connected deivices')

devices = i2c.scan()

print('{} device(s) are connected to I2C bus\n'.format(len(devices)))

for device in devices:
    # print(device)
    print('Found device w/ address 0x{0:2X}'.format(device))
print() 


