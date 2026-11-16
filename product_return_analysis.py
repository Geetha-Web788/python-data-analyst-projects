
# Product Return Analysis

products = {
    "Laptop": 10,
    "Mobile": 15,
    "Headphones": 5,
    "Keyboard": 8,
    "Mouse": 3
}

total_sold = 200

print("PRODUCT RETURN ANALYSIS")
print("-----------------------")

total_returns = sum(products.values())

print("Total Products Sold:", total_sold)
print("Total Products Returned:", total_returns)

print("\nProduct Return Report")

for product, returns in products.items():

    rate = (returns / total_sold) * 100

    print("\nProduct:", product)
    print("Returns:", returns)
    print("Return Rate:", round(rate, 2), "%")

    if returns >= 10:
        print("Status: High Returns")
    else:
        print("Status: Normal Returns")

highest = max(products, key=products.get)

print("\nProduct with Highest Returns:", highest)
print("Number of Returns:", products[highest])
