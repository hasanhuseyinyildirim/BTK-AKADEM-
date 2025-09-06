# class CartItem:    #class tanımlama
#     pass

# item1 = CartItem()  #object tanımlama

# item1.name="telefon"
# item1.price=50000
# item1.quantity=2

# item2=CartItem()

# item2.name="bilgisayar"
# item2.price=70000
# item2.quantity=1

# print(item1.name)
# print(item1.price)
# print(item2.name)
# print(item2.price)


class CartItem:    #class tanımlama
     def __init__(self,name,price,quantity):
          self.name=name
          self.price=price
          self.quantity=quantity          
     

item1 = CartItem("bilgisayar",50000,2)  #object tanımlama
item2 = CartItem("telefon",70000,1)
