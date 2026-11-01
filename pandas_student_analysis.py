import pandas as pd

# Student data
data = {
    "Name": ["Anu", "Ravi", "Priya", "Kumar"],
    "Maths": [85, 90, 75, 80],
    "Science": [90, 85, 80, 95],
    "English": [80, 75, 85, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Calculate average
df["Average"] = df["Total"] / 3

# Display results
print("STUDENT MARKS ANALYSIS")
print(df)

print("\nClass Average:", df["Average"].mean())
print("Highest Total:", df["Total"].max())
print("Lowest Total:", df["Total"].min())
