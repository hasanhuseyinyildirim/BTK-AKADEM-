import json

with open("bölüm-9/product.json") as file:
    # data = file.read() => string olarak okur 
    data = json.load(file)  #=> dict olarak okur

    #json string
    data="""
        {
            "id":1,
            "title":"MacBook Pro",
            "price":90000,
            "rating":"4.5",
            "category":"Bilgisayar",
            "colors":["Red","Blue"]
        }
    """

    data=json.loads(data)

    print(data)
    print(type(data))
    print(data["title"])
    

    #serialize => encode
    #deserialize => decode

