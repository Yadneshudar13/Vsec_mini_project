# Student Academic Performance Analysis System

# Importing required libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Creating folder for graphs
os.makedirs("graphs", exist_ok=True)

# Loading dataset
df = pd.read_csv("StudentsPerformance.csv")

# Displaying first five records
print("Dataset Loaded Successfully!")

print(df.head())

# Data Cleaning

# Removing duplicate records
df = df.drop_duplicates()

# Renaming columns
df.columns = [
    "Gender",
    "Ethnicity",
    "Parental_Education",
    "Lunch",
    "Test_Preparation",
    "Math",
    "Reading",
    "Writing"
]

# Checking missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Replacing missing numerical values with average
subjects = ["Math", "Reading", "Writing"]

for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")
    df[subject] = df[subject].fillna(df[subject].mean())

# Calculating total marks
df["Total"] = df[subjects].sum(axis=1)

# Calculating average percentage
df["Percentage"] = df[subjects].mean(axis=1)

# Assigning grades

def calculate_grade(per):

    if per >= 90:
        return "A+"

    elif per >= 80:
        return "A"

    elif per >= 70:
        return "B"

    elif per >= 60:
        return "C"

    elif per >= 40:
        return "D"

    else:
        return "Fail"


df["Grade"] = df["Percentage"].apply(calculate_grade)

print("\nData Cleaning Completed!")

# Display Student Records

def view_dataset():

    print("\nSTUDENT RECORDS\n")

    print(df.head(20))


# Display Dataset Information

def dataset_info():

    print("\nDATASET INFORMATION")

    print("\nTotal Rows:", df.shape[0])

    print("Total Columns:", df.shape[1])

    print("\nColumn Names:")

    print(df.columns.tolist())

    print("\nData Types:")

    print(df.dtypes)

# Statistical Analysis

def statistical_analysis():

    print("\nSTATISTICAL ANALYSIS")

    print("\nMean Marks:")

    print(df[subjects].mean())

    print("\nMedian Marks:")

    print(df[subjects].median())

    print("\nMaximum Marks:")

    print(df[subjects].max())

    print("\nMinimum Marks:")

    print(df[subjects].min())

    print("\nStandard Deviation:")

    print(df[subjects].std())

    print("\nOverall Class Average:")

    print(np.mean(df["Percentage"]))

# Student Performance Analysis

def performance_analysis():

    print("\nSTUDENT PERFORMANCE")

    print(df[["Total", "Percentage", "Grade"]].head(20))


# Top 10 Students

def topper_analysis():

    print("\nTOP 10 STUDENTS")

    top_students = df.sort_values(
        by="Percentage",
        ascending=False
    )

    print(
        top_students[
            ["Gender", "Math", "Reading",
             "Writing", "Percentage", "Grade"]
        ].head(10)
    )

    print("\nHighest Percentage:")

    print(top_students.iloc[0]["Percentage"])

# Subject-wise Analysis

def subject_analysis():

    print("\nSUBJECT-WISE AVERAGE")

    average = df[subjects].mean()

    print(average)

    print("\nBest Performing Subject:")

    print(average.idxmax())

    print("\nLowest Performing Subject:")

    print(average.idxmin())


# Gender-wise Analysis

def gender_analysis():

    print("\nGENDER-WISE PERFORMANCE")

    result = df.groupby("Gender")[subjects].mean()

    print(result)

# 1. Subject Average Bar Chart

def bar_chart():

    average = df[subjects].mean()

    plt.figure(figsize=(8, 5))

    plt.bar(average.index, average.values)

    plt.title("Average Marks by Subject")

    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    plt.savefig("graphs/bar_chart.png")

    plt.show()


# 2. Grade Distribution Pie Chart

def pie_chart():

    grades = df["Grade"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        grades.values,
        labels=grades.index,
        autopct="%1.1f%%"
    )

    plt.title("Student Grade Distribution")

    plt.savefig("graphs/pie_chart.png")

    plt.show()


# 3. Percentage Distribution Histogram

def histogram():

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Percentage"],
        bins=10,
        edgecolor="black"
    )

    plt.title("Student Percentage Distribution")

    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")

    plt.savefig("graphs/histogram.png")

    plt.show()


# 4. Subject Correlation Heatmap

def heatmap():

    correlation = df[subjects].corr()

    plt.figure(figsize=(7, 5))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Subject Marks Correlation")

    plt.savefig("graphs/heatmap.png")

    plt.show()

# Export Student Performance Report

def export_report():

    report = df[
        ["Gender", "Math", "Reading",
         "Writing", "Total", "Percentage", "Grade"]
    ]

    report.to_csv(
        "Student_Performance_Report.csv",
        index=False
    )

    print("\nReport Exported Successfully!")

    print("File: Student_Performance_Report.csv")

# Main Menu

while True:

    print("\n====================================")

    print(" STUDENT PERFORMANCE ANALYSIS SYSTEM")

    print("====================================")

    print("1. View Student Records")

    print("2. Dataset Information")

    print("3. Statistical Analysis")

    print("4. Student Performance Analysis")

    print("5. Top 10 Students")

    print("6. Subject-wise Analysis")

    print("7. Gender-wise Analysis")

    print("8. Subject Average Bar Chart")

    print("9. Grade Distribution Pie Chart")

    print("10. Percentage Histogram")

    print("11. Subject Correlation Heatmap")

    print("12. Export Performance Report")

    print("13. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        view_dataset()

    elif choice == "2":
        dataset_info()

    elif choice == "3":
        statistical_analysis()

    elif choice == "4":
        performance_analysis()

    elif choice == "5":
        topper_analysis()

    elif choice == "6":
        subject_analysis()

    elif choice == "7":
        gender_analysis()

    elif choice == "8":
        bar_chart()

    elif choice == "9":
        pie_chart()

    elif choice == "10":
        histogram()

    elif choice == "11":
        heatmap()

    elif choice == "12":
        export_report()

    elif choice == "13":
        print("\nThank You for Using the System!")

        break

    else:
        print("\nInvalid Choice! Please Try Again.")