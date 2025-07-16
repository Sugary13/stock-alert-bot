from dotenv import load_dotenv
import os
import requests
import twilio.rest

AVA_Endpoint = "https://www.alphavantage.co/query?"
NEWS_Endpoint = "https://newsapi.org/v2/everything"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

ava_api_key = os.getenv("AVA_API_KEY")
new_api_key = os.getenv("NEW_API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
messaging_service_id = os.getenv("MESSAGING_SERVICE_ID")
phone_number = os.getenv("PHONE_NUMBER")


ava_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ava_api_key,
}


response = requests.get(AVA_Endpoint, params=ava_params)
response.raise_for_status()

data = response.json()

time_series = data["Time Series (Daily)"]
dates = list(time_series.keys())
latest = time_series[dates[0]]
previous = time_series[dates[1]]

latest_close = float(latest["4. close"])
previous_close = float(previous["4. close"])

change_percent = ((latest_close - previous_close) / previous_close) * 100
print(f"📈 Cambio: {change_percent:.2f}%")


def get_news():
    news_params = {
        'apiKey': new_api_key,
        'qInTitle': COMPANY_NAME,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 3,
    }
    news_response = requests.get(NEWS_Endpoint, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    for article in articles:
        print(f"\n📰 {article['title']}\n{article['description']}\n{article['url']}\n")
        send_sms(article)


def send_sms(article):
    client = twilio.rest.Client(account_sid, auth_token)
    title = article["title"]
    description = article["description"]
    url = article["url"]
    message_body = f"📈 Cambio: {change_percent:.2f}%\n📰 {title}\n{description}\n{url}"

    message = client.messages.create(
        messaging_service_sid=messaging_service_id,
        body=message_body,
        to=phone_number
    )
    print(f"Mensaje enviado: {message.status}")


if change_percent > 5:
    print("🚀 La acción subió más de 5%")
    get_news()

elif change_percent < -5:
    print("📉 La acción bajó más de 5%")
    get_news()
else:
    print("📊 Cambio moderado.")
