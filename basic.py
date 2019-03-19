from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib as mtb
import pickle

data = pd.read_csv("kc1.csv")
x = data.iloc[:,[0,1,4,5,7,9,11,12,13,14,16,17,18,19]].values
y = data.iloc[:,21].values

from sklearn.preprocessing import LabelEncoder
l =LabelEncoder()
y =l.fit_transform(y[:])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)


from sklearn.ensemble import RandomForestRegressor
r =RandomForestRegressor(n_estimators = 10,random_state=0)
r.fit(x_train,y_train)

filename = 'finalized_model.sav'
pickle.dump(r, open(filename, 'wb'))

y1 =r.predict(x_test)
y1 = np.around(y1)
#print(y1,y_test)

"""python3 basic.py
[1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0.] [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0
 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]"""

