import os
from bs4 import BeautifulSoup
import requests

url = "https://okusno.je/recept/kremna-juha-iz-hokaido-buce-1"
page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
zgornja = soup.find("div", {"class":"flex justify-between items-center w-full p-16 md:p-0 md:mx-64 lg:mx-100 text-12 md:text-14 text-secondary dark:text-white"})
#print(zgornja)

kuhanje = zgornja.find_all("div", {"class":"flex flex-col text-center"})[1]
print(kuhanje.text.split("\n")[1])