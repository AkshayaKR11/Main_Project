from newsapi import NewsApiClient

api = NewsApiClient(api_key='4c6fd07fb18c436fb078d016002977f2')

news=api.get_top_headlines(country='us',category='sports')

print(news)
for new in news['articles']:
    print("##############################################################\n")
    print(str(new['title']), "\n\n")
    # engine.say(str(new['title']))
    print('______________________________________________________\n')
  
    # engine.runAndWait()
  
    print(str(new['description']), "\n\n")
    # engine.say(str(new['description']))
    # engine.runAndWait()
    print("..............................................................")
    # time.sleep(2)