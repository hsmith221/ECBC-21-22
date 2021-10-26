import shutil, os
import re

import pandas as pd
from csv import writer
import numpy as np
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot

dir = "/Users/shubaprasadh/Downloads/"
dir1 = dir + "ethics_csv"

windowdata_fp = dir + "topicmodel_sent"

new_words = {
    'sin': -1,
    'whore': -1,
    'obedience': 1,
    'obey': 1,
    'disobey': -1,
    'greed': -1,
    'hell': -1,
    'indulgent': -0.5,
    'indulge': -0.5,
    'fellowship': 1,
    'eve': -1,
    'delilah': -1,
    'bathsheba': -1,
    'tempt': -1,
    'temptation': -1,
    'blasphemy': -1,
    'moral': 1,
    'natural': 1,
    'unnatural': -1,
    'holiness': 1,
    'almighty': 1,
    'lust': -1,
    'covetousness': -1,
    'covet': -1,
    'deceit': -1,
    'deceitful': -1,
    'deceitfulness': -1,
    'cheat': -1,
    'wicked': -1,
    'devil': -1,
    'demon': -1,
    'lucifer': -1,
    'excess': -1,
    'avarice': -1,
    'green': 1,
    'vanity': -1,
    'pride': -1,
    'sloth': -1,
    'gluttony': -1,
    'drunk': -1,
    'drunkenness': -1,
    'faith': 1,
    'moral ': 1,
    'immoral ': -1,
    'immorality': -1,
    'kind': 1,
    'kinde': 1,
    'good': 1,
    'happiness': 1,
    'enlightenment': 1,
    'community': 1,
    'dreams': 1,
    'free': 1,
    'friend ': -0.5,
    'friendship': 1,
    'scholastic': 1,
    'ethics': 1,
    'thought ': 1,
    'teaching': 1,
    'law': 1,
    'legal': 1,
    'justice': 1,
    'criminal': -1,
    'indigent': -0.5,
    'uneducated ': -1,
    'nobles': -0.5,
    'nobility': 1,
    'liberalism* ': 1,
    'despotism': -1,
    'gentle': 1,
    'gentleman': 1,
    'gentlewoman': 1
}

SIA = SentimentIntensityAnalyzer()
SIA.lexicon.update(new_words)

# THIS METHOD analyzes sentiment using vader
def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return sentiment_dict['compound']

#           DOING SENTIMENT ANALYSIS
# for f in os.listdir(windowdata_fp):
#     fullname = windowdata_fp+"/"+f
#     if (f.endswith(".csv")) and (f!="template.csv") and (f!=".csv") and (f=="tobacco_file.csv"):
#         df = pd.read_csv(windowdata_fp + "/" + f, header=None, encoding='latin-1')
#
#         df.columns = ["item","ratio","window"]
#         scoresList = []                     #note that this func will throw an error if the csv if empty, but we can safely assume that none of these will be
#         for row, i in df.iterrows():
#             text = df._get_value(row,'window')
#             scoresList.append(sentiment_scores(text))
#         df['sent_scores'] = scoresList
#         df.to_csv(fullname, index=False)

#          Building visualizations
data = pd.read_csv("/Users/shubaprasadh/Downloads/topicmodel_sent/combined_file.csv", encoding='latin-1')
df = pd.DataFrame(data)
df.columns = ["item","ratio","window","sent_scores"]
df[["ratio", "sent_scores"]] = df[["ratio", "sent_scores"]].apply(pd.to_numeric)
print(df.head())

sns.set_theme(style="whitegrid")
bplot = sns.boxplot(y='sent_scores',x='item',data=df,width=0.5)
bplot.set(ylim=(-1, 1))
matplotlib.pyplot.show()
