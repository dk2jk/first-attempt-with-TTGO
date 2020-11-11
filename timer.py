# ************ timer.py ****************
#Timer esp32

import time

class Timer:
    def __init__(self, interval=1.0):
        self.start(interval)
        pass
    def event(self):
        now = time.ticks_ms()/1000  
        if now > self._overflow:
            self.restart(now)
            return True
        return False
        pass
    def restart(self,now):
        self._overflow = now+ self._interval
        pass
    def start(self,interval):
        self._interval= interval
        self._overflow =  time.ticks_ms()/1000 + self._interval
        pass
 
if  (__name__ == '__main__'):
    t1= Timer (0.5)

    while True:
        if t1.event():
            print ( time.time() )