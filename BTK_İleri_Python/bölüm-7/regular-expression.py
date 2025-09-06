import re


text="BTK Akademi Python Dersleri BTK"
pattern="BTK"


match=re.search(pattern,text)
# match=match.start()
# match=match.end()
# match=match.span()

match=re.findall(pattern,text)


sonuc = match
print(sonuc)