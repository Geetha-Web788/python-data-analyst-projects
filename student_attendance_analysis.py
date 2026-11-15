
# Student Attendance Analysis

students = {
    "Arun": 25,
    "Priya": 28,
    "Kumar": 20,
    "Divya": 30,
    "Meena": 24
}

total_days = 30

print("STUDENT ATTENDANCE ANALYSIS")
print("---------------------------")

total_attendance = sum(students.values())

print("Total Students:", len(students))
print("Total Attendance:", total_attendance)

print("\nIndividual Attendance Report")

for name, days in students.items():

    percentage = (days / total_days) * 100

    print("\nStudent:", name)
    print("Days Present:", days)
    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Eligible")
    else:
        print("Status: Low Attendance")
