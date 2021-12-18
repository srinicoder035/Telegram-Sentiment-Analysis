from textblob import TextBlob
import json
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px

with open("preprocessed.json","r") as fileName:
    data = json.load(fileName)

analyzer = SentimentIntensityAnalyzer()
messageData = []
processedList = data["messages"]

for i in processedList:
    score = analyzer.polarity_scores(i["text"])
    messageSentiment = {}
    messageSentiment["date"] = i["date"][:10]
    messageSentiment["text"] = i["text"]
    messageSentiment["neg"]  = score["neg"]
    messageSentiment["neu"]  = score["neu"]
    messageSentiment["pos"]  = score["pos"]
    messageSentiment["score"]  = score["compound"]
    messageData.append(messageSentiment)

df = pd.DataFrame(messageData)
df1 = df.groupby("date").mean()
df1.reset_index(inplace=True)
df2 = df.groupby("date").count()
df2.reset_index(inplace=True)
df2 = df2.drop(columns = ['text','neg','neu','pos'])
df2 = df2.rename(columns={"score":"count"})

count = px.bar(df2,x ="date",y ="count",barmode="group")
count.show()
averageScores = px.bar(df1,x ="date",y =["neg", "neu", "pos"], barmode="group")
averageScores.show()
averageSentimentAnalysisScore = px.bar(df1,x ="date",y ="score", barmode="group")
averageSentimentAnalysisScore.show()