import json
from datetime import datetime #importing datetime module to format date strings
def main():
    userdate = getUserDate()
    stocks = createDictionary(userdate)
    user_prompt(stocks)


def getUserDate():    
    while True:
        user_input = input("Enter a date in YYYY-MM-DD format: ")
        try:
            dt = datetime.strptime(user_input, "%Y-%m-%d")
            formatted_date = dt.strftime("%B %d, %Y")
            print(f"You entered the date: {formatted_date}")
            return dt
        except ValueError:
            print("Invalid date format. Please try again.")

def createDictionary(userdate):
    print(userdate.strftime("%Y-%m-%d"))
    with open(f"stock_data_{userdate.strftime('%Y-%m-%d')}.json", "r") as fp:
        data = json.load(fp)
    stocks = {} #creating empty dictionary to store stock data

    for entry in data["data"]: #looping through each stock entry in the JSON data
        raw_date = entry["date"]
        dt = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S%z")
        formatted_date = dt.strftime("%B %d, %Y") #formatting date to be more readable

        stocks[entry["symbol"]] = {
            "symbol": entry["symbol"],
            "date": formatted_date,
            "open": entry["open"],
            "high": entry["high"],
            "low": entry["low"],
            "close": entry["close"],
            "volume": entry["volume"]
        }
    return stocks
def display_stock(stock):
    print(f"\nStock symbol: {stock['symbol']}")
    print(f"Date: {stock['date']}")
    print(f"Open price: ${stock['open']:.2f}")
    print(f"Close price: ${stock['close']:.2f}")

    change = stock["close"] - stock["open"] #calculating share value change in USD
    percent = (change / stock["open"]) * 100 #calculating percentage change

    if change > 0: #stock price went up
        print(f"The stock price went up by ${change:.2f} (+{percent:.3f}%).")
    elif change < 0: #stock price went down
        print(f"The stock price went down by ${abs(change):.2f} ({percent:.3f}%).")
    else: #stock price unchanged
        print("The stock price remained unchanged today.")



def user_prompt(stocks):
    loop = True
    while loop:
        user_input = input("Enter a stock symbol (AAPL, AMZN, MSFT, GOOGL) or 'exit' to quit: ").upper()

        if user_input == "EXIT": #checking for exit condition before anything else
            print("Exiting program. Goodbye!")
            loop = False
        elif user_input in stocks: #validating user input
            display_stock(stocks[user_input])
        else: #invalid stock symbol entered, user needs to input again
            print("Stock symbol not found. Please try again.")
main()