import pandas as pd
#pandas este o librarie de lucru cu date tabelare (destul de populara)
# pip install pandas lxml
from time import sleep
#sleep ne ajuta sa luam o pauza din executarea codului

def read_tabel_din_wiki():
    url = 'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Romania'
    #url_2 = 'https://www.imdb.com/chart/top/'
    tabele = pd.read_html(url)
    #am citit o lista de tabeluri de pe site-ul indicat

    # print(len(tabele))
    # for index, tabel in enumerate(tabele):
    #     print(f"tabelul {index} are {len(tabel)} randuri si coloanele = {tabel.columns}")
    #     sleep(0.5)
    #prin codul comentat de mai sus mi-am identificat tabelul meu de interes, pentru a citit tocmai 11 tabele

    tabel_de_interes = tabele[2]
    #tabelul meu de interes are indexul [2]
    return tabel_de_interes

tabel = read_tabel_din_wiki()

coloane = ['City', 'County', 'Population (2011)[2]', 'Population (2002)',\
       'Elevation (m)', 'Year status granted (a) or first attested (b)',\
        'Image']

#print(tabel.columns)
#printeaza coloanele tabelului
#print(tabel["Image"][0])
#verific daca image are ceva date
tabel = tabel.drop(["Image"], axis=1)
#print(tabel.columns)
#am scapat de coloana "Image" pentru ca nu avea date relevante

#rename table columns df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
tabel = tabel.rename(columns={"City":"Oras","County":"Judet","Population (2011)[2]":"Populatie 2011",\
                              "Population (2002)":"Populatie 2002","Elevation (m)":"Altitudine",\
                              "Year status granted (a) or first attested (b)":"Anul atestarii"})




