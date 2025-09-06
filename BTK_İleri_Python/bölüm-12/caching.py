import mysql.connector
from cachetools import cached,TTLCache
import time

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1001.Hasan",
    database="shopdb"
)

@cached(cache=TTLCache(maxsize=32,ttl=60))
def getProducts():
    cursor=db.cursor() 
    sql="SELECT p.name,c.name FROM products p INNER JOIN categories c ON p.categoryid=c.id  WHERE c.name='Bilgisayar'"
    cursor.execute(sql)
    print("FROM SQL")
    return cursor.fetchall()

s=time.time()
print(getProducts())
print("geçen süre..: ",time.time()-s)

s=time.time()
print(getProducts())
print("geçen süre..: ",time.time()-s)

s=time.time()
print(getProducts())
print("geçen süre..: ",time.time()-s)