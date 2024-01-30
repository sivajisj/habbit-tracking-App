import math
from datetime import datetime, timedelta
from twilio.rest import Client
import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "1YCN9X8MBHIR7650"
NEWS_API_KEY= "5ba4e330a39d4f6b9751deab408cdc77"
ACCOUNT_SID = "AC02183d8d305c2c694344132b5b3ef716"
TWILIO_AUTH_TOKEN = "3402027f5380d8a415cdc7cc60e6fe29"
TWILIO_NUMBER = "+12053963189"
MY_NUMBER = "+917032891144"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Make the API request
response = requests.get(STOCK_ENDPOINT, params=stock_params)


# print(data)
# - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# print(yesterday_stock_price)

# Parse the JSON response
data = response.json()['Time Series (Daily)']

data_list = [val for (key,val) in data.items()]
# print(data_list)
# Get yesterday's date




# - Get the day before yesterday's closing stock price
yesterday_date = data_list[0]
day_before_yesterday_date = data_list[1]
# Get yesterday's closing stock price
yesterday_closing_price = yesterday_date["4. close"]
day_before_yesterday_closing_price = day_before_yesterday_date["4. close"]
print(f"yesterdays closing stock price: {yesterday_closing_price}")
print(f"day before yesterdays closing stock price: {day_before_yesterday_closing_price}")
#- Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# ercentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = math.floor((difference / float(yesterday_closing_price)) * 100)
print(diff_percentage)
# - Work out the p
# - If TODO4 percentage is greater than 5 then print("Get News").

if diff_percentage > 1:
    news_params = {
       "apikey":NEWS_API_KEY,
       "qInTitle": COMPANY_NAME,
    }
    #  - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    # print(articles)
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
    #. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    # print(template)
    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    #Optional TODO: Format the message like this:
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.status)


