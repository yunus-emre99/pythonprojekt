# Passwort initial wählbar
# Vllt große textdatei mit beispiel wörtern als Vorgabe
# # # Passwort muss änderbar sein
# # # Passwort soll beim eingeben nicht im Klartext erscheinen (.getpass
# # # (WICHTIG): Passwort wird in einer Textdatei abgelegt, beim starten des Programmes wird geschaut ob sich etwas in dieser Textdatei befindet
# # # Passwort sollte verschlüsselt werden
# # # sinnvolle Zeitspanne für erneute Abfrage vom Passwort
import os
from datetime import datetime
from datetime import timedelta
from random import randint

import maskpass
from cryptography.fernet import Fernet


def ueberpruefeGleichheit(passwort):
    zeitPunktAnfangMethode=datetime.now()
    pruefer = maskpass.advpass("Geben sie ihr passwort erneut ein")
    zeitPunktEndeMethode=datetime.now()
    zwischenZeit=timedelta.total_seconds(zeitPunktEndeMethode-zeitPunktAnfangMethode)
    if(zwischenZeit<300):
## if anweisung überprüft, ob länger als 5 minuten nix eingegeben wurde
        if (passwort == pruefer):
            print("akzeptiert")
            passwortVerstauen(passwort)

        elif (passwort!= pruefer):
            print("Die Eingabe hat nicht übereingestimmt mit der zuvor, auf ein neues")
            passwortBestimmen()
    else:
        print(str(300-(zwischenZeit/60))+"min zu lange untätig")
        print("sie wurden rausgeworfen, da sie zu lange untätig waren")
        passwortBestimmen()


def passwortVerstauen(passwort):
    key = Fernet.generate_key()
    crypter = Fernet(key)
    with open('key.txt', 'wb') as file:

        file.write(key)

    bPW = bytes(passwort, 'utf8')
    with open('passwort.txt', 'wb') as file:
        file.write(crypter.encrypt(bPW))

def ueberpruefePasswortLaenge(passwort):
    while passwort.__len__() < 7:
        print("zu kurz!")
        satzZufälligGebildet()
        passwort = maskpass.advpass("")
    return passwort

### überpürft ob es bereits ein Passwort gibt(es wird geschaut nach "passwort.txt" und "key.txt)
def pruefExistPassW():
    tester=False
    try:
        f=open('key.txt')
        t1=open('passwort.txt')

        tester=True
    except Exception:
        print("Noch kein Passwort erstellt")
    if tester==True:
        pwEinlesenVonTextData()
    elif tester==False:
        passwortBestimmen()
        
        

def pwEinlesenVonTextData():
    print("Es gibt bereits ein Passwort")
    #pwEingabe = maskpass.advpass("Geben sie ihr Passwort ein um fortzufahren")
    #bPwEingabe=bytes(pwEingabe,"utf-8")

    with open('key.txt', 'rb') as file:
        key = file.read()
        crypter = Fernet(key)

    with open('passwort.txt', 'rb') as file:
        pw = file.read()
        decryptetPW = crypter.decrypt(pw)
    '''if (decryptetPW==bPwEingabe):
        print("richtige Eingabe")
        menuFuerPwOptionen()'''
    pwEingabeBeiProgrammStart(decryptetPW)

#hier wird die Eingabe vom Nutzer mit dem gespeichertem Passwort verglichen
def pwEingabeBeiProgrammStart(decryptetPW):
    x = pruefeAnzahlVersucheMasterPassW()
    while x > 0:
        zeitPunktAnfangMethode=datetime.now()
        pwEingabe = maskpass.advpass("Geben sie ihr Passwort ein um fortzufahren " + str(x) + " Versuch/e verbleibend")
        zeitPunktEndeMethode=datetime.now()
        bPwEingabe = bytes(pwEingabe, "utf-8")
        zwischenZeit=timedelta.total_seconds(zeitPunktEndeMethode-zeitPunktAnfangMethode)
        if(zwischenZeit<200):
            if (bPwEingabe == decryptetPW):
                print("richtige Eingabe")
                with open('versucheBleibend.txt', 'w') as file:
                    x=3
                    file.write(str(x))
                menuFuerPwOptionen()
                #x = 0
            x = x - 1
            with open('versucheBleibend.txt', 'w') as file:
                file.write(str(x))
        else:
            print(zwischenZeit)
            print("programm geschlossen, zu lange untätig")
            return

#In Datei "versucheBleibend.txt" werden Restversuche gespeichert und abgelegt.
def pruefeAnzahlVersucheMasterPassW():
    try:
        with open('versucheBleibend.txt', 'r') as file:
            Z = file.read()
            x = int(Z)
            if (x < 1):
                print("sie wurden gesperrt")

    except:
        x = 3
    return x


def menuFuerPwOptionen():
    optionen = maskpass.advpass("Falls sie ihr passwort anzeigen wollen, drücken sie die 1\n"
                                "Falls sie ihr passwort ändern wollen, drücken sie die 2\n"
                                "Falls sie das programm beenden wollen, drücken sie die 3\n"
                                )

    # Option 1 noch nicht gemacht. 
    if(optionen=='2'):
        fileKey = r"C:\Users\Arvand\PycharmProjects\Uni1\tester\key.txt"
        filePassW=r"C:\Users\Arvand\PycharmProjects\Uni1\tester\passwort.txt"
        ##os.remove(fileKey)
        ##os.remove(filePassW)
        passwortBestimmen()
    elif(optionen=='3'):
        print("Programm beendet")
        exit()

#hier wird die Datei "100k.txt" abgeglichen mit der Eingabe, falls fündig wird ein True zurückgegeben 
def sicherheitsTest(passwort):
    fopen= open('100k.txt', 'r')
    fread= fopen.readlines()

    pwTest=True
    while(pwTest==True):
        pw= str(passwort)
        pw.lower()
        for line in fread:

            if pw in line:
                return True
                break
        pwTest=False
    return False


#hier werden mithilfe der  Datei "liste.txt" drei Vorschläge für den Nutzer gemacht für ein sicheres Passwort
def satzZufälligGebildet():
    print("Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
          "WICHTIG! Schreiben sie für ein sicheres Passwort zunächst einmal einen unüblichen Satz auf ein Blatt Papier, wie Z.B:")
    zufallszahl=randint(1,93)
    fopen= open('liste.txt', 'r')
    fread=fopen.readlines()
    data=[]
    for line in fread:
        line=line.strip()
        data.append(line)
    #s=""
    zufallszahlSatzLaenge=randint(7,12)
    for i in range(0,3):
        s=""
        for z in range(zufallszahlSatzLaenge):
            s=(s + data[randint(1,1000)]+" ")
        print(s)
    print("\nFalls sie dies getan haben, sollten sie nun einfach aus jedem Wort ein bis zwei buchstaben\n"
          "für ihr passwort aussuchen. Markieren sie sich auf ihrer Notiz die jeweiligen Buchstaben\n"
          "und achten sie dabei, mindestens 8 Zeichen zu haben.")

def passwortBestimmen():
    #dummePWdaTa()
    satzZufälligGebildet()
    passwort = maskpass.advpass("")

    '''if sicherheitsTest(passwort):
        print("Nicht sicher genug,anderes Passwort wählen!")
        passwortBestimmen()'''
    ueberpruefePasswortLaenge(passwort)
    #sicherheitsTest(passwort)
    ueberpruefeGleichheit(passwort)
    # passwortaendern(passwort)

pruefExistPassW()






