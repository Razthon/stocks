import os
import json
from datetime import datetime
from urllib.request import Request, urlopen
def grabDate():
    while True:
        user_input = input("Enter a date in YYYY-MM-DD format: ")
        try:
            dt = datetime.strptime(user_input, "%Y-%m-%d")
            formatted_date = dt.strftime("%B %d, %Y")
            print(f"You entered the date: {formatted_date}")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")

date = grabDate()
url = (f"https://api.marketstack.com/v2/eod/{date}?access_key=42c292b011064ee1beda036f86f446d6&symbols=AMZN,AAPL,MSFT,GOOGL")
with urlopen(url) as response: 
    source = response.read()
data = json.loads(source)
print(data)
#stock_data = open("stock_data{}", "w")     #rerunning this will overwrite, add a way for the script to create a unique file for each day
#current_date = datetime.now().strftime("%Y-%m-%d")
stock_data = open(f"stock_data_{date}.json", "w")     #rerunning this will overwrite, add a way for the script to create a unique file for each day
json.dump(data, stock_data, indent = 4)
stock_data.close()

#oijukoi jjjkuui

#hnjoiioikikjytgtl;;;;;;;;;;;;;;;;;;;o -Zelda