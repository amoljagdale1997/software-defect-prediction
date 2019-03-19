from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib as mtb


data = pd.read_csv("jm1.csv")
x = data.iloc[:,[0,4,5,7,11,12,13,14,16,17,18,19]].values
y = data.iloc[:,21].values
print(x.shape)
from sklearn.preprocessing import LabelEncoder
l =LabelEncoder()
y =l.fit_transform(y[:])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.1,random_state=0	)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors =5 ,metric ='minkowski',p=2)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)																																																																																																																																																				       

'''for x in range(len(y_pred)):
	print(y_pred[x],y_test[x])'''

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)
print (acc)


from sklearn.metrics import confusion_matrix
acc1 = confusion_matrix(y_test, y_pred)
print (acc1)
