#!/usr/bin/env python
# coding: utf-8

# In[6]:


import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)
import sklearn; print("sklearn", sklearn.__version__)


from sklearn.datasets import load_iris
import pandas as pd
import os


# In[7]:


def create_load_iris(df_name = "iris_df.csv"):
    
    path = os.getcwd()
    
    iris_arr = load_iris()

    X = iris_arr["data"]

    y = iris_arr["target"]
    
    iris_df = pd.DataFrame(X)
    iris_df.columns = list(iris_arr["feature_names"])
    iris_df["target"] = y

    iris_df = iris_df.rename(columns={"sepal length (cm)": "sepal_length", "sepal width (cm)": "sepal_width",
                 "petal length (cm)":"petal_length","petal width (cm)":"petal_width"})
    
    saved_path = os.path.join(path,df_name)
    
    iris_df.to_csv(df_name,index=False)

    return iris_df, path


if __name__ =="__main__":
    iris_df,path = create_load_iris()

    joined_path = os.path.join(path,"data_here","output.csv")

    print(joined_path)

    iris_df.to_csv(joined_path, index=False)
    
    print("data is saved at:", path)


# In[ ]:




