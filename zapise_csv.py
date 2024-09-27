from main import *
import csv

def zapisi_csv(slovar, datoteka)
    with open("podatki.csv", "w", encoding="utf-8") as datoteka:
        writer = csv.writer(datoteka)
        writer.writerow(["Instrumenti", "Stil", "Opus", "Datum kompozicije", "Vir", "Avtorske pravice", "Zadnja posodobitev", "Glasbeni ID", "Typeset"])
        writer.writerow(data["instrumenti"], data["stil"], data["opus"], data["datum_kompozicije"], data["vir"], data["avtorske_pravice"], data["zadnja_posodobitev"], data["glasbeni_ID, typeset"])

