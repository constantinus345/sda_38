from mysql import connector
from credentiale import parola

mydb = connector.connect(host = 'localhost',
                         user ='root',
                         password = parola,
                         port = 3306)

print(mydb)