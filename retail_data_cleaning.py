import pandas as pd

# Retail Data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", None],
    "Price": [50000, 20000, 15000, 50000, None, 10000],
    "Quantity": [2, 3, 1, 2, 4, 2]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Find missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing values
df["Product"] = df["Product"].fillna("Unknown")
df["Price"] = df["Price"].fillna(df["Price"].mean())

print("\nCleaned Data:")
print(df)

# Total Sales
df["Total"] = df["Price"] * df["Quantity"]

print("\nFinal Retail Analysis:")
print(df)

print("\nTotal Revenue:", df["Total"].sum())

# Save cleaned data
df.to_csv("cleaned_retail_data.csv", index=False)
