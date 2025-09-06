import csv

with open("bölüm-8/urunler.csv") as file:
    csv_reader = csv.DictReader(file,delimiter=",")  #delimiter="," default değeridir. delimiter="|"....
    # print(list(csv_reader))
    for i in csv_reader:
        if i["Category"]=="Telefon" and float(i["Rating"])>=4.5:
            print(i["ProductName"],i["Price"])
