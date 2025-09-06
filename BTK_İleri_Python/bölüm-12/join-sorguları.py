import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1001.Hasan",
    database="shopdb"
)
cursor=db.cursor()

# sql ="SELECT * FROM products"
# sql ="SELECT * FROM categories"
# sql ="SELECT products.name,categories.name FROM products INNER JOIN categories ON products.categoryid=categories.id"
sql ="SELECT p.name,c.name FROM products p INNER JOIN categories c ON p.categoryid=c.id"


cursor.execute(sql)

result=cursor.fetchall()

print(result)