data = {
  "2":{
    "title": "MacBook Air",
    "price": 70000
  },
  "3":{
    "title": "Samsung S24",
    "price": 50000
  }
}

import json

with open("bölüm-9/products.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("bölüm-9/products.json") as file:
    products=json.load(file)

print(products["2"])
print(products["3"])

products.update({
    "1":{
        "title":"MacBook Air",
        "price":90000
    }
})

products.update({
    "3":{
        "title":"Samsung S25",
        "price":90000
    }
})

products.pop("2")

with open("bölüm-9/products.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2) 