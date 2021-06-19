from datetime import datetime
from datetime import timedelta
from random import randint
import inquirer
from getpass import getpass

# unsere erstellte Liste fuer die Option von Beispielsaetzen
RANDOM_SENTENCE_WORDLIST = "/Users/yunusemre/PycharmProjects/pythonprojekt/masterpass/liste.txt"

# die Rockyou Datei mit den schlechtesten passwoertern
ROCKYOU = "/Users/yunusemre/PycharmProjects/pythonprojekt/masterpass/100k.txt"


# Ueberpruefen ob zweite eingabe beim bestimmen vom Mpw, gleich ist wie die erste
def check_second_mpw_input(passwort):
    zeitPunktAnfangMethode = datetime.now()
    pruefer = getpass("[?]Geben Sie ihr Passwort erneut ein")
    zeitPunktEndeMethode = datetime.now()
    zwischenZeit = timedelta.total_seconds(zeitPunktEndeMethode - zeitPunktAnfangMethode)
    if zwischenZeit <= 60:
        # if anweisung überprueft, ob laenger als 5 minuten nix eingegeben wurde
        if passwort == pruefer:
            print("[!] Akzeptiert")
            # passwortVerstauen(passwort)

        else:
            print("[!] Die Eingabe hat nicht übereingestimmt mit der zuvor, auf ein neues")
            set_password()
    else:
        print(str(zwischenZeit - 60) + "[!] Sekunden zu lange untätig")
        print("[!]Sie wurden rausgeworfen, da Sie zu lange untätig waren")
        set_password()


# ueberprueft die Laenge des Passwortes
def check_length_mpw_input(passwort):
    while passwort.__len__() < 7:
        print("[!] zu kurz")
        generate_random_sentence()
        passwort = getpass("")
    return passwort


# hier wird die Eingabe vom Nutzer mit dem gespeichertem Passwort verglichen
# wahrscheinlich nicht wichtig, da wir nicht viel mit textdateien arbeiten wollen
def mpw_input_program_start(decryptetPW):
    x = check_wrong_inputs_mpw_program_start()
    while x > 0:
        zeitPunktAnfangMethode = datetime.now()
        pwEingabe = getpass("[?]Geben sie ihr Passwort ein um fortzufahren " + str(x) + " Versuch/e verbleibend")
        zeitPunktEndeMethode = datetime.now()
        bPwEingabe = bytes(pwEingabe, "utf-8")
        zwischenZeit = timedelta.total_seconds(zeitPunktEndeMethode - zeitPunktAnfangMethode)
        if zwischenZeit < 200:
            if bPwEingabe == decryptetPW:
                print("[!] richtige Eingabe")
                with open('versucheBleibend.txt', 'w') as file:
                    x = 3
                    file.write(str(x))
            x = x - 1
            with open('versucheBleibend.txt', 'w') as file:
                file.write(str(x))
        else:
            print(zwischenZeit)
            print("[!] Programm geschlossen, zu lange untätig")
            return


# In Datei "versucheBleibend.txt" werden Restversuche gespeichert und abgelegt.
# wahrscheinlich nicht wichtig, da wir nicht viel mit textdateien arbeiten wollen
def check_wrong_inputs_mpw_program_start():
    try:
        with open('versucheBleibend.txt', 'r') as file:
            Z = file.read()
            x = int(Z)
            if x < 1:
                print("[!] Sie wurden gesperrt")

    except:
        x = 3
    return x


# hier wird die Datei "100k.txt->ROCKYOU" abgeglichen mit der Eingabe, falls fuendig wird ein True zurückgegeben
def is_in_rockyou(passwort):
    with open(ROCKYOU, "r") as fopen:
        fread = fopen.readlines()
        for line in fread:
            if passwort == line.strip():
                return True
        return False


# hier werden mithilfe der  Datei "liste.txt" drei Vorschlaege für den Nutzer gemacht für ein sicheres Passwort
def generate_random_sentence():
    print("WICHTIG! Schreiben sie für ein sicheres Passwort zunächst einmal einen unüblichen Satz auf ein Blatt "
          "Papier\nwie z.B einen dieser drei Sätze:")
    with open(RANDOM_SENTENCE_WORDLIST, 'r') as fopen:
        fread = fopen.readlines()
    data = []
    for line in fread:
        line = line.strip()
        data.append(line)
    zufallszahlSatzLaenge = randint(7, 12)
    for i in range(0, 3):
        s = ""
        for z in range(zufallszahlSatzLaenge):
            s = (s + data[randint(1, 1000)] + " ")
        print(s)
    print("\n[!] Falls Sie dies getan haben, sollten Sie nun einfach aus jedem Wort ein bis zwei Buchstaben\n"
          "für ihr Passwort aussuchen. Markieren Sie sich auf ihrer Notiz, die jeweiligen Buchstaben.\n")


# wird als erstes aufgerufen
def set_password():
    questions = [
        inquirer.List('Passwort',
                      message="[?] Möchten Sie Hilfe beim erstellen des Passworts",
                      choices=['JA', 'NEIN'],
                      ),
    ]
    answers = inquirer.prompt(questions)

    gegebeneAntwort = str(answers)
    if gegebeneAntwort.__contains__("JA"):
        generate_random_sentence()
    passwort = getpass("[?]Passwort eingeben(länger als 7 Zeichen)")

    if is_in_rockyou(passwort):
        print("[!]Befindet sich in der ROCKYOU Datei, somit nicht sicher genug")
        set_password()
    # möglicherweise nicht funktionsfähig, bei der methode bekomme ich Error, der nicht weg gehen will
    # bei Yunus funktioniert es allerdings

    check_length_mpw_input(passwort)
    check_second_mpw_input(passwort)


set_password()
