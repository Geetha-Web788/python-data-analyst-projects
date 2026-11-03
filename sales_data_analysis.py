
import pandas as pd

# Create sales data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Sales": [50000, 20000, 15000, 60000, 25000],
    "Quantity": [2, 3, 2, 1, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total revenue
df["Revenue"] = df["Sales"] * df["Quantity"]

# Display sales data
print("SALES DATA")
print(df)

# Total revenue
print("\nTotal Revenue:")
print(df["Revenue"].sum())

# Best selling product by revenue
print("\nProduct-wise Revenue:")
print(df.groupby("Product")["Revenue"].sum())

# Average sales
print("\nAverage Sales:")
print(df["Sales"].mean())

# Highest sale
print("\nHighest Sale:")
print(df["Sales"].max())
