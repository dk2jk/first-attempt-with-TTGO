# ************ ntp_time.py ****************
import time
import ntp as ntp
from timer import Timer
from machine import RTC,Pin,I2C
import ssd1306

class display:
    def __init__(self):
        i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
        self.oled = ssd1306.SSD1306_I2C( 128, 64, i2c, 0x3c )
        self.oled.text("  time (MEZ) ", 5,0,1)
        self.oled.show()
    def time(self, hms, x= 20,y=20):
        s= "{:02}:{:02}:{:02}".format(hms[0], hms[1],hms[2])      
        self.oled.fill_rect(x,y,128,28,0)
        self.oled.text(s, x,y,1)
        print(s)
        self.oled.show()

def meineUhr():
    d= display()
    t1=Timer(1) # 1 sekunde
    ntp.settime()  # RTC laeuft nun selbststaendig
    print( time.localtime())  # (2020, 11, 8, 10, 18, 5, 6, 313)
    hms=time.localtime()[3:6]  # (h,m,s)
    d.time(hms)
    print(hms)  # (10, 18, 5)

    while True:
        if t1.event():
            if time.localtime()[5] == 00:
                ntp.settime()
                print('x')
            t=time.localtime()
            hms= time.localtime()[3:6] 
            d.time(hms)
            
            
if __name__ == '__main__':
    meineUhr()
    