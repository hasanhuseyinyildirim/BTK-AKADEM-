from bs4 import BeautifulSoup

with open("bölüm-11/index.html",encoding="utf-8") as file:
    html=file.read()

obj=BeautifulSoup(html,"html.parser")

sonuc= obj.body.div.contents[3]

for i in obj.body.div.children:
    print(i)

print("-----------------------------------------------")
for i in obj.body.div.descendants:
    print(i)


#print(sonuc)