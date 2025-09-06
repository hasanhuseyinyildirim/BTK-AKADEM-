def selamlama(fn):
    def inner(isim):
        print("hoş geldiniz")
        fn(isim)
        print("görüşmek üzere")
    return inner

@selamlama
def gunaydin(isim):
    print(f"günaydın benim adım {isim}")
    
@selamlama
def iyigunler(isim):
    print(f"iyi günler benim adım {isim}") 


# gn = selamlama(gunaydin)
# ig = selamlama(iyigunler)

# gn()
# ig()

gunaydin("Hasan")
iyigunler("Hüseyin")