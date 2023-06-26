import requests

api_key= "84ddf74fb1194df68664dab98aae09d9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-26&sortBy=publishedAt&apiKey=84ddf74fb1194df68664dab98aae09d9"
# Make request
requests = requests.get(url)

# Get the data
content = requests.json()
# Acess the article titles and description
for article in content["articles"]:
     print(article["title"])