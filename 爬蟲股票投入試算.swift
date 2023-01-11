import Foundation

let stockName = "VOO"
let startDate = DateComponents(calendar: .current, year: 2015, month: 1, day: 1).date
let endDate = DateComponents(calendar: .current, year: 2022, month: 12, day: 31).date
let investment = 1000.0
var shares = 0.0
var balance = 0.0
let feeTWD = 600.0
let feeUSD = 25.0

// Fetch historical prices
// Code to fetch historical prices goes here

for date in startDate...endDate {
    let dateComponents = Calendar.current.dateComponents([.day, .month, .year], from: date)
    guard let day = dateComponents.day, let month = dateComponents.month, let year = dateComponents.year else {
        continue
    }
    if day == 1 {
        let rate = 1/30
        let price = // Code to get the open price of VOO on this date goes here
        shares += (investment - feeUSD - feeTWD * rate) / price
        balance += investment - feeUSD - feeTWD * rate
    }
    // Code to get dividends goes here
}

let finalValue = shares * // Code to get the closing price of VOO on the last date goes here + balance
print("Final total value from \(stockName) from \(startDate) to \(endDate) is $\(finalValue)")
