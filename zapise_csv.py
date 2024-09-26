from main import *
import csv


with open("podatki.csv", "w", encoding="utf-8") as datoteka:
    writer = csv.writer(datoteka)
    writer.writerow(["Instrumenti", "Stil", "Opus", "Datum kompozicije", "Vir", "Avtorske pravice", "Zadnja posodobitev", "Glasbeni ID", "Typeset"])
    writer.writerow([instrumenti, stil, opus, datum_kompozicije, vir, avtorske_pravice, zadnja_posodobitev, glasbeni_ID, typeset])

