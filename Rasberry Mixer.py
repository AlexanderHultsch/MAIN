#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
from tkinter import *
import functools
import os
from PIL import Image, ImageTk

#------------------------------------------------------------------
def Pumpenbelegung_2_PumpenListe():

    PumpenbelegungOrginal = open("Pumpenbelegung.txt","r")
    PumpenListe= []
    PumpenListe = PumpenbelegungOrginal.read()
    PumpenListe = PumpenListe.split("\n")
    PumpenbelegungOrginal.close()

    return PumpenListe

#------------------------------------------------------------------
def Pumpenbelegung_Speichern(PumpenListe):

    PumpenbelegungNeu = open("Pumpenbelegung.txt","w")

    Index1 = 0

    while Index1 < len(PumpenListe):

        PumpenbelegungNeu.write(str(PumpenListe[Index1]))
        PumpenbelegungNeu.write("\n")
        Index1 = Index1 +1

    PumpenbelegungNeu.close()

#-----------------------------------------------------------------
def PumpenKonfiguration(PumpenNummer, PumpenListe):  

    PumpenListe = Pumpenbelegung_2_PumpenListe()

    NeuerInhalt = str(input("Neuer Inhalt? "))
    NeueLiter = str(input("Wie viele ml? "))
    NeueViskositaet = str(input("Neue Viskositaet? "))

    if PumpenNummer == 1:
        PumpenIndex = 0
    elif PumpenNummer == 2:
        PumpenIndex = 5
    elif PumpenNummer == 3:
        PumpenIndex = 10

    PumpenListe[PumpenIndex] = "Pumpe" + str(PumpenNummer)
    PumpenListe[PumpenIndex+1] = NeuerInhalt
    PumpenListe[PumpenIndex+2] = NeueLiter
    PumpenListe[PumpenIndex+3] = NeueViskositaet
    PumpenListe[(PumpenIndex+4)] = "----------"

    Pumpenbelegung_Speichern(PumpenListe)

    return PumpenListe  

#------------------------------------------------------------------
def Getraenkeliste_2_GetraenkeListe():

    GetraenkeListe = []
    Getraenke = open("Getraenkeliste.txt","r")
    GetraenkeListe = Getraenke.read()
    GetraenkeListe = GetraenkeListe.split("\n")
    Getraenke.close()
    return GetraenkeListe

#------------------------------------------------------------------
def Getraenkeliste_Speichern(GetraenkeListe):

        Getraenke = open("Getraenkeliste.txt","w")
        Index2 = 0
        while Index2 < len(GetraenkeListe):

            Getraenke.write(GetraenkeListe[Index2])
            GetraenkeListe[Index2]
            Getraenke.write("\n")
            Index2 = Index2 +1

        Getraenke.close()      
#------------------------------------------------------------------
def GetraenkeListeKonfigurieren():

    Fenster.iconify()
    GetraenkeListe_Anzeigen()

    NameGetraenk = str(input("Name des Getraenks? "))
    if NameGetraenk != "0":
        Getraenk_Hinzufuegen(NameGetraenk)

        if NameGetraenk == "0":
            Frage = 0

        Frage = int(input("Weiteres Getraenk hinzufuegen 1/0? "))       
        if Frage == 0:
            OptionTab.destroy()
            Fenster.lift()


def PumpenKonfiuration():

    Fenster.iconify()        

    PumpenNummer = int(input("Welche Pumpe soll konfiguriert werden? "))
    if PumpenNummer != 0:
        PumpenListe = Pumpenbelegung_2_PumpenListe()
        PumpenKonfiguration(PumpenNummer, PumpenListe)

        Frage = int(input("Weitere Pumpe Konfigurieren 1/0? "))  

        if Frage == 0:
            BackButton()
            
#----------------------------------------------------------------------
def Getraenk_Hinzufuegen(NameGetraenk):

    if NameGetraenk != "0":

        GetraenkeListe = Getraenkeliste_2_GetraenkeListe()

        Zutat1 = str(input("Zutat Eins: "))
        Menge1 = str(input("Menge Eins: "))

        Zutat2 = str(input("Zutat Zwei: "))
        if Zutat2 != "":
            Menge2 = str(input("Menge Zwei: "))

        if Zutat2 == "":

            Zutat2 = "-"
            Zutat3 = "-"
            Zutat4 = "-"
            Zutat5 = "-"
            Menge2 = "0"
            Menge3 = "0"
            Menge4 = "0"
            Menge5 = "0"


        else:
            Zutat3 =  str(input("Zutat Drei: ")) 
            if Zutat3 != "":
                Menge3 = str(input("Menge Drei: "))
            if Zutat3 == "":
                Zutat3 = "-"
                Zutat4 = "-"
                Zutat5 = "-"
                Menge3 = "0"
                Menge4 = "0"
                Menge5 = "0"

            else:
                Zutat4 =  str(input("Zutat Vier: "))
                if Zutat4 != "":
                    Menge4 = str(input("Menge Vier: "))
                if Zutat4 == "":
                    Zutat4 = "-"
                    Zutat5 = "-"
                    Menge4 = "0"
                    Menge5 = "0"

                else:
                    Zutat5 =  str(input("Zutat Fuenf: "))
                    if Zutat5 != "":
                        Menge5 = str(input("Menge Fuenf: "))
                    if Zutat5 == "":
                        Zutat5 = "-"
                        Menge5 = "0"

        GetraenkeListe.append(NameGetraenk)

        GetraenkeListe.append(Zutat1)
        GetraenkeListe.append(Menge1)
        GetraenkeListe.append(Zutat2)
        GetraenkeListe.append(Menge2)
        GetraenkeListe.append(Zutat3)
        GetraenkeListe.append(Menge3)
        GetraenkeListe.append(Zutat4)
        GetraenkeListe.append(Menge4)
        GetraenkeListe.append(Zutat5)
        GetraenkeListe.append(Menge5)

        GetraenkeListe.append("----------")

        print("Getraenk hinzugefuegt!")
        Getraenkeliste_Speichern(GetraenkeListe)
        return GetraenkeListe

#---------------------------------------------------------------------
def GetraenkeListe_Anzeigen():

    GetraenkeListe = Getraenkeliste_2_GetraenkeListe()
    Index3 = 0
    global GListe
    GListe = []

    while Index3 < len(GetraenkeListe):
        GListe.append(GetraenkeListe[Index3])
        Index3 = Index3 + 13

    return(GListe)

#---------------------------------------------------------------------
def Zutaten_4_Getraenk(Getraenkewunsch):

    GetraenkeListe =  Getraenkeliste_2_GetraenkeListe()

    GetraenkeNummer = GetraenkeListe.index(Getraenkewunsch)

    Zutaten4Pumpen = (GetraenkeListe[(GetraenkeNummer+1):(GetraenkeNummer+11)])

    return Zutaten4Pumpen

#---------------------------------------------------------------------
def Alle_Pumpen_fuer_Getraenk_finden(Getraenkewunsch):

        Zutaten4Pumpen = Zutaten_4_Getraenk(Getraenkewunsch)
        PumpenListe = Pumpenbelegung_2_PumpenListe()


        Index4 = 0
        PumpenanweisungKomplett = []

        while Index4 < len(Zutaten4Pumpen):    

            Zutat = Zutaten4Pumpen[Index4]

            if Zutat != "-":

                Pumpennummer = PumpenListe[((PumpenListe.index(Zutat))-1)]
                PumpenanweisungKomplett.append(Pumpennummer)

                Menge = Zutaten4Pumpen[(Index4 + 1)]
                PumpenanweisungKomplett.append(Menge)

                Viskositaet = PumpenListe[((PumpenListe.index(Zutat))+2)]
                PumpenanweisungKomplett.append(Viskositaet)

            Index4 = Index4 +2

        PumpenanweisungKomplett2txt(PumpenanweisungKomplett)
        return PumpenanweisungKomplett

#-------------------------------------------------------------------

def PumpenanweisungKomplett2txt(PumpenanweisungKomplett):

    txt = open("Pumpenanweisung.txt","w")
    Index1 = 0
    while Index1 < len(PumpenanweisungKomplett):

        txt.write(str(PumpenanweisungKomplett[Index1]))
        txt.write("\n")
        Index1 = Index1 +1
    txt.close()

#--------------------------------------------------------------------
#Fuellstand checken & ggf. updaten

def Fuellstand_Aktualisieren(PumpenanweisungKomplett, PumpenListe):

    IndexFuell1 = 0
    AnzahlLeer = 0
    
    while IndexFuell1 < len(PumpenanweisungKomplett):
        PumpeNr = PumpenanweisungKomplett[IndexFuell1]
        PumpenIndex_in_PumpenListe = PumpenListe.index(PumpeNr)

        Soll = float(PumpenanweisungKomplett[((IndexFuell1)+1)])
        Haben = float(PumpenListe[((PumpenIndex_in_PumpenListe)+2)])

        if (Haben - Soll) >= 0:
            NeuerFuellstand = Haben - Soll
            PumpenListe[((PumpenIndex_in_PumpenListe)+2)] = NeuerFuellstand


        elif (Haben - Soll) < 0:
            print("Zu wenig", PumpenListe[((PumpenIndex_in_PumpenListe)+1)])
            AnzahlLeer = AnzahlLeer +1
        
        IndexFuell1 = IndexFuell1 +3
    
        
    if AnzahlLeer ==0:
        Pumpenbelegung_Speichern(PumpenListe)
        
    return AnzahlLeer

#-------------------------------------------------------------------------
#ReinigungsLauf

def AllePumpenAnsteuern():

    PumpenanweisungKomplett = ["Pumpe1", 500, 1, "Pumpe2", 500, 1, "Pumpe3", 500, 1, "Pumpe4", 500, 1]
    Pi_Ansteuern(PumpenanweisungKomplett)

#------------------------------------------------------------------------
# Pi ansteuern

def Pi_Eingaenge_belegen():

    EingaengeBelegt = 1
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)

    #GPIO.setup(18,GPIO.OUT)
    #GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(20,GPIO.OUT)
    #GPIO.setup(21,GPIO.OUT)


#------------------------------------------------------------------------
# Pi ansteuern

def Pi_Ansteuern(PumpenanweisungKomplett):

    Pi_Eingaenge_belegen()

    os.popen('Pumpe1.py')
    #os.popen('Pumpe2.py')
    #os.popen('Pumpe3.py')
    #os.popen('Pumpe4.py')



#-------------------------------------------------------------------------
# Ausschank

def Ausschank(Getraenkewunsch):
    button.config(state = 'disabled')
    Zutaten_4_Getraenk(Getraenkewunsch)
    Alle_Pumpen_fuer_Getraenk_finden(Getraenkewunsch)
    PumpenanweisungKomplett = Alle_Pumpen_fuer_Getraenk_finden(Getraenkewunsch)
    PumpenListe = Pumpenbelegung_2_PumpenListe()
    print(Getraenkewunsch)
    print(PumpenanweisungKomplett)
    AnzahlLeer = Fuellstand_Aktualisieren(PumpenanweisungKomplett, PumpenListe)
    
    if AnzahlLeer == 0:
        Pi_Ansteuern(PumpenanweisungKomplett)
        Loading()
        
    elif AnzahlLeer != 0:
         #Fuellstandswarnung()
        print("Fehler Füllstand")
        #os.startfile('OLI-SKRIPT.py')

    button.config(state = 'normal')


#--------------------------------------------------------------------------
#---------------------------------------------------------------------------
#GUI


def SetUp():

        global ScreenWidth
        global ScreenHeight


        ScreenWidth = 800
        ScreenHeight = 480


def FensterSet(ScreenWidth, ScreenHeight):

    global Fenster
    Fenster = Tk()
    Fenster.title("CocktailMixer.py")
    Fenster.attributes("-topmost", 0)

    Fenster.geometry("{0}x{1}+0+0".format(ScreenWidth, ScreenHeight))


def ueberschrift():

    ueberschriftGroese = int(round((ScreenHeight * 0.05),0))

    BreiteX = ScreenWidth
    HoeheY = int(round((ScreenHeight*1.1),0))

    TopImage = Image.open("BackgroundTop.gif")
    TopImage = TopImage.resize((BreiteX, HoeheY), Image.ANTIALIAS)
    TopBild = ImageTk.PhotoImage(TopImage)

    Schriftart_Groesse = ("Arial", ueberschriftGroese, "bold")     
    Hoehe = round((ScreenHeight*0.08),0)
    ueberschrift = Canvas(Fenster, width=ScreenWidth, height=Hoehe, highlightthickness=0)

    ueberschrift.create_image(0, 0, image=TopBild, anchor=NW)
    ueberschrift.image = TopBild

    ueberschrift.create_text(ScreenWidth*0.5, round((ScreenHeight*0.04),0), justify=CENTER, text="CocktailMixer.py", font = Schriftart_Groesse, fill="White")

    ueberschrift.pack()       


def UnterFenster():

    GetraenkeAnzahl = len(GetraenkeListe_Anzeigen())

    UnterFenster = Canvas(Fenster, width= int(round((ScreenWidth * 0.9),0)), height=(GetraenkeAnzahl*30), highlightthickness=0)
    UnterFenster.pack_propagate(0) 
    UnterFenster.place(relx=0.05, rely=0.1)

    GetraenkeListe_Anzeigen()
    Max_Zeit = MaxZeit()

    def Funktion(item):
        Ausschank(item)

    for item in GListe:
        global button

        button = Button(UnterFenster,text=item, command=functools.partial(Funktion,item))
        button.pack(fill=X,pady=0)

def Hintergrund():

    Breite = ScreenWidth
    Hoehe = ScreenHeight

    image = Image.open("Background.gif")
    image = image.resize((Breite, Hoehe), Image.ANTIALIAS)
    Bild = ImageTk.PhotoImage(image)

    background_image=Bild
    background_label =Label(Fenster, image=background_image)
    background_label.image = Bild
    background_label.place(relx=0, rely=0, relheight=1)

def PumpenKonfiuration_OptionTabdestroy():
    OptionTab.destroy()
    PumpenKonfiuration()            

def GetraenkeListeKonfigurieren_OptionTabdestroy():
    OptionTab.destroy()
    GetraenkeListeKonfigurieren()

def Reinigungsprogramm():
    OptionTab.destroy()
    AllePumpenAnsteuern()

def BackButton():
    OptionTab.destroy()
    Fenster.lift()

def OptionTabFunction():

    global OptionTab
    OptionTab = Toplevel(Fenster)
    OptionTab.attributes("-topmost", 1)

    def PumpenKonfiuration_OptionTabdestroy():
        OptionTab.destroy()
        PumpenKonfiuration()            

    def GetraenkeListeKonfigurieren_OptionTabdestroy():
        OptionTab.destroy()
        GetraenkeListeKonfigurieren()

    def Reinigungsprogramm():
        OptionTab.destroy()
        AllePumpenAnsteuern()

    def BackButton():
        OptionTab.destroy()
        Fenster.lift()



    Optionen_Button1 = Button(OptionTab, text = "Pumpen konfigurieren", command =   PumpenKonfiuration_OptionTabdestroy)
    Optionen_Button1.pack()

    Optionen_Button2 = Button(OptionTab, text = "GetraenkeListe erweitern", command = GetraenkeListeKonfigurieren_OptionTabdestroy)
    Optionen_Button2.pack()

    Optionen_Button3 = Button(OptionTab, text = "Reinigungsprogramm", command = Reinigungsprogramm)
    Optionen_Button3.pack()

    Optionen_Button4 = Button(OptionTab, text = "Zurueck", command = BackButton)
    Optionen_Button4.pack()


def OptionenButton():

    B = int(round((ScreenWidth*0.075),0))
    H = int(round((ScreenHeight*0.125),0))

    image = Image.open("Settings.gif")
    image = image.resize((B, H), Image.ANTIALIAS)
    Bild = ImageTk.PhotoImage(image)

    OptionenButton = Button(Fenster,image = Bild, width= B, height= H, activebackground="black", bd=0, command = OptionTabFunction, highlightthickness=0)
    OptionenButton.image = Bild
    OptionenButton.place(relx=0.92, rely=0.87) 

            
def MaxZeit():
    PumpenListeZeit = []
    txtPumpe = open("Pumpenanweisung.txt","r")
    PumpenListeZeit = txtPumpe.read()
    PumpenListeZeit = PumpenListeZeit.split("\n")
    txtPumpe.close()
    ZeitListe = []
    IndexZeit = 1
    
    while IndexZeit < len(PumpenListeZeit):
        ZeitListe.append(PumpenListeZeit[IndexZeit])
        IndexZeit = IndexZeit +3
    Max_Time = (int(max(ZeitListe)) * 100)
    return Max_Time


def Loading():
    
    MaxDauer = MaxZeit()
    
    Br = ScreenWidth
    Hoe = ScreenHeight

    imageP = Image.open("Processing.gif")
    imageP = imageP.resize((Br, Hoe), Image.ANTIALIAS)
    BildP = ImageTk.PhotoImage(imageP)

    background_imageP = BildP
    background_label_P =Label(Fenster, image=background_imageP, highlightthickness=0)
    background_label_P.image = BildP
    background_label_P.place(relx=0, rely=0, relheight=1)

    LoadingFenster = Canvas(Fenster, width= ScreenWidth, height=ScreenHeight,  highlightthickness=0)

    frames = [PhotoImage(file='Loading.gif',format = 'gif -index %i' %(i)) for i in range(8)]     


    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == 8:
            ind = 0
        Flaeche.configure(image=frame)
        Flaeche.image = frame
        LoadingFenster.after(150, update, ind)

    def Close():
        LoadingFenster.destroy()
        background_label_P.destroy()

    Flaeche = Label(LoadingFenster)

    Flaeche.pack()  
    LoadingFenster.place(relx=0.2, rely=0.2)
    LoadingFenster.after(0, update, 0)
    LoadingFenster.after(MaxDauer, Close)

def Fuellstandswarnung():

    Breit = int(round((ScreenWidth*0.03),0))
    Hoch = Breit

    Warnbild = Image.open("Fuellstand.gif")
    Warnbild = Warnbild.resize((Breit, Hoch), Image.ANTIALIAS)
    WarnBild = ImageTk.PhotoImage(Warnbild)
    
    def CloseWarning():
        WarnLabel.destroy()
        PumpenKonfiuration() 
        
    WarnLabel = Button(Fenster, image=WarnBild, width= Breit, height= Hoch, activebackground="black", bd=0, command = CloseWarning, highlightthickness=0)
    WarnLabel.image = WarnBild

    WarnLabel.place(relx=0.95, rely=0.01)

#-----------------------------------

def TK_GUI():    

    SetUp()
    FensterSet(ScreenWidth, ScreenHeight) 
    Hintergrund()
    ueberschrift()       
    UnterFenster()    
    OptionenButton()  
    Fenster.mainloop()


#-------------------------------------------------------------------------
#Eigentliches Programm
TK_GUI()


# In[ ]:




