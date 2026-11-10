
# Inventory Data Analysis Project

# Product Details
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"]

prices = [50000, 500, 1500, 12000, 2000]
stock = [10, 50, 30, 5, 8]

# 1. Total Number of Products
total_products = len(products)

# 2. Total Stock Quantity
total_stock = sum(stock)

# 3. Total Inventory Value
total_value = sum(
    prices[i] * stock[i] for i in range(len(products))
)

# 4. Highest Priced Product
highest_price = max(prices)
highest_product = products[prices.index(highest_price)]

# 5. Lowest Stock Product
lowest_stock = min(stock)
lowest_stock_product = products[stock.index(lowest_stock)]

# 6. Low Stock Products (Stock <= 10)
print("LOW STOCK PRODUCTS:")
for i in range(len(products)):
    if stock[i] <= 10:
        print(products[i], "-", stock[i])

# 7. Display Inventory Report
print("\nINVENTORY ANALYSIS REPORT")
print("-------------------------")

print("Total Products:", total_products)
print("Total Stock:", total_stock)
print("Total Inventory Value: Rs.", total_value)
print("Highest Priced Product:", highest_product)
print("Lowest Stock Product:", lowest_stock_product)

# 8. Category-wise Product Count
print("\nCATEGORY-WISE PRODUCT COUNT")

for category in set(categories):
    count = categories.count(category)
    print(category, ":", count)
