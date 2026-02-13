import pandas as pd
data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam'],
    "Age":[10,20,30],
    "City" : ['Nagpur', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)
# print(df)

df.to_csv("Output.csv", index=False)
with open("D:\Code\Python\PY_PANDAS\Output.csv")as f:
    output = f.read()

print(output)