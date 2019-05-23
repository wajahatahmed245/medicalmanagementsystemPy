#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fitter import Fitter
import seaborn as sns
import scipy.stats as ss
from sklearn.utils import resample
from sklearn.utils import shuffle
from sklearn.model_selection import *
from sklearn import model_selection
from sklearn.preprocessing import *
from sklearn.metrics import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.svm import *
from sklearn.linear_model import *
from sklearn.model_selection import KFold


# In[6]:

def predict_medicine(symptoms):
    dataset=pd.read_csv('/home/wajahatahmed/PycharmProjects/medicalmanagementsystem/Homeopathic_Medicine/Doctor/DATANEW.csv',engine='python')


    # In[7]:


    dataset.head()


    # In[8]:


    from sklearn.feature_extraction.text import CountVectorizer
    corpus = dataset.iloc[:,0]
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())

    vectors=pd.DataFrame(vectors.todense(), columns=vectorizer.get_feature_names())
    print(vectors)


    # In[9]:


    y=dataset.iloc[:,-1]
    labelencoder_y = LabelEncoder()
    y = labelencoder_y.fit_transform(y)


    # In[10]:


    X,Y=shuffle(vectors,y)


    # In[11]:


    Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.3,random_state=42)


    # In[12]:


    from sklearn.multioutput import MultiOutputClassifier
    from sklearn.linear_model import LogisticRegression
    lr = LogisticRegression()
    lr.fit(Xtrain, Ytrain)


    # In[13]:


    predictions=lr.predict(Xtest)
    print(classification_report(Ytest,predictions))


    # In[14]:


    symp=symptoms

    probabilities=np.vstack(lr.predict_proba(vectorizer.transform([symp.lower()])))


    # In[15]:

    result = []
    index = 0
    for i, j in sorted(zip(labelencoder_y.classes_, probabilities[0]), key=lambda t: t[1], reverse=True):
        if j > 0.30:
            #         print('***********************************************')

            result.append(i)

            index = index + 1
            if index == 3:
                break
    return result


# In[16]:




# In[ ]:



