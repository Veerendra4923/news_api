import requests
api_key = 'ab6983f6da7d4946a9eb2d1e6312b8fa'
url="https://newsapi.org/v2/everything?q=tesla&from=2025-05-21&sortBy=publishedAt&apiKey=ab6983f6da7d4946a9eb2d1e6312b8fa"
response = requests.get(url)
content=response.json()

for article in content['articles']:
    title=article['title']
    description=article['description']
    print(title,description)

