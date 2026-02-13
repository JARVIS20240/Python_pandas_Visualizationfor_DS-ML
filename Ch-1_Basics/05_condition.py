import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30,29,40,25,32],
    "Salary": [50000, 60000,45000,52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}

"""
1- square brackets
2- boolean conditions
selecting columns
1- a series
2- dataframe multiple columns of data

column =df["Column Name"]
subset = df["Column1", "Column2","..."]

filtering rows
boolean indexing
#based on a single condition
filtered_Rows = df [df["Salary"] > 50000]
#combine multiple conditions
filtered_Rows =df[(df ["Salary'] > 50000) & (df ["Column2] < 80000)]
"""
df = pd.DataFrame(data)
age_and_salary = df[((df["Age"]> 30) & (df['Age'] < 50) & (df['Salary']> 50000))]
Filter_rows = df[df["Salary"]> 50000]
print(age_and_salary)

Subset = df[['Name','Age','Salary']]
print(Subset)