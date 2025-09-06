import json

product = {
    "id":2,
    "title":"MacBook Pro",
    "price":90000,
    "rating":"4.5",
    "category":"Bilgisayar",
    "colors":["Red","Blue"]
}

print(product)
print(type(product))

# sonuc= json.dumps(product)

# print(sonuc)
# print(type(sonuc))

with open("bölüm-9/product.json","w",encoding="utf-8") as file:
    json.dump(product,file,indent=2)
