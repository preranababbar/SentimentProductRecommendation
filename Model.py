#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# user input, define function and take input


# In[1]:


import pandas as pd
import pickle


# In[27]:


class Model:
    
    def __init__(self):
        self.user_final_rating = pd.read_csv("user_final_rating.csv",index_col='reviews_username')  
        #User final rating contains final ratings from user-user based recommendation system.
        self.df_predicted = pd.read_csv("df_predicted_xg.csv",index_col='Unnamed: 0')
        #df predicted has been created previously in notebook from XG model on cleaned df data
    
    def get_top_5_sentiment_reommendation(self,user_input):
        
      d = self.user_final_rating.loc[user_input].sort_values(ascending=False)[0:20]
      dict_scores={}
      for a in d.index:
        #print(a,d[a])
        #Normalized Score for sentiment positive
        pos_score = self.df_predicted[self.df_predicted['name']==a].predicted_sentiment.value_counts(normalize=True)[1]
        rec_score = d[a]
        #Multiplying both
        final_score = pos_score*rec_score
       # print(a)
        dict_scores[a]=final_score
      b = sorted(dict_scores, key=dict_scores.get, reverse=True)[:5]
     # print(b)
      return b


# In[28]:


model = Model()


# In[29]:


model.get_top_5_sentiment_reommendation('joshua')


# In[ ]:




