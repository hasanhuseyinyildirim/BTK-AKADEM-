import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1001.Hasan",
    database="shopdb"
)
cursor=db.cursor()

sql="INSERT INTO products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"

# value=("Iphone 16",70000,"3.jpg","iyi bir telefon")
values=[
    ("Samsung S23",80000,"4.jpg","iyi bir telefon"),
    ("Samsung S24",90000,"5.jpg","iyi bir telefon"),
    ("Samsung S25",950000,"6.jpg","iyi bir telefon"),
    ]

# cursor.execute(sql,value)
cursor.executemany(sql,values)

try:
    db.commit()
    print(cursor.rowcount," kayıt edildi")
    print(f"son eklenen kaydın id: {cursor.lastrowid}")
except mysql.connector.Error as err:
    print("hata:",err)
finally:
    cursor.close()
    db.close()
    print("bağlantı kapatıldı")