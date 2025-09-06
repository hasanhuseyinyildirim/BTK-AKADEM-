import requests

url="http://api.weatherapi.com/v1/current.json"
key="6099771d234140538b8183224250308"


while True:
    konum=input("konum..: ")
    response=requests.post(url,params={
        "key":key,
        "q":konum,
        "lang":"tr"
    })

    sonuc=response.json()
    sehir=sonuc["location"]["name"]
    havadurumu=sonuc["current"]["temp_c"]
    text=sonuc["current"]["condition"]["text"]
    print(f"{sehir} {havadurumu} derece,hava {text}")