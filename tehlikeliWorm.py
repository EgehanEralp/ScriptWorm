from sys import argv
import time
import os
import shutil
"""

Olduğu dizine 4 adet dosya açıp içerisine kendini kopyalıyor
startupta başlatma eklenebilir fakat test etmek istemedik

"""
script = argv
name = str(script[0])
print(name)
i=0

while True:
    directoryName = "kopya"+str(i)
    os.mkdir(directoryName)
    shutil.copy(name, directoryName)
    i+=1
    time.sleep(5)
    if i==4:
        break