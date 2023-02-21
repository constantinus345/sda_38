from mysql import connector
from credentiale import parola
import pandas as pd
from sda_1 import read_tabel_din_wiki

mydb = connector.connect(host = 'localhost',
                         user ='root',
                         password = parola,
                         port = 3306,
                         database = 'romania')
#am creat conexiunea cu baza de date MySQL
#database se va adauga doar dupa ce a fost creata mai jos

print(mydb)
#
# coloane = ['Oras', 'Judet', 'Populatie_2011', 'Populatie_2002', 'Altitudine',
#        'Anul_atestarii']
mycursor = mydb.cursor()
#am creat un obiect de executare in MySQL

query_creare_db = "CREATE DATABASE romania"
mycursor.execute(query_creare_db)
#mycursor.execute("CREATE DATABASE romania")

query_creare_tabel = """
CREATE TABLE romania.orase_ro(
Oras text,
Judet text,
Populatie_2011 int,
Populatie_2002 int,
Altitudine int,
Anul_atestarii int
);
"""

#am creat un obiect de executare a comenzilor
mycursor.execute(query_creare_tabel)

