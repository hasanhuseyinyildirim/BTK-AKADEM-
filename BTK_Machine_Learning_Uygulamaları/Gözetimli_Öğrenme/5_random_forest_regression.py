from sklearn.datasets import fetch_california_housing 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

house=fetch_california_housing()
X=house.data
y=house.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

rf_reg=RandomForestRegressor(n_estimators=100,random_state=42)
rf_reg.fit(X_train,y_train)

y_pred=rf_reg.predict(X_test)

rmse=root_mean_squared_error(y_test,y_pred)

print(rmse)

