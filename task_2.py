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
