import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age" : [28,34,22,30,29,40,25,32],
    "Salary": [50000, 60000,45000,52000, 49000, 70000,48000, 58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)

# # .loc[]
# # df.loc[row_index, "column_name"] = New Data
# df.loc[2,'Salary']= 100000
# Ghanshyam_data = df[df['Name'] == 'Ghanshyam']
# print(Ghanshyam_data)

# df.loc[df['Name'] == "Shyam", 'Age'] = 50
# print(df)

df = df.set_index('Name')
print(df)
# df.loc['Ghanshyam', 'Salary']=150000
# print(df.loc['Ghanshyam'])


df.iloc[2,0]=100
print(df)
print(df.iloc[2])

