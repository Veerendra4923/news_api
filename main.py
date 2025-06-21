import requests
from send_mail import send_email

api_key = 'ab6983f6da7d4946a9eb2d1e6312b8fa'
url="https://newsapi.org/v2/everything?q=tesla&from=2025-05-21&sortBy=publishedAt&apiKey=ab6983f6da7d4946a9eb2d1e6312b8fa"
response = requests.get(url)
content=response.json()
body=""
for article in content['articles']:
    body=body+article['title']+"\n"+article['description']+"\n"+2*"\n"

body=body.encode('utf-8')
send_email(body)

