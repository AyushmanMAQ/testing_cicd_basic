import requests

API_KEY = "your_api_key"  # Replace with your NewsAPI key
URL = "https://newsapi.org/v2/top-headlines"
PARAMS = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(URL, params=PARAMS)
if response.status_code == 200:
    news_data = response.json()
    for i, article in enumerate(news_data.get("articles", []), start=1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}\n")
else:
    print(f"Error fetching news: {response.status_code}")

#Hello Madan

# temporary changes in the python file
#now check
#ab check kar
#now check

#again check
