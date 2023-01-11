import yfinance as yf
from datetime import datetime

# Ticker symbol
stock_name = 'VOO'
stock = yf.Ticker(stock_name)

# Starting and ending dates
start_date = datetime(2021,1,1)
end_date = datetime(2022,12,31)

# Fetch historical prices
hist = stock.history(start=start_date, end=end_date)

# The amount of regular investment
investment = 1000

# The number of shares bought per investment
shares = 0

# The balance of the investment account
balance = 0

# Track the shares and balance over time
share_track = []
balance_track = []

# Fees in TWD and USD
fee_twd = 600
fee_usd = 25

for date, row in hist.iterrows():
    # Check if date is the first day of the month
    if date.day == 1:
        # Get the exchange rate
        rate = get_exchange_rate(date)
        # Calculate the number of shares bought with the investment after the fees
        shares += (investment-25-600*rate)/row["Open"]
        balance += investment-25-600*rate
        share_track.append(shares)
        balance_track.append(balance)
    # Reinvest dividends
    dividend = row["Dividends"]
    if dividend>0:
        shares += dividend/row["Open"]
        balance += dividend
        
# calculate the final total value
final_value = shares*row["Close"] + balance
print(f'Final total value from {stock_name} from {start_date} to {end_date} is ${final_value}')
