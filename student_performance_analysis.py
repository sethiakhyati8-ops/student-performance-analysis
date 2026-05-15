# Student Performance Analysis
# Tools: Python, NumPy, Pandas
# Goal: Identify top performers, at-risk students,
#        and key performance drivers

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Student performance dataset
df = pd.DataFrame({
    "name": [
        "Aarav", "Priya", "Rohan", "Sneha", "Vikram",
        "Anita", "Karan", "Divya", "Arjun", "Meera",
        "Sahil", "Pooja", "Nikhil", "Tanya", "Rahul",
        "Ishaan", "Kavya", "Manav", "Riya", "Aditya"
    ],
    "gender": [
        "M", "F", "M", "F", "M",
        "F", "M", "F", "M", "F",
        "M", "F", "M", "F", "M",
        "M", "F", "M", "F", "M"
    ],
    "study_hours": [2, 6, 1, 7, 3, 5, 2, 8, 4, 6,
                    1, 7, 3, 5, 4, 6, 8, 2, 7, 3],
    "math":    [55, 82, 40, 91, 63, 78, 48, 95, 70, 85,
                38, 88, 60, 76, 72, 80, 93, 45, 89, 58],
    "english": [60, 79, 45, 88, 58, 82, 52, 90, 65, 87,
                42, 85, 63, 80, 68, 75, 91, 50, 84, 62],
    "science": [58, 85, 42, 93, 60, 80, 50, 92, 68, 83,
                40, 87, 62, 78, 70, 82, 94, 48, 86, 55],
    "attendance": [72, 91, 65, 95, 78, 88, 70, 97, 82, 92,
                   60, 94, 75, 89, 83, 90, 96, 68, 93, 74]
})
#Average score
df["total"]=df["math"]+df["english"]+df["science"]
df["average"]=np.round(df["total"]/3,1)
top5=df.sort_values("average", ascending=False)
print(top5[["name", "math", "english", "science", "average"]].head(5))

#pass or fail
df["result"]="Fail"
df.loc[(df["average"] >= 50) & (df["attendance"] >=75), "result"]="Pass"
print(df["result"].value_counts())
print(df[["name", "average", "attendance", "result"]])

# gender analysis
print(df.groupby("gender")[["math", "english", "science"]].mean())

#study hours vs performance
high = df[df["study_hours"] >= 5]["average"].mean()
low  = df[df["study_hours"] < 5]["average"].mean()
print(f"5+ study hours average : {high.round(1)}")
print(f"Under 5 hours average  : {low.round(1)}")

# students at risk
condition = (df["attendance"] < 75) & (df["average"] < 60)
c=df[condition]
print(c[["name","attendance", "average"]])

# =====================
# CHART 1 - Scatter plot
# study hours vs average 
# =====================
plt.figure(figsize=(7, 5))
plt.scatter(df["study_hours"], df["average"],
            color="purple", s=80)          # s = dot ka size

# Har point pe student ka naam likhenge
for i, row in df.iterrows():
    plt.annotate(row["name"],
                 (row["study_hours"], row["average"]),
                 fontsize=7, ha="left")

plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Score")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter.png")
plt.show()

# =====================
# CHART 2 - Histogram
# score distribution
# =====================
plt.figure(figsize=(7, 5))
plt.hist(df["average"], bins=6, color="steelblue", edgecolor="white")
plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# =====================
# CHART 3 - Heatmap (Seaborn)
# math, english, science and attendance correlation
# =====================
plt.figure(figsize=(6, 5))
corr = df[["math", "english", "science",
           "study_hours", "attendance"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f",
            cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()
