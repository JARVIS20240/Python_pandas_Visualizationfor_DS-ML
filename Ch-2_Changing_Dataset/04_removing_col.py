import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30,29,40,25,32],
    "Salary": [50000, 60000,45000,52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

df.insert(0,"Employee_ID", [10,20,30,40,50,60,70,80])
df.insert(3,"Bonus",df["Salary"] * 0.5)
print(df)

df.drop(columns=["Employee_ID"], inplace=True)
print(df)