import pandas as pd

# Customer purchase data
data = {
    "Customer": ["Anu", "Ravi", "Priya", "Kumar",
                 "Anu", "Ravi", "Priya", "Kumar",
                 "Anu", "Priya"],

    "Amount": [5000, 3000, 8000, 2000,
               4000, 2000, 6000, 3000,
               3000, 5000]
}

df = pd.DataFrame(data)

# Calculate customer spending
summary = df.groupby("Customer").agg(
    Total_Spending=("Amount", "sum"),
    Purchase_Count=("Amount", "count"),
    Average_Spending=("Amount", "mean")
).reset_index()

# Customer segmentation
def categorize(amount):
    if amount >= 10000:
        return "High"
    elif amount >= 5000:
        return "Medium"
    else:
        return "Low"

summary["Segment"] = summary["Total_Spending"].apply(categorize)

# Display results
print("CUSTOMER SEGMENTATION ANALYSIS")
print("--------------------------------")
print(summary)
