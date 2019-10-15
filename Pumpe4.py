#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

Pumpenanweisung4 = []
txt4 = open("Pumpenanweisung.txt","r")
Pumpenanweisung4 = txt4.read()
Pumpenanweisung4 = Pumpenanweisung4.split("\n")
txt4.close()
print("Pumpe4")
print(Pumpenanweisung4)

Umrechungsfaktor = 0.1
Index4 = 0


while Index4 < len(Pumpenanweisung4):
    
    if Pumpenanweisung4[Index4] == "Pumpe4":
            ml = int(Pumpenanweisung4[(Index4+1)])
            Viskosität = int(Pumpenanweisung4[(Index4+2)])
            Pumpdauer = ml*Viskosität*Umrechungsfaktor
            print("Pumpe4 läuft ", Pumpdauer, "sek!")
            #GPIO.output(21, GPIO.HIGH)#
            time.sleep(Pumpdauer)
            print("Pumpe4 stop")
            #GPIO.output(21, GPIO.LOW)#
            
    Index4 = Index4 +1

time.sleep(5)
        

