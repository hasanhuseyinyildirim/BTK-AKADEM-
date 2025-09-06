import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#veri yükleme
veriler=pd.read_csv("eksikveriler.csv")

#eksik veri tamamlama


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
Yas=veriler.iloc[:,1:4].values
imputer=imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])

# #yukardaki kodla aynı işlevi görüyor sadece yukardaki kod değerleri array olarak yazıyor

# veriler=veriler.fillna(veriler["yas"].mean())

#encoder: Kategorik ---> Numeric

ulke=veriler.iloc[:,0:1].values

from sklearn import preprocessing

labelEnc=preprocessing.LabelEncoder()
ulke[:,0]=labelEnc.fit_transform(veriler.iloc[:,0])

oneHotEnc=preprocessing.OneHotEncoder()
ulke=oneHotEnc.fit_transform(ulke).toarray()

#numpy dizileri dataframe donusumu

sonuc=pd.DataFrame(data=ulke,index=range(22),columns=["fr","tr","us"])

sonuc2=pd.DataFrame(data=veriler,index=range(22),columns=["boy","kilo","yas"])

cinsiyet=veriler.iloc[:,-1].values

sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])

#dataframe birleştirme

sonVeri=pd.concat([sonuc,sonuc2,sonuc3],axis=1)

#verilerin train ve test için bölünmesi

from sklearn.model_selection import train_test_split
y=sonVeri["cinsiyet"]
x=sonVeri.drop(["cinsiyet"],axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=0)

#verilerin ölçeklendirilmesi

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train=scaler.fit_transform(x_train)
X_test=scaler.fit_transform(x_test)

#backward elimination
import statsmodels.api as sm

X = np.append(arr=np.ones((22,1)).astype(int),values=veri,axis=1)

X_liste = veri.iloc[:,[0,1,2,3,4,5]].values
X_liste = np.array(X_liste,dtype=float)
model = sm.OLS(boy,X_liste).fit()
model.summary()