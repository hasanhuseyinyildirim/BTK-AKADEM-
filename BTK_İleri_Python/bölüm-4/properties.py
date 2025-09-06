class Product:
    def __init__(self,name,price):
        self.name=name
        if price >=0:
            self._price=price
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    def set_price(self,value):
        if value >=0:
            self._price=value
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    def get_price(self):
        return self._price

        
p = Product("Iphone 16",80000)

p.set_price (70000)

#print(p.name,p.price)
        