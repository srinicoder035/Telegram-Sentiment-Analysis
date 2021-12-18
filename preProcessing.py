import json
import pycld2 as cld2
from tqdm import tqdm

with open("result.json","r") as fileName:
    data = json.load(fileName)

messages = data["messages"]
processedList = []
processedDict = {}

for i in tqdm(messages):
    if(isinstance(i["text"],str) and any(t.isalpha() for t in i["text"])):
        isReliable, textBytesFound, details = cld2.detect(i["text"])
        if(details[0][1] == "en"):
            if "doge" in i["text"].lower().split() or "shib" in i["text"].lower().split():
                individualMessage = {}
                individualMessage["date"] = i["date"]
                individualMessage["text"] = i["text"]
                processedList.append(individualMessage)

processedDict["messages"] = processedList
with open("preprocessed.json", "w") as fileName:
    json.dump(processedDict,fileName,indent=4)