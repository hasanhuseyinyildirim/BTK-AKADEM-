db ={
    "users":{
        "hasanyildirim":{
            "firstName":"Hasan",
            "lastName":"Yıldırım"
        },
        "hüseyinyildirim":{
            "firstName":"Hüseyin",
            "lastName":"Yıldırım"
        }
    },

    "products":{
        "1": {
            "title": "Samsung S25",
            "price": 90000
        },
        "2": {
            "title": "MacBook Air",
            "price": 90000
        }       
    }
}

import json

# with open("bölüm-9/db.json","w",encoding="utf-8") as file:
#     json.dump(db,file,ensure_ascii=False,indent=2)

with open("bölüm-9/db.json",encoding="utf-8") as file:
    data=json.load(file)

    print(data["users"]["hasanyildirim"]["firstName"])
    print(data["products"]["2"]["title"])


    data["products"].update({
        "4":{
            "title":"deneme",
            "price":2
        }
    })

with open("bölüm-9/db.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

