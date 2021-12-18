Implementation
------------------------------------------------------------------------------------------------------

(a) Preprocessing
----------------------
The data has then been preprocessed and  filtered such that we consider the texts in English language and among those texts include only the texts which contain the words "DOGE" and "SHIB" using the Python Bindings to CLD2 library to filter the data.

This library has a function detect which effectively checks if a text message belongs to English language or not. After checking the language we trim out the fields and keep only the fields that are relevant for sentiment analysis.

(b) Sentiment Analysis
----------------------
The preprocessed data is then subjected to sentiment analysis using the Valence Aware Dictionary and sEntiment Reasoner(VADER) library in the Natural Language Toolkit (NTLK) and is specifically attuned to sentiments expressed in social media.

Each text message is analysed the probability scores for the message is provided as 4 values named as pos(probability for positivity), neu(probability for neutrality), neg(probability for negativity), compound (normalized compound score which calculates the sum of all lexicon ratings and takes values from -1 to 1)

All the probabilites (positivity, negativity and neutrality) add up to 1. 
Compound score is the overall sentiment.
Overall sentiment will be 
(a) Positive - if score >= 0.05
(b) Neutral  - if score > -0.05 and score < 0.05
(c) Negative - if score <= -0.05

Dataframes are created from the processed data to hold each text message along with their positivity, negativity,neutrality and compound scores. The number of messages and statistics for sentiment analysis for messages in a day are computed by using the groupby attribute of the dataframe.

After the results are computed in the Dataframe, the results are visually represented using the Bar plot in Plotly library. The number of messages analysed in each day is plotted as a graph with count and date  values as the y and x axis respectively. The average positivity,negativity,neutrality score in a day's text message have been analysed and plotted as graph. Similarly the sentiment score generated (compound attribute) for all the texts in a day has been plotted as Bar plot.

Results
------------------------------------------------------------------------------------------------------

The data has been obtained from Telegram in the form a JSON file called result.json

The data has been reduced from 49436 to 1001 relevant messages and for the next stage of sentiment analysis only the relevant fields such as date and text alone have been considered and rest of the fields have been discarded since they don't have much use in this scenario and preprocessed result has been stored in preprocessed.json

The preprocessed data is then sent to the sentiment analyzer where we get the positivity, negativity, neutrality and overall sentiment score for each message and these statistics are grouped by the date constraint. The grouped data results are represented in the form of graphs.  

There are 3 graph images that are attached here
(a) messageCount.png - This graph plots the number of messages in each day as a bar plot.
(b) averagePositivityNegativityNeutrality.png - This graph plots the average positivity score, negativity score and neutrality score that is computed for each day.
(c) averageSentimentAnalysisScore.png - This graph plots the average sentiment score for all the text messages in each day.

Instructions to run code 
------------------------------------------------------------------------------------------------------
All the packages required have been mentioned in the requirements.txt

To install the packages use the following command
pip3 install -r requirements.txt

To perform pre-processing of the data from Telegram
python3 preprocessing.py

To perform the sentiment analysis and obtain the results
python3 sentimentAnalysis.py