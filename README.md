# Stock Investment Tracker

This is a tool to help track your stock investments and monitor their performance. With this tool, you can keep an eye on your investments, make informed decisions, and achieve your financial goals.

## Getting Started

1. Clone the repository and navigate to the directory:

    git clone https://github.com/<username>/stock-investment-tracker
    cd stock-investment-tracker

2. Install the required libraries:

    pip install -r requirements.txt

3. Run the script:

    python 爬蟲股票投入試算.py

## Usage

You can use this tool to track any stock that you have invested in by changing the ticker symbol in the script.
You can also change the start and end dates to match the dates of your investments.

The script uses the yfinance library to get the historical prices of the stock, and simulate an investment strategy of regular investments of a specified amount at the beginning of each month, taking into account the fees of a specified amount in USD and TWD using the function get_exchange_rate to get the exchange rate on a specific date.

The script also tracks the number of shares and balance over time, and reinvest dividends into the same ETF at the closing price of the day.

## Note

It's important to note that the function get_exchange_rate should be defined and implemented correctly to get the real-time exchange rate on that specific date, and this script assumes that historical data contains dividends, if not, you need to handle it properly.

It is also important to note that this script uses the historical data, so the result might not reflect the real situation since the value is based on past performance, and future performance may differ.
Also, it's important to check the API/ website's policy to avoid any unexpected issues.

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/my-new-feature)
5. Create a new Pull Request

## License

This project is licensed under the MIT License

## Acknowledgments

* Inspiration
* etc