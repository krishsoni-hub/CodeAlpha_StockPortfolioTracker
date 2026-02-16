=> Code <=


# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    value = stock_prices[stock] * quantity
    total_investment += value

    print(f"✅ {stock} investment value: ₹{value}")

print("\n💰 Total Investment Value: ₹", total_investment)

# Optional: save result to a file
save = input("Do you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value: ₹{total_investment}")
    print("📁 Saved to portfolio.txt")


=> Description <=

The Stock Portfolio Tracker is a simple Python-based console application designed to help users calculate their stock investments.
The program uses predefined stock prices (AAPL, TSLA, GOOG, MSFT) and allows users to enter the stock name along with the quantity they wish to purchase.
It automatically calculates the investment value for each stock and displays the total portfolio value at the end.
Additionally, the program provides an option to save the final investment summary to a text file (portfolio.txt).

This project demonstrates practical implementation of core Python concepts such as dictionaries, loops, conditional statements, user input handling, and file handling.


=> Key features <=

> Supports multiple stock entries
> Real-time investment calculation
> Input validation for unavailable stocks
> Option to save results to a file
> Simple and user-friendly console interface
