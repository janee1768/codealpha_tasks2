# Stock Portfolio Tracker

# Creating pre-defined dictionary
stock_names = {"AAPL": 180, "TSLA": 250}

# Dictionary that stores user input
portfolio = {}

print("Welcome to Stock Portfolio Tracker!")

# Main loop
while True:
    stock = input("Enter stock name(e.g; AAPL)or type done to quit: ").upper().strip()
    if stock == "DONE":
        print("Good-bye!")
        break

    if stock not in stock_names:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity for the stock: "))
    # Add or Update stock quantity
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    # Calculating and Displaying total investment value
total_value = 0
print("\n Your Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_names[stock]  # Getting price from dictionary
    value = price * quantity  # Multiplying price and quantity
    total_value += value

    print(stock, ":", quantity, "shares x", price, "=", value)
print("\n Total Investment value: ", total_value)

# Storing the result in a .txt file
with open("stock_portfolio.txt", "w") as file:
    price = stock_names[stock]
    value = price * quantity
    file.write(
        stock + ":" + str(quantity) + "x $" + str(price) + "= $" + str(value) + "\n"
    )
    file.write("Total investment: $" + str(total_value))

# End of Stock Portfolio Tracker
