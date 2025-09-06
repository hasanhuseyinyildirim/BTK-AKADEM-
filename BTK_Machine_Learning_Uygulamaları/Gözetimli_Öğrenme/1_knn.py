import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

cancer=load_breast_cancer()
df=pd.DataFrame(data=cancer.data,columns=cancer.feature_names)
df["target"]=cancer.target

X=cancer.data
y=cancer.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)

accuracy=accuracy_score(y_test ,y_pred)
print("Doğruluk ..: " ,accuracy)
cm=confusion_matrix(y_test,y_pred)
print("confusion_matrix..: ",cm)

k=1
accuracy_values=[]
k_values=[]
for k in range(1,22):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,y_train)
    y_pred=knn.predict(X_test)
    accuracy=accuracy_score(y_test ,y_pred)
    accuracy_values.append(accuracy)
    k_values.append(k)

plt.figure()
plt.plot(k_values,accuracy_values,marker="o",linestyle="-")
plt.title("K degerine gore dogruluk")
plt.xlabel("K degeri")
plt.ylabel("Dogruluk")
plt.xticks(k_values)
plt.grid(True)
plt.show()