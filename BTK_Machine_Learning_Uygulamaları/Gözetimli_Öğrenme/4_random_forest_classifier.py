import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
oli=fetch_olivetti_faces() # 2D(64x64)  -> 1D (4096)

#veri görselleştirme
plt.figure()
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(oli.images[i],cmap="gray")
    plt.axis("off")
plt.show()

X=oli.data
y=oli.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=0)


rf_cls=RandomForestClassifier(n_estimators=100,random_state=0)
rf_cls.fit(X_train,y_train)
y_pred=rf_cls.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)

print(accuracy)