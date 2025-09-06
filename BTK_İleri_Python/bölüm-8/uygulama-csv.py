import csv

with open("bölüm-8/onlinefoods.csv") as file:
    csv_reader=csv.reader(file)
    liste=list(csv_reader)

# online yemek şipariş eden kişi sayısı
    print(len(liste)-1) 

# online yemek veren öğrenciler
with open("bölüm-8/onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    liste=[user for user in csv_reader if user["Occupation"]=="Student"]
    print(len(liste))

# 20-30 yaş aralığı adres bilgileri
with open("bölüm-8/onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    users=(user for user in csv_reader if int(user["Age"])>20 and int(user["Age"])<30)

    for i in users:
        print(i["latitude"],i["longitude"])
