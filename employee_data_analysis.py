
import pandas as pd

# Employee Dataset
data = {
    "Employee": ["Anu", "Ravi", "Priya", "Kumar", "Divya", "Arun", "Meena"],
    "Department": ["HR", "IT", "IT", "Sales", "HR", "Sales", "IT"],
    "Salary": [25000, 45000, 50000, 30000, 28000, 35000, 55000],
    "Experience": [2, 5, 6, 3, 2, 4, 7]
}

# Create DataFrame
df = pd.DataFrame(data)

print("EMPLOYEE DATA")
print(df)

# 1. Total Employees
print("\nTotal Employees:", len(df))

# 2. Average Salary
print("Average Salary:", df["Salary"].mean())

# 3. Highest Paid Employee
highest = df.loc[df["Salary"].idxmax()]
print("\nHighest Paid Employee:")
print(highest)

# 4. Department-wise Average Salary
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())

# 5. Sort Employees by Salary
print("\nEmployees Sorted by Salary:")
print(df.sort_values(by="Salary", ascending=False))

# 6. Department-wise Employee Count
print("\nEmployees in Each Department:")
print(df["Department"].value_counts())

# 7. Save Analysis
df.to_csv("employee_analysis.csv", index=False)

print("\nEmployee Analysis Completed!")
