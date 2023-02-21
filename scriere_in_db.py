from sqlalchemy import create_engine
#pip install sqlalchemy
import pandas as pd
#pip3 install mysqlclient

from credentiale import parola
from sda_1 import  read_tabel_din_wiki

host = 'localhost',
user ='root',
port = 3306,
database = 'romania'
engine = create_engine(f"mysql+mysqldb://{user}:{parola}@{host}/{database}")

#am creat un alt tip de obiect de conexiune cu MySQL prin libraria sqlalchemy

tabel = read_tabel_din_wiki()
tabel_din_baza_de_date = 'orase'

with engine.begin() as connection:
    #m-am conectat la db printr-un context manager si i-am dat un alias (pseudonim?) connection
    tabel.to_sql(tabel_din_baza_de_date, con=connection, if_exists='append')
    #to_sql este functie a pandas prin care ne introducem datele in MySQL