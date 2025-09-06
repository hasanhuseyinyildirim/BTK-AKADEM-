from bs4 import BeautifulSoup

with open("bölüm-11/index.html",encoding="utf-8") as file:
    html=file.read()


obj=BeautifulSoup(html,"html.parser")

sonuc=obj
sonuc=type(obj)
sonuc=type(html)
sonuc=obj.prettify()
sonuc=obj.title
sonuc=type(obj.title)
sonuc=obj.title.name
sonuc=obj.title.string

sonuc=obj.body.h1.string
sonuc=obj.ul
print(sonuc) 