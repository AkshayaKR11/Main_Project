import pyttsx3
import requests
import json
import time

   
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)
  
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)
  
sound = engine.getProperty ('voices');
engine.setProperty('voice', 'sound[1].id')
  
  
from newsapi import NewsApiClient

api = NewsApiClient(api_key='4c6fd07fb18c436fb078d016002977f2')

news=api.get_top_headlines(sources='bbc-news')

print(news)

  
for new in news['articles']:
    print("##############################################################\n")
    print(str(new['title']), "\n\n")
    engine.say(str(new['title']))
    print('______________________________________________________\n')
  
    engine.runAndWait()
  
    print(str(new['description']), "\n\n")
    engine.say(str(new['description']))
    engine.runAndWait()
    print("..............................................................")
    time.sleep(2)