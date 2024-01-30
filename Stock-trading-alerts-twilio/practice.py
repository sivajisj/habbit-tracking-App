from datetime import datetime, timedelta

yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
print(yesterday_date)
