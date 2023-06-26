import requests

from send_email import send_email

api_key = "84ddf74fb1194df68664dab98aae09d9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-26&sortBy=publishedAt&apiKey=84ddf74fb1194df68664dab98aae09d9&language=en"
# Make request
requests = requests.get(url)

# Get the data
content = requests.json()
# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    body = "Subject: Today's news"+body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
