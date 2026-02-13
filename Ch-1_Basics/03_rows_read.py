import pandas as pd

df = pd.read_csv("D:\Code\Python\PY_PANDAS\Ch-1_Basics\sales_data_sample.csv", encoding="latin1")

print(df.isnull().mean()* 100)