# Bu proje "mrsemihkaba" tarafından yazılmıştır.
import requests
from bs4 import BeautifulSoup

url = "https://deprem.afad.gov.tr/last-earthquakes.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")
table_body = table.find("tbody")
rows = table_body.findAll("tr")

for row in rows:
    cols = row.findAll("td")
    tarih = cols[0].text.strip()
    enlem = cols[1].text.strip()
    boylam = cols[2].text.strip()
    derinlik = cols[3].text.strip()
    tip = cols[4].text.strip()
    buyukluk = cols[5].text.strip()
    yer = cols[6].text.strip()
    deprem_id = cols[7].text.strip()
    print(f"Tarih(TS): {tarih}\nEnlem: {enlem}\nBoylam: {boylam}\nDerinlik(Km): {derinlik}\nTip: {tip}\nBüyüklük: {buyukluk}\nYer: {yer}\nDeprem Id: {deprem_id}\n\n")
