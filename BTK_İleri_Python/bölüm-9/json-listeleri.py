

data = [
    {
        "id": 1,
        "title": "MacBook Pro",
        "price": 80000
    },
    {
        "id": 2,
        "title": "MacBook Air",
        "price": 70000
    }
]
import json
# with open("bölüm-9/products.json","w",encoding="utf-8") as file:
#     json.dump(data,file,indent=2)

product = {
        "id": 3,
        "title": "Samsung S23",
        "price": 50000
}

with open("bölüm-9/products.json") as file:
    products = json.load(file)

for p in products:
    if p["title"] == "Samsung S23":
        p["title"] = "Samsung S24"
#products.append(product)
products.remove(products[0])


with open("bölüm-9/products.json","w",encoding="utf-8") as file:
    json.dump(products,file,indent=2)
    
