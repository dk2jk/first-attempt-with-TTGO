# ************ connect.py ****************
# uPython connect.py

import network
from time import sleep
ssid="nichts ist geheim"
sta_if = network.WLAN(network.STA_IF)

def wlan_ein():   
    if sta_if.isconnected():
        sta_if.active(False)
        #sta_if.disconnect()
    sta_if.active(True)
    sta_if.connect(ssid, "kabelloseverbindung-2") # 
        
    sleep(.5)
    return sta_if.isconnected()

def run_wlan():
    for i in range(0,10):
        x=wlan_ein()
        print("wlan",x)
        if x: break
        
if __name__ =='__main__':
    run_wlan()
