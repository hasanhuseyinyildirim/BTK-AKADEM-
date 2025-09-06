import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("satislar.csv")

satislar = veriler[["Satislar"]]
aylar = veriler[["Aylar"]]

#verilerin train ve test için bölünmesi

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(aylar,satislar,test_size=0.33,random_state=0)

'''
#verilerin ölçeklendirilmesi

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X_train=scaler.fit_transform(x_train)
X_test=scaler.fit_transform(x_test)
Y_train=scaler.fit_transform(y_train)
Y_test=scaler.fit_transform(y_test)

'''


#model inşası(linear regresyon)
from sklearn.linear_model import LinearRegression
linReg =LinearRegression()
linReg.fit(x_train,y_train)

tahmin=linReg.predict(x_test)

#verileri görselleştirme
x_train=x_train.sort_index()
y_train=y_train.sort_index()
plt.plot(x_train,y_train)
plt.plot(x_test,linReg.predict(x_test))
plt.title("aylara göre satis")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.show() 