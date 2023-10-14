import os
import datetime

from colorama import Fore, Style, init

init()

#colors
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
r = Fore.LIGHTRED_EX
re = Fore.RESET

#styles
dim = Style.DIM
res = Style.RESET_ALL

def colored(type, text_colored, text_normal):
    output = ""

    if text_colored == "":
        space = ""
    else:
        space = " "

    if type == "normal":
        output = c + "[*] " + text_colored + space + re + text_normal 
    
    if type == "normal no star":
        output = c + text_colored + space + re + text_normal 

    elif type == "input":
        output = y + "[+] " + text_colored + space + re + text_normal 

    elif type == "error":
        output = r + "[!] " + text_colored + space + re + text_normal 

    return output

# Erstelle einen Ordner für das Tagebuch, wenn er nicht existiert
if not os.path.exists("tagebuch"):
    os.mkdir("tagebuch")


def tagebuch_schreiben():
    # Datum für den Eintrag erfassen
    datum = datetime.datetime.now()
    jahr = datum.year
    woche = datum.strftime("%U")  # Woche im Jahr
    tag = datum.strftime("%A")    # Wochentag
    day = datum.isoweekday()

    # Den Eintragstext eingeben
    eintrag = input(colored("input", "Tagebucheintrag eingeben: ", ""))

    # Den Eintrag in die entsprechende Datei schreiben oder erstellen
    datei_pfad = f"tagebuch/{jahr}/{woche}/{day}_{tag}.txt"

    if not os.path.exists(f"tagebuch/{jahr}/{woche}"):
        os.mkdir(f"tagebuch/{jahr}/{woche}")

    with open(datei_pfad, "a") as datei:
        datei.write(f"{datum.strftime('%Y-%m-%d %H:%M:%S')} | {eintrag}\n")
    print(colored("normal", "", "Eintrag wurde gespeichert."))


def tagebuch_anzeigen():
    print(c + "\nVerfügbare Tagebuchdateien\n" + re)
    jahr = datetime.datetime.now().year
    count = 0
    eintraege = []
    datum = datetime.datetime.now()
    woche = datum.strftime("%U")  # Woche im Jahr

    for verzeichnis_woche in os.listdir(f"tagebuch/{jahr}/"):
        if os.path.isdir(f"tagebuch/{jahr}/"):
            count += 1
            print(colored("normal no star", "["+str(count)+"]", verzeichnis_woche))
            eintraege.append(verzeichnis_woche)

    print("")

    auswahl = input(colored("input", "Bitte wählen:", ""))

    print("")

    woche = eintraege[int(auswahl) - 1]

    eintraege = []
    count = 0

    for verzeichnis in os.listdir(f"tagebuch/{jahr}/{woche}"):
        if os.path.isfile(f"tagebuch/{jahr}/{woche}/{verzeichnis}"):
            count += 1
            print(colored("normal no star", "["+str(count)+"]", verzeichnis))


def tagebuch_eintraege_anzeigen():
    jahr = datetime.datetime.now().year

    eintraege = []

    count = 0

    datum = datetime.datetime.now()
    woche = datum.strftime("%U")  # Woche im Jahr

    tag = datum.strftime("%A")    # Wochentag
    day = datum.isoweekday()


    print(c + "\nVerfügbare Tagebuchdateien\n" + re)

    for verzeichnis_woche in os.listdir(f"tagebuch/{jahr}/"):
        if os.path.isdir(f"tagebuch/{jahr}/"):
            count += 1
            print(colored("normal no star", "["+str(count)+"]", verzeichnis_woche))
            eintraege.append(verzeichnis_woche)

    print("")

    auswahl = input(colored("input", "Bitte wählen:", ""))

    print("")

    woche = eintraege[int(auswahl) - 1]

    eintraege = []
    count = 0

    for verzeichnis in os.listdir(f"tagebuch/{jahr}/{woche}"):
        if os.path.isfile(f"tagebuch/{jahr}/{woche}/{verzeichnis}"):
            count += 1
            print(colored("normal no star", "["+str(count)+"]", verzeichnis))
            eintraege.append(verzeichnis)

    print("")

    auswahl = input(colored("input", "Bitte wählen:", ""))

    datei = eintraege[int(auswahl) - 1]

    datei_pfad = f"tagebuch/{jahr}/{woche}/{datei}"

    print("")

    if os.path.exists(datei_pfad):
        with open(datei_pfad, "r") as datei:
            eintraege = datei.readlines()
            for i, eintrag in enumerate(eintraege, 1):
                print(dim + "{:02d}".format(i) + ". " + res + eintrag.strip())
    else:
        print(colored("error", "", f"{woche} wurde nicht gefunden."))


def tagebuch_eintrag_loeschen():
    jahr = datetime.datetime.now().year

    print(c + "\nVerfügbare Tagebuchdateien\n" + re)

    eintraege = []

    count = 0

    datum = datetime.datetime.now()
    woche = datum.strftime("%U")  # Woche im Jahr

    tag = datum.strftime("%A")    # Wochentag
    day = datum.isoweekday()

    for verzeichnis_woche in os.listdir(f"tagebuch/{jahr}/"):
        if os.path.isdir(f"tagebuch/{jahr}/"):
            count += 1
            print(colored("normal no star", "["+str(count)+"]", verzeichnis_woche))
            eintraege.append(verzeichnis_woche)

    print("")

    auswahl = input(colored("input", "Bitte wählen:", ""))

    print("")

    woche = eintraege[int(auswahl) - 1]

    eintraege = []
    count = 0

    for verzeichnis in os.listdir(f"tagebuch/{jahr}/{woche}"):
        if os.path.isfile(f"tagebuch/{jahr}/{woche}/{verzeichnis}"):
            count += 1
            print(colored("normal no star", "["+str(count)+"]", verzeichnis))
            eintraege.append(verzeichnis)

    print("")

    auswahl_datei = input(colored("input", "Bitte wählen:", ""))

    datei = eintraege[int(auswahl_datei) - 1]

    datei_pfad = f"tagebuch/{jahr}/{woche}/{datei}"

    print("")

    if os.path.exists(datei_pfad):
        with open(datei_pfad, "r") as datei:
            eintraege1 = datei.readlines()
            for i, eintrag in enumerate(eintraege1, 1):
                print(dim + "{:02d}".format(i) + ". " + res + eintrag.strip())
    else:
        print(colored("error", "", f"{woche} wurde nicht gefunden."))

    print("")

    nummer = int(input(colored("input", "Nummer eingeben:", "")))

    if os.path.exists(datei_pfad):
        with open(datei_pfad, "r") as datei:
            eintraege = datei.readlines()
        
        if 1 <= nummer <= len(eintraege):
            del eintraege[2 * (nummer - 1):2 * nummer]
            
            with open(datei_pfad, "w") as datei:
                datei.writelines(eintraege)
            
            print(colored("normal", "", f"Eintrag {nummer} wurde gelöscht."))
        
        else:
            print(colored("error", "", "Ungültige Eintragsnummer."))
    
    else:
        print(colored("error", "", f"{woche} wurde nicht gefunden."))


def main():
    while True:
        print(c + "\nTagebuch-CLI" + re)
        
        print("")
        
        print(colored("normal no star", "[1]", "Tagebuch schreiben"))
        print(colored("normal no star", "[2]", "Tagebuch anzeigen"))
        print(colored("normal no star", "[3]", "Einträge in der Woche anzeigen"))
        print(colored("normal no star", "[4]", "Eintrag löschen"))
        print(colored("normal no star", "[5]", "Beenden"))
        
        print("")
        
        auswahl = input(colored("input", ">", ""))

        if auswahl == "1":
            tagebuch_schreiben()
        
        elif auswahl == "2":
            tagebuch_anzeigen()
        
        elif auswahl == "3":
            tagebuch_eintraege_anzeigen()
        
        elif auswahl == "4":            
            tagebuch_eintrag_loeschen()
        
        elif auswahl == "5":
            print("")
            print(colored("error", "", "Programm beendet!"))
            print("")
            break
        
        else:
            print("")
            print(colored("error", "", "Ungültige Auswahl. Bitte wählen Sie erneut."))


if __name__ == "__main__":
    main()
