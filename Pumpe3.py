#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

Pumpenanweisung3 = []
txt3 = open("Pumpenanweisung.txt","r")
Pumpenanweisung3 = txt3.read()
Pumpenanweisung3 = Pumpenanweisung3.split("\n")
txt3.close()
print("Pumpe3")
print(Pumpenanweisung3)

Umrechungsfaktor = 0.1
Index3 = 0


while Index3 < len(Pumpenanweisung3):
    
    if Pumpenanweisung3[Index3] == "Pumpe3":
            ml = int(Pumpenanweisung1[(Index3+1)])
            Viskosität = int(Pumpenanweisung3[(Index3+2)])
            Pumpdauer = ml*Viskosität*Umrechungsfaktor
            print("Pumpe3 läuft ", Pumpdauer, "sek!")
            #GPIO.output(20, GPIO.HIGH)#
            time.sleep(Pumpdauer)
            print("Pumpe3 stop")
            #GPIO.output(29, GPIO.LOW)#
            
    Index3 = Index3 +1

time.sleep(5)       

