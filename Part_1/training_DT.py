#!/usr/bin/env python
# coding: utf-8

# In[11]:


import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)

import os
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


import pandas as pd
from joblib import dump


# In[19]:


def main_py():


    # comes as a dictionary where the key "data" has the value "array" which is our dataset and the "target" which is the label vector.
    
    path = os.getcwd()
    df_name = "iris_df.csv"
    full_path = os.path.join(path,df_name)

    iris_df = pd.read_csv(full_path)

    X = iris_df.drop("target",axis=1)

    y = iris_df["target"]


    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 50, test_size = 0.25)


    clf = AdaBoostClassifier(n_estimators=21,algorithm='SAMME.R')

    clf.fit(X_train,y_train)

    # Predict Accuracy Score
    y_pred = clf.predict(X_test)
    print("Train data accuracy:",accuracy_score(y_true = y_train, y_pred=clf.predict(X_train)))
    print("Test data accuracy:",accuracy_score(y_true = y_test, y_pred=y_pred))
    
if __name__ == '__main__':
    main_py()

