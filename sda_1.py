import pandas as pd
# pip install pandas lxml
from time import sleep

url = 'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Romania'
#url_2 = 'https://www.imdb.com/chart/top/'

tabeluri = pd.read_html(url)

# print(len(tabeluri))
# for index, tabel in enumerate(tabeluri):
#     print(f"tabelul {index} are {len(tabel)} randuri si coloanele = {tabel.columns}")
#     sleep(0.5)

tabel_de_interes = tabeluri[2]
print(tabel_de_interes.head)