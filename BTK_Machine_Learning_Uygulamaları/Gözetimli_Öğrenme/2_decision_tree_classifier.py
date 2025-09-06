import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
iris=load_iris()
X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
tree_cls=DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)
tree_cls.fit(X_train,y_train)

y_pred=tree_cls.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy..:",accuracy)

cm=confusion_matrix(y_test,y_pred)
print("confusion matrix ..:",cm)

plt.figure(figsize=(15,10))
plot_tree(tree_cls,filled=True,feature_names=iris.feature_names,class_names=list(iris.target_names))
plt.show()

feature_importances=tree_cls.feature_importances_
feature_names=iris.feature_names
feature_importances_sorted=sorted(zip(feature_importances,feature_names),reverse=True)

for importance,feature_name in feature_importances_sorted:
    print(f"{feature_name}:{importance}")

#feature selection
import warnings
warnings.filterwarnings("ignore")
from sklearn.inspection import DecisionBoundaryDisplay
iris=load_iris()

n_classes=len(iris.target_names)
plot_colors="ryb"

for pairidx,pair in enumerate ([[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]):

    X=iris.data[:,pair]
    y=iris.target

    clf=DecisionTreeClassifier().fit(X,y)

    ax=plt.subplot(2,3,pairidx+1)
    plt.tight_layout(h_pad=0.5,w_pad=0.5,pad=2.5)
    DecisionBoundaryDisplay.from_estimator(clf,
                                           X,
                                           cmap=plt.cm.RdYlBu,
                                           response_method="predict",
                                           ax=ax,
                                           xlabel=iris.feature_names[pair[0]],
                                           ylabel=iris.feature_names[pair[1]])
    
    for i,color in zip(range(n_classes),plot_colors):
        idx=np.where(y==i)
        plt.scatter(X[idx,0],X[idx,1],c=color,label=iris.target_names[i],
                    cmap=plt.cm.RdYlBu,
                    edgecolors="black")
        
plt.legend()
plt.show()




