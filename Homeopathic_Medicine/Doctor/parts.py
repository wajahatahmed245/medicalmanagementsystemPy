#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
from pandas import DataFrame


# In[33]:

# try:
data = pd.read_csv("/home/wajahatahmed/PycharmProjects/medicalmanagementsystem/Homeopathic_Medicine/Doctor/medicine-data.csv")

# except Exception as e:
#     print(e)


# In[80]:



DataFrame.drop_duplicates(data)
d=data.drop_duplicates(subset='Part', keep="last")
d['Part']


# In[35]:


data.describe()


# In[36]:


data.count()


# In[43]:


head=data[data['Part'] == 'Head']
head_symptoms=head['Symptoms']
head_symptoms_list=head_symptoms.tolist()


# In[75]:


Stomach=data[data['Part'] == 'Stomach']
Stomach_symptoms=Stomach['Symptoms']
Stomach_symptoms_list=Stomach_symptoms.tolist()


# In[76]:


Face=data[data['Part'] == 'Face']
Face_symptoms=Face['Symptoms']
Face_symptoms_list=Face_symptoms.tolist()


# In[77]:



Anus=data[data['Part'] == 'Anus']
Anus_symptoms=Anus['Symptoms']
Anus_symptoms_list=Anus_symptoms.tolist()


# In[78]:


# Circulatory Organs

Circulatory_Organs=data[data['Part'] =='Circulatory Organs']
Circulatory_Organs_symptoms=Circulatory_Organs['Symptoms']
Circulatory_Organs_symptoms_list=Circulatory_Organs_symptoms.tolist()


# In[85]:



#  Nose


Nose=data[data['Part'] =='Nose']
Nose_symptoms=Nose['Symptoms']
Nose_symptoms_list=Nose_symptoms.tolist()
Nose_symptoms_list
print(Nose_symptoms_list)


# In[86]:


# 99                    Teeth



Teeth=data[data['Part'] =='Teeth']
Teeth_symptoms=Teeth['Symptoms']
Teeth_symptoms_list=Teeth_symptoms.tolist()
Teeth_symptoms_list


# In[87]:


# 117                    limb

limb=data[data['Part'] =='limb']
limb_symptoms=limb['Symptoms']
limb_symptoms_list=limb_symptoms.tolist()
limb_symptoms_list


# In[88]:


# 120                    Skin


Skin=data[data['Part'] =='Skin']
Skin_symptoms=Skin['Symptoms']
Skin_symptoms_list=Skin_symptoms.tolist()
Skin_symptoms_list


# In[89]:


# 128                   Mouth


Mouth=data[data['Part'] =='Mouth']
Mouth_symptoms=Mouth['Symptoms']
Mouth_symptoms_list=Mouth_symptoms.tolist()
Mouth_symptoms_list


# In[90]:


# 133            Sexual Organ



Sexual_Organ=data[data['Part'] =='Sexual Organ']
Sexual_Organ_symptoms=Sexual_Organ['Symptoms']
Sexual_Organ_symptoms_list=Sexual_Organ_symptoms.tolist()
Sexual_Organ_symptoms_list


# In[91]:


# 138                   Chest
Chest=data[data['Part'] =='Chest']
Chest_symptoms=Chest['Symptoms']
Chest_symptoms_list=Chest_symptoms.tolist()
Chest_symptoms_list


# In[95]:


# appetite

appetite=data[data['Part'] =='appetite']
appetite=appetite['Symptoms']
appetite_symptoms_list=appetite.tolist()
appetite_symptoms_list


# In[96]:


# Generalities


Generalities=data[data['Part'] =='Generalities']
Generalities=Generalities['Symptoms']
Generalities_symptoms_list=Generalities.tolist()
Generalities_symptoms_list


# In[97]:


#  Female Sexual Organs


Female_Sexual_Organs=data[data['Part'] =='Female Sexual Organs']
Female_Sexual_Organs=Female_Sexual_Organs['Symptoms']
Female_Sexual_Organs_symptoms_list=Female_Sexual_Organs.tolist()
Female_Sexual_Organs_symptoms_list


# In[98]:


# 250      Respiratory_Organs


Respiratory_Organs=data[data['Part'] =='Respiratory Organs']
Respiratory_Organs=Respiratory_Organs['Symptoms']
Respiratory_Organs_symptoms_list=Respiratory_Organs.tolist()
Respiratory_Organs_symptoms_list


# In[99]:


# 251                   Heart


Heart=data[data['Part'] =='Heart']
Heart=Heart['Symptoms']
Heart_symptoms_list=Heart.tolist()
Heart_symptoms_list


# In[100]:


# 252                    Back


Back=data[data['Part'] =='Back']
Back=Back['Symptoms']
Back_symptoms_list=Back.tolist()
Back_symptoms_list


# In[101]:


#  Sleep



Sleep=data[data['Part'] =='Sleep']
Sleep=Sleep['Symptoms']
Sleep_symptoms_list=Sleep.tolist()
Sleep_symptoms_list


# In[102]:


# 256                    Mind


Mind=data[data['Part'] =='Mind']
Mind=Mind['Symptoms']
Mind_symptoms_list=Mind.tolist()
Mind_symptoms_list


