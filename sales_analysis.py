
products = ["Laptop", "Mobile", "Tablet", "Headphones"]

sales = [50000, 30000, 20000, 10000]

total_sales = sum(sales)

average_sales = total_sales / len(sales)

highest_sales = max(sales)

print("SALES ANALYSIS")

print("Total Sales:", total_sales)

print("Average Sales:", average_sales)

print("Highest Sales:", highest_sales)

print("Highest Selling Product:",
      products[sales.index(highest_sales)])
