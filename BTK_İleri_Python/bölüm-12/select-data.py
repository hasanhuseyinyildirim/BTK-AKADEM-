import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1001.Hasan",
    database="shopdb"
)
cursor=db.cursor()

# sql="SELECT * FROM products"
# sql="SELECT id,name FROM products"
sql="SELECT * FROM products WHERE id=1"

cursor.execute(sql)

# products=cursor.fetchall()
result=cursor.fetchone()

# for p in products:
#     print(p[0],p[1])

print(result)