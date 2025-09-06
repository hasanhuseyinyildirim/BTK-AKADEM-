import requests
from bs4 import BeautifulSoup
from csv import writer

url="https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"

response=requests.get(url)

html=BeautifulSoup(response.text,"html.parser")
kurslar=html.find(id="gbt_catalog-main-right-course")
print(kurslar)

......
