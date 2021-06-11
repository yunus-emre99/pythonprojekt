import random
import string
import pyperclip
import getpass

random.random()
###################################

inhalt = ''
tester1=0;
tester2=0;
tester3=0;
tester4=0;

#ABFRAGE/INHALT PASSWORT
laenge = int(input("Laenge: "))
klein = input("Kleinbuchstabe (j/n): ")
gross = input("Grossbuchstaben (j/n): ")
zahl = input("Zahlen (j/n): ")
zeichen = input("Sonderzeichen (j/n): ")



#SICHERHEITSLEVEL DES PASSWORTS

if klein == 'j':
    inhalt += string.ascii_lowercase
    tester1=1;
if gross == 'j':
    inhalt += string.ascii_uppercase
    tester2=1;
if zahl == 'j':
    inhalt += '0123456789'
    tester3=1;
if zeichen == 'j':
    inhalt += string.punctuation
    tester4=1;

    alle_Tester=tester1+tester2+tester3+tester4
    print("Sicherheitslevel "+str(alle_Tester))


#GENERIERUNG DES PASSWORTS:
pw= ''.join(random.choice(inhalt) for i in range(laenge))
print("Ihr sicheres Passwort lautet:", pw)

#wischenablage Kopieren
pyperclip.copy(pw)


