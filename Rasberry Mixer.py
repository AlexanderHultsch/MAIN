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
    NeueViskosität = str(input("Neue Viskosität? "))

    if PumpenNummer == 1:
        PumpenIndex = 0
    elif PumpenNummer == 2:
        PumpenIndex = 5
    elif PumpenNummer == 3:
        PumpenIndex = 10

    PumpenListe[PumpenIndex] = "Pumpe" + str(PumpenNummer)
    PumpenListe[PumpenIndex+1] = NeuerInhalt
    PumpenListe[PumpenIndex+2] = NeueLiter
    PumpenListe[PumpenIndex+3] = NeueViskosität
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
def GetränkeListeKonfigurieren():

    Fenster.iconify()
    GetraenkeListe_Anzeigen()

    NameGetränk = str(input("Name des Getränks? "))
    if NameGetränk != "0":
        Getränk_Hinzufügen(NameGetränk)

        if NameGetränk == "0":
            Frage = 0

        Frage = int(input("Weiteres Getränk hinzufügen 1/0? "))       
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
def Getränk_Hinzufügen(NameGetränk):

    if NameGetränk != "0":

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
                    Zutat5 =  str(input("Zutat Fünf: "))
                    if Zutat5 != "":
                        Menge5 = str(input("Menge Fünf: "))
                    if Zutat5 == "":
                        Zutat5 = "-"
                        Menge5 = "0"

        GetraenkeListe.append(NameGetränk)

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

        print("Getränk hinzugefügt!")
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
def Zutaten_4_Getraenk(Getränkewunsch):

    GetraenkeListe =  Getraenkeliste_2_GetraenkeListe()

    GetränkeNummer = GetraenkeListe.index(Getränkewunsch)

    Zutaten4Pumpen = (GetraenkeListe[(GetränkeNummer+1):(GetränkeNummer+11)])

    return Zutaten4Pumpen

#---------------------------------------------------------------------
def Alle_Pumpen_für_Getraenk_finden(Getränkewunsch):

        Zutaten4Pumpen = Zutaten_4_Getraenk(Getränkewunsch)
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

                Viskosität = PumpenListe[((PumpenListe.index(Zutat))+2)]
                PumpenanweisungKomplett.append(Viskosität)

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
#Füllstand checken & ggf. updaten

def Füllstand_Aktualisieren(PumpenanweisungKomplett, PumpenListe):

    IndexFüll1 = 0
    AnzahlLeer = 0
    
    while IndexFüll1 < len(PumpenanweisungKomplett):
        PumpeNr = PumpenanweisungKomplett[IndexFüll1]
        PumpenIndex_in_PumpenListe = PumpenListe.index(PumpeNr)

        Soll = float(PumpenanweisungKomplett[((IndexFüll1)+1)])
        Haben = float(PumpenListe[((PumpenIndex_in_PumpenListe)+2)])

        if (Haben - Soll) >= 0:
            NeuerFüllstand = Haben - Soll
            PumpenListe[((PumpenIndex_in_PumpenListe)+2)] = NeuerFüllstand


        elif (Haben - Soll) < 0:
            print("Zu wenig", PumpenListe[((PumpenIndex_in_PumpenListe)+1)])
            AnzahlLeer = AnzahlLeer +1
        
        IndexFüll1 = IndexFüll1 +3
    
        
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

def Pi_Eingänge_belegen():

    EingängeBelegt = 1
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)

    #GPIO.setup(18,GPIO.OUT)
    #GPIO.setup(19,GPIO.OUT)
    #GPIO.setup(20,GPIO.OUT)
    #GPIO.setup(21,GPIO.OUT)


#------------------------------------------------------------------------
# Pi ansteuern

def Pi_Ansteuern(PumpenanweisungKomplett):

    Pi_Eingänge_belegen()

    os.startfile('Pumpe1.py')
    #os.startfile('Pumpe2.py')
    #os.startfile('Pumpe3.py')
    #os.startfile('Pumpe4.py')



#-------------------------------------------------------------------------
# Ausschank

def Ausschank(Getränkewunsch):
    button.config(state = 'disabled')
    Zutaten_4_Getraenk(Getränkewunsch)
    Alle_Pumpen_für_Getraenk_finden(Getränkewunsch)
    PumpenanweisungKomplett = Alle_Pumpen_für_Getraenk_finden(Getränkewunsch)
    PumpenListe = Pumpenbelegung_2_PumpenListe()
    print(Getränkewunsch)
    print(PumpenanweisungKomplett)
    AnzahlLeer = Füllstand_Aktualisieren(PumpenanweisungKomplett, PumpenListe)
    
    if AnzahlLeer == 0:
        Pi_Ansteuern(PumpenanweisungKomplett)
        Loading()
        
    elif AnzahlLeer != 0:
         Füllstandswarnung()
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


def Überschrift():

    ÜberschriftGroese = int(round((ScreenHeight * 0.05),0))

    BreiteX = ScreenWidth
    HöheY = int(round((ScreenHeight*1.1),0))

    TopImage = Image.open("BackgroundTop.gif")
    TopImage = TopImage.resize((BreiteX, HöheY), Image.ANTIALIAS)
    TopBild = ImageTk.PhotoImage(TopImage)

    Schriftart_Größe = ("Arial", ÜberschriftGroese, "bold")     
    Höhe = round((ScreenHeight*0.08),0)
    Überschrift = Canvas(Fenster, width=ScreenWidth, height=Höhe, highlightthickness=0)

    Überschrift.create_image(0, 0, image=TopBild, anchor=NW)
    Überschrift.image = TopBild

    Überschrift.create_text(ScreenWidth*0.5, round((ScreenHeight*0.04),0), justify=CENTER, text="CocktailMixer.py", font = Schriftart_Größe, fill="White")

    Überschrift.pack()       


def UnterFenster():

    GetränkeAnzahl = len(GetraenkeListe_Anzeigen())

    UnterFenster = Canvas(Fenster, width= int(round((ScreenWidth * 0.9),0)), height=(GetränkeAnzahl*26), highlightthickness=0)
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
    Höhe = ScreenHeight

    image = Image.open("Background.gif")
    image = image.resize((Breite, Höhe), Image.ANTIALIAS)
    Bild = ImageTk.PhotoImage(image)

    background_image=Bild
    background_label =Label(Fenster, image=background_image)
    background_label.image = Bild
    background_label.place(relx=0, rely=0, relheight=1)

def OptionTabFunction():

    global OptionTab
    OptionTab = Toplevel(Fenster)
    OptionTab.attributes("-topmost", 1)

    def PumpenKonfiuration_OptionTabdestroy():
        OptionTab.destroy()
        PumpenKonfiuration()            

    def GetränkeListeKonfigurieren_OptionTabdestroy():
        OptionTab.destroy()
        GetränkeListeKonfigurieren()

    def Reinigungsprogramm():
        OptionTab.destroy()
        AllePumpenAnsteuern()

    def BackButton():
        OptionTab.destroy()
        Fenster.lift()



    Optionen_Button1 = Button(OptionTab, text = "Pumpen konfigurieren", command =   PumpenKonfiuration_OptionTabdestroy)
    Optionen_Button1.pack()

    Optionen_Button2 = Button(OptionTab, text = "GetränkeListe erweitern", command = GetränkeListeKonfigurieren_OptionTabdestroy)
    Optionen_Button2.pack()

    Optionen_Button3 = Button(OptionTab, text = "Reinigungsprogramm", command = Reinigungsprogramm)
    Optionen_Button3.pack()

    Optionen_Button4 = Button(OptionTab, text = "Zurück", command = BackButton)
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
    Hö = ScreenHeight

    imageP = Image.open("Processing.gif")
    imageP = imageP.resize((Br, Hö), Image.ANTIALIAS)
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
        Fläche.configure(image=frame)
        Fläche.image = frame
        LoadingFenster.after(150, update, ind)

    def Close():
        LoadingFenster.destroy()
        background_label_P.destroy()

    Fläche = Label(LoadingFenster)

    Fläche.pack()  
    LoadingFenster.place(relx=0.2, rely=0.2)
    LoadingFenster.after(0, update, 0)
    LoadingFenster.after(MaxDauer, Close)

def Füllstandswarnung():

    Breit = int(round((ScreenWidth*0.03),0))
    Hoch = Breit

    Warnbild = Image.open("Füllstand.gif")
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
    Überschrift()       
    UnterFenster()    
    OptionenButton()  
    Fenster.mainloop()


#-------------------------------------------------------------------------
#Eigentliches Programm
TK_GUI()


# In[ ]:




