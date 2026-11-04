
import pandas as pd
import matplotlib.pyplot as plt

# Create Sales Data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones"],
    "Sales": [50000, 80000, 30000, 20000]
}

df = pd.DataFrame(data)

# Display Data
print("SALES DATA")
print(df)

# Total Sales
print("\nTotal Sales:", df["Sales"].sum())

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Sales"])
plt.title("Product Wise Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.show()

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%"
)
plt.title("Sales Distribution")
plt.show()

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df["Product"], df["Sales"], marker="o")
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.show()
