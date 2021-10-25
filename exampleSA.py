import shutil, os
import re

import pandas as pd
from csv import writer
import numpy as np
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot

dir = "..."
dir1 = dir + "ethics_csv"
windowdata_fp = dir + "topicmodel_sent"

SIA = SentimentIntensityAnalyzer()

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
data = pd.read_csv("...file path...", encoding='latin-1')
df = pd.DataFrame(data)
df.columns = ["item","ratio","window","sent_scores"]
df[["ratio", "sent_scores"]] = df[["ratio", "sent_scores"]].apply(pd.to_numeric)
print(df.head())

sns.set_theme(style="whitegrid")
bplot = sns.boxplot(y='sent_scores',x='item',data=df,width=0.5)
bplot.set(ylim=(-1, 1))
matplotlib.pyplot.show()