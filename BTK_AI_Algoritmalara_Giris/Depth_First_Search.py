

grafik={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":[],
}

ziyaret=[]

def dfs(ziyaret,grafik,dugum):
    if dugum not in ziyaret:
        print(dugum)
        ziyaret.append(dugum)
        for komsu in grafik[dugum]:
            dfs(ziyaret,grafik,komsu)
    


dfs(ziyaret,grafik,"A")