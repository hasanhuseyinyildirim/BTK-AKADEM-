import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error,root_mean_squared_error

diabetes=load_diabetes()

X=diabetes.data #features
y=diabetes.target #target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#decision tree regression

tree_reg=DecisionTreeRegressor(random_state=42)
tree_reg.fit(X_train,y_train)

y_pred=tree_reg.predict(X_test)

mse=mean_squared_error(y_test,y_pred)
rmse=root_mean_squared_error(y_test,y_pred)

print("mse..:",mse)
print("rmse..:",rmse)
print("np.sqrt(mse)..:",np.sqrt(mse))


#kendi datasetimizle örnek 

X=np.sort(5*np.random.rand(80,1),axis=0)
y=np.sin(X).ravel()
y[::5]+=0.5*(0.5-np.random.rand(16))

plt.scatter(X,y)

regr_1=DecisionTreeRegressor(max_depth=2)
regr_2=DecisionTreeRegressor(max_depth=5)
regr_1.fit(X,y)
regr_2.fit(X,y)

X_test=np.arange(0,5,0.05)[:,np.newaxis]
y_pred_1=regr_1.predict(X_test)
y_pred_2=regr_2.predict(X_test)

plt.figure()
plt.scatter(X,y,c="red",label="data")
plt.plot(X,y,c="red",label="data")
plt.plot(X_test,y_pred_1,color="blue",label="Max Depth: 2",linewidth=2)
plt.plot(X_test,y_pred_2,color="green",label="Max Depth : 5",linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.legend()
plt.show()