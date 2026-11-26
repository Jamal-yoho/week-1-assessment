import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([
    [80, 75, 90],
    [60, 70, 65],
    [85, 90, 95],
    [50, 55, 60]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)
print("Student Average:",np.mean(marks,axis=1))
print("Subject Average:",np.mean(marks,axis=0))

print("Grace Marks:")
print(marks+ 5)

weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)

print("Weighted Scores:", weighted_scores)

df = pd.read_csv("data/employees.csv")

df["salary"] = df["salary"].fillna(df["salary"].median())
df = df.drop_duplicates()
df["salary"] = df["salary"].astype(int)

print("After Cleaning:")
print(df)
print("Missing Values:")
print(df.isna().sum())
print("Duplicate Rows:", df.duplicated().sum())

print("Data Info:")
print(df.info())

print("Description:")
print(df.describe())

print("Using loc:")
print(df.loc[0:2])

print("Using iloc:")
print(df.iloc[0:3])

print("IT Employees:")
print(df[df["department"] == "IT"])

department = pd.read_csv("data/departments.csv")

print("Department Date:")
print(department)

print("Department Summary:")
print(df.groupby("department").agg({"name": "count", "salary": ["mean","max"]}))

inner_merge = pd.merge(df, department, on="department", how="inner")
left_merge = pd.merge(df, department, on="department", how="left")
Outer_merge = pd.merge(df, department, on="department", how="outer")

print("Inner Merge:",inner_merge.shape)
print("Left Merge: ", left_merge.shape)
print("Outer Merge:", Outer_merge.shape)

print("Department without employees:")
print("Inner Merge:")
print(inner_merge)

print("Left Merge:")
print(left_merge)

print("Outer Merge:")
print(Outer_merge)

print("Department without employees:")

for dept in department["department"]:
    found = False

    for emp_dept in df["department"]:
        if dept == emp_dept:
            found = True

    if found == False:
        print(dept)

dept_salary = df.groupby("department")["salary"].mean()

plt.figure()
plt.bar(dept_salary.index,dept_salary.values, label="Average Salary")
plt.title("Average Salaryby Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.savefig("reports/bar_chart.png")
plt.close()
print("Insight: IT has the highest average salary.")

plt.figure()
plt.hist(df["salary"], label= "Salary")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("reports/histogram.png")
plt.close()
print("Insight: Histogram shows employee salary distribution.")

plt.figure()
plt.scatter(df["id"], df["salary"], label= "Employee Salary")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("reports/scatter_chart.png")
plt.close()
print("Insight: Scatter chart compares employee IDs and salaries.")

plt.figure()
plt.plot(df["id"], df["salary"], marker="o", label="Salary Trend")
plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("reports/line_chart.png")
plt.close()
print("Insight: Line chart shows salary variation across employees.")

print("All 4 charts saved successfully.")