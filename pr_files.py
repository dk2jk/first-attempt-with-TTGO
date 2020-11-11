# ************ pr_files.py ****************

# program zum kopieren der python dateien im flash nach sdkarte
# hardware: ttgo mit esp32 lora sdcard oled
# Nov. 2020 dk2jk

#wähle hardware
TTGO=True    # TTGO
# TTGO=False # windows
import os
liste= os.listdir()
#print (liste)


if TTGO:
    pass
else: #windows
    curdir= os.curdir
    print( curdir)   # '.'

# ziel bereitstellen ( in ttgo sd card via spi verbinden)
# bei ttgo sd mount sd card

if TTGO:
    from machine import SDCard
    filesystem= SDCard(slot=2, width=1, cd=None, wp=None, sck=14, miso=2, mosi=15, cs=13)
    os.mount(filesystem, '/sd')    #Will raise OSError(EPERM) if mount_point is already mounted.
    print("Filesystem check")
    print(os.listdir('/sd'))
else: # windows   
    # make zieldirectory, falls noch nicht vorhanden
    if os.path.isdir('./subdir'):
        pass
    else:
        os.mkdir("subdir")

# for files in quelle
for file in liste:
    if file[-3:]=='.py':
        print (file) # ok und weiter bei 'open'
    else:
        continue # keine '.py' datei, nächste datei in liste nehemen
      
    a= open( file,'r')  # file open in quelle read A
    if TTGO:
        b= open( '/sd/'+file,'w') # file open in zieldir write B
    else:
        b= open( 'subdir/'+file,'w') # file open in zieldir write B
    
    kopf= "# ************ {} ****************\n".format(file)
    b.write(kopf)  # titel
    # for zeilen in A
    while True:
    # read zeile n in A
        y= a.readline() # achtung : geht nur bei ASCII, zb. "xxx.py"
        if y=='':       # nichts mehr gelesen ?
            break
        print(y,end='') # zeigen wie gelesen
        b.write(y) # write zeile nach B 
        pass # next zeile
    # eine datei fertig
    # close A,B
    a.close()
    b.close()
    pass # nächste datei

# unmount sd karte
if TTGO:
    os.umount('/sd')
    filesystem.deinit()
    del filesystem

