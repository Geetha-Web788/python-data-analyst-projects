
import pandas as pd

# Customer purchase data
data = {
    "Customer": ["Anu", "Ravi", "Priya", "Kumar", "Anu", "Ravi"],
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet"],
    "Amount": [50000, 20000, 15000, 45000, 10000, 12000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display customer purchase details
print("CUSTOMER PURCHASE REPORT")
print(df)

# Total purchase amount
total = df["Amount"].sum()
print("\nTotal Purchase Amount:", total)

# Average purchase amount
average = df["Amount"].mean()
print("Average Purchase Amount:", average)

# Customer-wise spending
customer_spending = df.groupby("Customer")["Amount"].sum()

print("\nCustomer-wise Spending:")
print(customer_spending)

# Highest spending customer
print("\nHighest Spending Customer:")
print(customer_spending.idxmax())

# Product-wise sales
print("\nProduct-wise Sales:")
print(df.groupby("Product")["Amount"].sum())

# Sort purchases from highest to lowest
print("\nPurchase Ranking:")
print(df.sort_values(by="Amount", ascending=False))
