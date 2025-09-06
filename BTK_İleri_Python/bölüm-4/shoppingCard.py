class CartItem:    #class tanımlama
     def __init__(self,name,price,quantity):
          self.name=name
          self.price=price
          self.quantity=quantity          
     

item1 = CartItem("bilgisayar",50000,2)  #object tanımlama
item2 = CartItem("telefon",70000,1)
item3 = CartItem("kitap",500,3)

class ShoppingCart:
    def __init__(self,liste):
        self.liste=liste

    def addItem(self,item):
        self.liste.append(item)

    def display_items(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")


    def calculate_total(self):
        return sum([item.price * item.quantity  for item in self.liste])
    

    def remove_item(self,cart_item):
        self.liste=[item for item in self.liste if item != cart_item]

    def clear(self):
        self.liste=[]


sc = ShoppingCart([item1,item2])
sc.addItem(item3)
sc.display_items()

print(sc.calculate_total())

sc.remove_item(item1)

sc.display_items()

sc.clear()

sc.display_items()

