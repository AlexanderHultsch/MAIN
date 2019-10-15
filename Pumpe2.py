#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

Pumpenanweisung2 = []
txt2 = open("Pumpenanweisung.txt","r")
Pumpenanweisung1 = txt2.read()
Pumpenanweisung1 = Pumpenanweisung1.split("\n")
txt2.close()
print("Pumpe2")
print(Pumpenanweisung2)

Umrechungsfaktor = 0.1
Index2 = 0


while Index2 < len(Pumpenanweisung2):
    
    if Pumpenanweisung1[Index1] == "Pumpe2":
            ml = int(Pumpenanweisung2[(Index2+1)])
            Viskosität = int(Pumpenanweisung1[(Index2+2)])
            Pumpdauer = ml*Viskosität*Umrechungsfaktor
            print("Pumpe2 läuft ", Pumpdauer, "sek!")
            #GPIO.output(19, GPIO.HIGH)#
            time.sleep(Pumpdauer)
            print("Pumpe2 stop")
            #GPIO.output(19, GPIO.LOW)#
            
    Index2 = Index2 +1

    
time.sleep(5)
        

