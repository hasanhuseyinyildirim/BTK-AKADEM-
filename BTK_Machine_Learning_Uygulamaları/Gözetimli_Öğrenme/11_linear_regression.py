import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import root_mean_squared_error
import numpy as np

#veri oluştur
X=np.random.rand(100,1)
y=3+4*X+0.5*np.random.rand(100,1)  #y=3+4x

lin_reg=LinearRegression()
lin_reg.fit(X,y)

plt.figure()
plt.scatter(X,y)
plt.plot(X,lin_reg.predict(X),color="red",alpha=0.7)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")


#y=a0 + a1x
a1=lin_reg.coef_[0][0]
print("a1.:",a1)

a0=lin_reg.intercept_[0]
print("a0.:",a0)

for i in range(100):
    y_=a0+a1*X
    plt.plot(X,y_,color="green",alpha=0.7)

plt.show()