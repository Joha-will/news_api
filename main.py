import requests


def get_news(topic, from_date, to_date, language='en', api_key='api'):

  results = []
  url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
  re = requests.get(url)
  content = re.json()
  articles = content['articles']

  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results



print(get_news(topic='space', from_date='2022-2-27', to_date='2022-2-28'))