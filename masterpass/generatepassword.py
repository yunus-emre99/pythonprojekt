import random
import string
import inquirer


def _generate_password():
    laenge = int(input("Laenge: "))

    abfrage = [
        inquirer.Checkbox('Passwort',
                          message="Was soll ihr generiertes Passwort beeinhalten",
                          choices=['Kleinbuchstaben', 'Grossbuchstaben', 'Zahlen[0-9]', 'Zeichen'],
                          default=[]),
    ]

    answers = inquirer.prompt(abfrage)

    gegebeneAntworten = str(answers)

    inhalt = ''
    if gegebeneAntworten.__contains__("Kleinbuchstaben"):
        inhalt += string.ascii_lowercase
    if gegebeneAntworten.__contains__("Grossbuchstaben"):
        inhalt += string.ascii_uppercase
    if gegebeneAntworten.__contains__("Zahlen[0-9]"):
        inhalt += string.digits
    if gegebeneAntworten.__contains__("Zeichen"):
        inhalt += string.punctuation

    pw = ''.join(random.choice(inhalt) for i in range(laenge))


_generate_password()
