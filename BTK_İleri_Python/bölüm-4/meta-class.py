# class Test():
#     pass


# sonuc=Test()
# sonuc=Test
# sonuc=type(Test)



# print(sonuc)


class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)

        a={}

        for name,val in attrs.items():
            if name.startswith("_"):
                a[name]=val
            else:
                a[name.upper()]=val

        return type(class_name,bases,attrs)
    
class Person(metaclass=Meta):
    x=5
    y=10
    _age = 40

    def hello(self):
        print("Merhaba")

p=Person()

sonuc=p.x
sonuc=p.y

print(sonuc)