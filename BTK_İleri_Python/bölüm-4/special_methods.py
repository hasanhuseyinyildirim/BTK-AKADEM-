class Movie:
    def __init__(self,title,director,year,duration):
        self.title=title
        self.director=director
        self.year=year
        self.duration=duration

    def __repr__(self):
        return f"{self.title},{self.director},{self.year} yılında yayınlandı."
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("film silindi")


m= Movie("film adı","film yönetmeni","yayın tarihi",120)

# print(m)   # print(m.__repr__())

print(m.__repr__())

print(len(m))

del m