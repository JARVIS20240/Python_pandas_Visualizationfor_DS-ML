import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [29,34,32,30,29,32,29,32],
    "Salary": [50000, 60000,45000,52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

grouped = df.groupby(['Age','Name'])["Salary"].sum()
print(grouped)