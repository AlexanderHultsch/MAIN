#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

Pumpenanweisung1 = []
txt1 = open("Pumpenanweisung.txt","r")
Pumpenanweisung1 = txt1.read()
Pumpenanweisung1 = Pumpenanweisung1.split("\n")
txt1.close()
print("Pumpe1")
print(Pumpenanweisung1)

Umrechungsfaktor = 0.1
Index1 = 0


while Index1 < len(Pumpenanweisung1):
    
    if Pumpenanweisung1[Index1] == "Pumpe1":
            ml = int(Pumpenanweisung1[(Index1+1)])
            Viskosität = int(Pumpenanweisung1[(Index1+2)])
            Pumpdauer = ml*Viskosität*Umrechungsfaktor
            print("Pumpe1 läuft ", Pumpdauer, "sek!")
            #GPIO.output(18, GPIO.HIGH)#
            time.sleep(Pumpdauer)
            print("Pumpe1 stop")
            #GPIO.output(18, GPIO.LOW)#
            
    Index1 = Index1 +1

time.sleep(5)
        

