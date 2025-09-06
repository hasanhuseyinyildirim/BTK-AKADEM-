import csv


with open ("bölüm-8/urunler2.csv","w",newline="") as file:
    headers=["Id","ProductName","Price","IsActive","Category","Rating"]
    csv_writer=csv.DictWriter(file,headers)
    csv_writer.writeheader()

    # csv_writer.writerow({
    #     "Id":1,
    #     "ProductName":"Iphone 14",
    #     "Price":40000,
    #     "IsActive":True,
    #     "Category":"Telefon",
    #     "Rating":4.5
    # })

    # csv_writer.writerow({
    #     "Id":2,
    #     "ProductName":"Iphone 15",
    #     "Price":50000,
    #     "IsActive":True,
    #     "Category":"Telefon",
    #     "Rating":4.6
    # })

    csv_writer.writerows(
       [ {"Id":1,
        "ProductName":"Iphone 14",
        "Price":40000,
        "IsActive":True,
        "Category":"Telefon",
        "Rating":4.5},
        {"Id":2,
        "ProductName":"Iphone 15",
        "Price":50000,
        "IsActive":True,
        "Category":"Telefon",
        "Rating":4.6},
        {"Id":3,
        "ProductName":"Iphone 16",
        "Price":60000,
        "IsActive":False,
        "Category":"Telefon",
        "Rating":4.2}])
    

with open ("bölüm-8/urunler2.csv","a",newline="") as file:
    headers=["Id","ProductName","Price","IsActive","Category","Rating"]
    csv_writer=csv.DictWriter(file,headers)

    csv_writer.writerow({
        "Id":4,
        "ProductName":"Iphone 17",
        "Price":70000,
        "IsActive":True,
        "Category":"Telefon",
        "Rating":4.8
    })