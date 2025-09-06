import re


text="A125a ABC 123 XYZ 456 @&% 300 2 34 1455 abc aKx A343A"

# pattern="\d\d\d" #sayısayısayı
# pattern = r"\d+" #1 veya daha fazla sayı
# pattern = r"\d*" #sıfır veya daha fazla sayı (boşlukları da verir bize)
# pattern = r"\d{3}" #3 basamaklı sayı
# pattern = r"\d{3,5}" #3,4,5 basamaklı sayı
# pattern = r"\d{3,}"  #3 ve daha büyük basamaklı sayı
# pattern = r"\d{,5}"  #en fazla 5  basamaklı sayı
# pattern = r"\d.\d" 
# pattern= r"[a-zA-Z0-9]"
# pattern = r"\d|[a-z]"
# pattern = r"\d\w\w\w"
# pattern = r"^A\d\w\w\w"
pattern = r"A\d\w\w\w$"


# matches = re.search(pattern,text) #tek bir eleman döndürür
# matches = re.finditer(pattern,text) #iterator döndürür

matches = re.findall(pattern,text)

sonuc=matches

print(sonuc)