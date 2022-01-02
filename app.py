#!/usr/bin/env python
# coding: utf-8

# In[1]:
# My app has been deployed at : https://sentimentproductrecommendatio.herokuapp.com/

import pandas as pd
user_final_rating = pd.read_csv("user_final_rating.csv",index_col='reviews_username')
df_predicted = pd.read_csv("df_predicted_xg.csv",index_col='Unnamed: 0')


# In[2]:
def get_top_5_sentiment_reommendation(user_input):
      d = user_final_rating.loc[user_input].sort_values(ascending=False)[0:20]
      dict_scores={}
      for a in d.index:
        #print(a,d[a])
        #Normalized Score for sentiment positive
        pos_score = df_predicted[df_predicted['name']==a].predicted_sentiment.value_counts(normalize=True)[1]
        rec_score = d[a]
        #Multiplying both
        final_score = pos_score*rec_score
       # print(a)
        dict_scores[a]=final_score
      b = sorted(dict_scores, key=dict_scores.get, reverse=True)[:5]
     # print(b)
      return b


from flask import Flask, request, render_template
app = Flask(__name__, static_url_path='',static_folder='static/css', template_folder='templates')
@app.route('/')
def home():
    print("I am in home")
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("I am in result")
    user_input = request.form.get("username")
    try:
        output = get_top_5_sentiment_reommendation(user_input)
        print(output)
        #return render_template('result.html', prediction_text="Top 5 products are".format(user_input))
        return render_template('result.html', prediction_text="Top 5 products are".format(user_input), data=output)
    except Exception as e:
        print(e)
        return render_template("index.html", message="Oops!! No such user in Database")
        


# In[5]:


if __name__=='__main__':
    app.run(debug=True)


# In[ ]:




