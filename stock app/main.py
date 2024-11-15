import requests
from config import STOCK_API_KEY, NEWS_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_PHONE_NUMBER, TWILIO_AUTH_TOKEN, MY_NUMBER
from twilio.rest import Client

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"
icon:str
diff_percent:float

# STEP 1: Use https://www.alphavantage.co
#When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_difference() -> bool:
    global icon, diff_percent
    parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()
    data_list = [value for (key,value) in data["Time Series (Daily)"].items()]
    yesterday_closing_price = float(data_list[0]["4. close"])
    day_before_yesterday_closing_price = float(data_list[1]["4. close"])
    difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
    diff_percent = (difference / yesterday_closing_price) * 100
    if diff_percent > 0:
        icon = "🔺"
    else:
        icon = "🔻"

    return diff_percent < -5 or diff_percent > 5



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def send_alert_message():
    global icon, diff_percent
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response =  requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    message_text = ""
    for article in articles:
        headline = article["title"]
        brief = article["description"]
        message_text += f"Headline: {headline}\nBrief:{brief}\n"

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
                    .create(
        body=f"""\n
        {COMPANY_NAME}: {icon}{diff_percent}%\n{message_text}
        """,
        from_=TWILIO_PHONE_NUMBER,
        to=MY_NUMBER
    )
    print(message.status)



if stock_difference():
    send_alert_message()
