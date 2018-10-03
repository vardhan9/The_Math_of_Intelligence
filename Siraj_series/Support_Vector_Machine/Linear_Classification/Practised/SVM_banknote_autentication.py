#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:43:20 2018

@author: rajavardhan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("banknote.txt")

X= data.iloc[:,0:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 

from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train)  

y_pred = svclassifier.predict(X_test)


from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred,y_test))


