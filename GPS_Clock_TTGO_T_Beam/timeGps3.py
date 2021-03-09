'''
(C) 2019 dk2jk
Gps -zeit lesen

11.2020 'timeGps3.py' fuer esp32 ttgo-beam
'timeGps2.py' fuer raspi
'''
import time
from machine import UART
from  machine import Pin,I2C
import ssd1306
from time import sleep

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
#i2c  = machine.I2C( scl=machine.Pin(PIN_CLOCK), sda=machine.Pin(PIN_DATA) )
oled = ssd1306.SSD1306_I2C( 128, 64, i2c, 0x3c )

class MyTimeGps:
    _c=""
    def __init__(self):
        try:
            self._ser = UART(2, tx=12, rx=34)
            self._ser.init(9600, bits=8, parity=None, stop=1)
        except:
            assert False,"*** error uart"
        print ("---Time (GPS)----")

    
    def read(self):
        while True:
            time.sleep(.01)
            try:
                c= self._ser.readline().decode()            
                s2= c.split(',')          
                if s2[0]=="$GPRMC":                
                    break
            except:
                # no data
                pass
        return s2
    
    def last_sentence(self):
        return self._c 

def settime():
    t = ntptime() +1* 3600 # winterzeit
    import machine
    import utime

    tm = localtime(t)
    machine.RTC().init((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

def rmc_to_localtime(rmc_time,rmc_date):
    print (rmc_time,rmc_date)  # 165002.00 090321
    dt= [2021, 3, 9, 16, 44, 22, 1, 68] # vorlage
    dt[0]=2000+int(rmc_date[4:6])
    dt[1]=int(rmc_date[2:4])
    dt[2]=int(rmc_date[0:2])
    dt[3]=int(rmc_time[0:2])
    dt[4]=int(rmc_time[2:4])
    dt[5]=int(rmc_time[4:6])
    dt[6]=int(rmc_time[7:9])
    dt[6]=0
    
    return dt

uhr = MyTimeGps()

def display_gps_time_utc():
    x=uhr.read()
    #print(x)
    #print("date= {} time= {}".format(x[9],x[1][0:6]  ) )
    """ x= ['$GPRMC', '162914.00', 'A', '5128.97807', 'N',
    '00819.32146', 'E', '1.666', '', '090321', '', '', 'A*7A\r\n']"""
    
    x=rmc_to_localtime(x[1],x[9])
    #assert False, ""
    #x=time.localtime()  #(2020, 11, 16, 10, 23, 0, 0, 321)
    #print( x)
    timeStr= "{:02d}:{:02d}:{:02d}".format( x[3],x[4],x[5])
    dateStr= "{:02d}.{:02d}.{:02d}".format( x[2],x[1],x[0])
    
    print(timeStr,dateStr)
    oled.text("GPS-Zeit [UTC]",10,11) #x,y
    oled.hline(0,22,127,1)
    oled.text(timeStr,20,33)
    oled.text(dateStr,20,48)
    oled.show()
    oled.fill(0)
    
if __name__ == '__main__':
    display_gps_time_utc()
 

