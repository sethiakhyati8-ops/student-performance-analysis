# Student Performance Analysis
# Tools: Python, NumPy, Pandas
# Goal: Identify top performers, at-risk students,
#        and key performance drivers

import numpy as np
import pandas as pd

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