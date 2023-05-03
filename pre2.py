from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_182078d6fbe086eaa15206b54e7054c52f176")


news = api.news_api(country = "in")

print(news)
for new in news['results']:
    print("##############################################################\n")
    print(str(new['title']), "\n\n")
  
    print("---------------------------------------")
    print(str(new['content']), "\n\n")
  