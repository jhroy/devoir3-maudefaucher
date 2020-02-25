# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

fichier = "vege.csv"

entetes = {
    "User-Agent":"Maude Faucher, étudiante en journalisme à l'UQAM"
}
# Je vais essayer de moissoner, dans les pages de recettes de plats végétariens de la page de Ricardo, les plats qui contiennent le mot "tofu" dans le titre. 

urlp1 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/1"
# Mon url est celui de la page 1 parce que je vais devoir moissoner les données sur 11 pages. Il va donc falloir que je travaille avec un url différent à chaque fois. Je commence donc par la page 1. 
site = requests.get(urlp1, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

n=0
liste = []
for plat in plats:
    # print(plat.find("a")["href"])
    urlplat1 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat1)
    n+=1
    # print(n, urlplat1)
    # Je ne me souvenais plus comment simplement ajouter des éléments, alors j'ai triché un peu avec .replace mais ça fonctionne !
    # Pour chacune de mes pages (il y en a 11), je vais sortir le titre des 20 recettes affichées sur la page. 
    # Il y a certainement une manière plus efficace de faire, mais je ne la connais pas ou bien je n'arrive pas à l'imaginer !
    # Désolée pour ce script éternellement long ! 

# numeros = list(range (1, 12))
# for numero in numeros:
    # urlpages = url + str(numero)
    # print("."*10)
    # print(urlpages)
    # print("."*10)
    # J'ai réussi à générer 11 url fonctionnels qui amènent aux pages de plats végés de la page de Ricardo !
    # Ce qui m'a amené à changer mon url de base ! 

# urlp1 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/1"
# urlp2 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# urlp3 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/3"
# urlp4 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/4"
# urlp5 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/5"
# urlp6 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/6"
# urlp7 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/7"
# urlp8 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/8"
# urlp9 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/9"
# urlp10 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/10"
# urlp11 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/11"

urlp2 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
site = requests.get(urlp2, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")
# Pour chaque page, je change le chiffre de la fin de l'url (qui mène à la bonne page sur le site), l'url de requests.get, l'urlplatX et le print. 

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat2 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat2)
    n+=1
    # print(n, urlplat2)

urlp3 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/3"
site = requests.get(urlp3, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat3 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat3)
    n+=1
    # print(n, urlplat3)

urlp4 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/4"
site = requests.get(urlp4, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat4 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat4)
    n+=1
    # print(n, urlplat4)

urlp5 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/5"
site = requests.get(urlp5, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat5 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat5)
    n+=1
    # print(n, urlplat5)

urlp6 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/6"
site = requests.get(urlp6, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat6 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat6)
    n+=1
    # print(n, urlplat6)

urlp7 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/7"
site = requests.get(urlp7, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat7 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat7)
    n+=1
    # print(n, urlplat7)

urlp8 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/8"
site = requests.get(urlp8, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat8 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat8)
    n+=1
    # print(n, urlplat8)

urlp9 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/9"
site = requests.get(urlp9, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat9 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat9)
    n+=1
    # print(n, urlplat9)

urlp10 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/10"
site = requests.get(urlp10, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat10 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat10)
    n+=1
    # print(n, urlplat10)

urlp11 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/11"
site = requests.get(urlp11, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat11 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    liste.append(urlplat11)
    n+=1
    # print(n, urlplat11)

liste.append("")
liste.append("TOFUTOFUTOFUTOFUTOFUTOFUTOFUTOFUTOFUTOFU")
liste.append("")

# Maintenant que j'ai toutes les recettes classées dans "Plats végétariens" du site de Ricardo, je vais moissoner tout ceux qui contiennent le mot "tofu" (avec un t majuscule ou minuscule) dans le titre.

urlp1 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/1"
site = requests.get(urlp1, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

# Ici, j'ai répété ce que je faisais dans la première moitié pour moissoner les urls des recettes végés, mais en ajoutant la condition if pour les mots contenant "ofu".

n=0
for plat in plats:
    # print(plat.find("a")["href"])
    urlplat1 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat1:
        liste.append(urlplat1)
        n+=1
        # print(n, urlplat1)

urlp2 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
site = requests.get(urlp2, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat2 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat2:
        liste.append(urlplat2)
        n+=1
        # print(n, urlplat2)

urlp3 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/3"
site = requests.get(urlp3, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat3 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat3:
        liste.append(urlplat3)
        n+=1
        # print(n, urlplat3)

urlp4 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/4"
site = requests.get(urlp4, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat4 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat4:
        liste.append(urlplat4)
        n+=1
        # print(n, urlplat4)

urlp5 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/5"
site = requests.get(urlp5, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat5 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat5:
        liste.append(urlplat5)
        n+=1
        # print(n, urlplat5)

urlp6 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/6"
site = requests.get(urlp6, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat6 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat6:
        liste.append(urlplat6)
        n+=1
        # print(n, urlplat6)

urlp7 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/7"
site = requests.get(urlp7, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat7 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat7:
        liste.append(urlplat7)
        n+=1
        # print(n, urlplat7)

urlp8 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
site = requests.get(urlp8, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat8 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat8:
        liste.append(urlplat8)
        n+=1
        # print(n, urlplat8)

urlp9 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
site = requests.get(urlp9, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat9 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat9:
        liste.append(urlplat9)
        n+=1
        # print(n, urlplat9)

urlp10 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
site = requests.get(urlp10, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat10 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat10:
        liste.append(urlplat10)
        n+=1
        # print(n, urlplat10)

urlp11 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
site = requests.get(urlp11, headers=entetes)
page = BeautifulSoup(site.text,"html.parser")
plats = page.find_all("h2", class_="title")

for plat in plats:
    # print(plat.find("a")["href"])
    urlplat11 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
    if "ofu" in urlplat11:
        liste.append(urlplat11)
        n+=1
        # print(n, urlplat11)

print(liste)

platsveges = open(fichier, "a")
tofu = csv.writer(platsveges)
tofu.writerows(liste)