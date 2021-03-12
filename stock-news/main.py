import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ""
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = ""
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "apikey": NEWS_KEY
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.


stock_response = requests.get(STOCK_ENDPOINT, STOCK_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday = str(date.today() - timedelta(days=1))
closing_yesterday = stock_data["Time Series (Daily)"][yesterday]["4. close"]
day_before = str(date.today() - timedelta(days=2))
closing_day_before = stock_data["Time Series (Daily)"][day_before]["4. close"]
diff = float(closing_yesterday) - float(closing_day_before)
diff_percent = round((diff / float(closing_yesterday)) * 100)

tendence = None
if diff > 0:
    tendence = f"{COMPANY_NAME}: 🔼{abs(diff_percent)}%"
else:
    tendence = f"{COMPANY_NAME}: 🔽{abs(diff_percent)}%"

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

if abs(diff_percent) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    news = "".join([f"headline: {article['title']}\nbrief: {article['description']}\n" for article in news_data])

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    # HINT 1: Consider using a List Comprehension.

    client = Client(account_sid="", auth_token="")
    message = client.messages \
        .create(
        body=f"{tendence}\n{news}",
        from_='',
        to=''
    )
    print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
