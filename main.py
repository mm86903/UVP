import os                                
from bs4 import BeautifulSoup            #za razčlenjevanje html
import requests                          #za vsebino html
import csv






def razclenjevanje_html(vrstice):
    """Obdelava html vrstic in pridobitev podatkov"""
    data = {
        "instrumenti" : None,
        "stil" : None,
        "opus" : None,
        "datum_kompozicije" : None,
        "vir" : None,
        "avtorske_pravice" : None,
        "zadnja_posodobitev" : None,
        "glasbeni_ID" : None,
        "typeset" : None
    }

    for vrstica in vrstice:
        celice = vrstica.find_all("td")  #Znotraj "tr" imamo v vsakem dva "td"
        
        for celica in celice:
            if "Instrument(s):" in celica.text:
                data["instrumenti"] = celica.text.split(":")[1].strip()   #vzamemo prvi elemnt seznama in pobrisemo bele znake
            if "Style:" in celica.text:
                data["stil"] = celica.text.split(":")[1].strip()
            if "Opus:" in celica.text:
                data["opus"] = celica.text.split(":")[1].strip()
            if "Date of composition:" in celica.text:
                data["datum_kompozicije"] = celica.text.split(":")[1].strip()
            if "Source:" in celica.text:
                data["vir"] = celica.text.split(":")[1].strip()
            if "Copyright:" in celica.text:
                data["avtorske_pravice"] = celica.text.split(":")[1].strip()
            if "Last updated:" in celica.text:
                data["zadnja_posodobitev"] = celica.text.split(":")[1].strip().split(".")[0]     #odstranimo se "View change history"
            if "Music ID Number:" in celica.text:
                data["glasbeni_ID"] = celica.text.split(":")[1].strip()
            if "Typeset using:" in celica.text:
                data["typeset"] = celica.text.split(":")[1].strip()
            
    return data



def sparsa_skladbo(url, writer):
    page = requests.get(url)   #dobimo izvrono kodo
    soup = BeautifulSoup(page.text, "html.parser")            #Naredimo beautifulsoup objekt

    #Vsi podatki o določeni skladbi:
    vsi_podatki = soup.find("table", {"class":"table table-bordered result-table"})            #tabela podatkov
    vrstice = vsi_podatki.find_all("tr")                                                       #Vse vrstice v tabeli

    slovar = razclenjevanje_html(vrstice)
    ime_skladbe = "not_found"
    
    writer.writerow([ime_skladbe, slovar["instrumenti"], slovar["stil"], slovar["opus"], slovar["datum_kompozicije"], slovar["vir"], slovar["avtorske_pravice"], slovar["zadnja_posodobitev"], slovar["glasbeni_ID"], slovar["typeset"]])
 
 
def main():
    file = open("Podatki.csv", "w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["IME_SKLADBE","Instrumenti", "Stil", "Opus", "Datum kompozicije", "Vir", "Avtorske pravice", "Zadnja posodobitev", "Glasbeni ID", "Typeset"])
    #url = "https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2247"
    
    #sparsa_skladbo(url, writer)
    #url = "https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=439"
    #sparsa_skladbo(url, writer)
    
    glavni_url = "https://www.mutopiaproject.org/cgibin/make-table.cgi?Instrument=Piano"
    
main()
