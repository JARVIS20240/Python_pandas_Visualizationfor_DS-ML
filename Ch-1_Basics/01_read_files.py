import pandas as pd

# df = pd.read_csv("D:\Code\Python\PY_PANDAS\Ch-1_Basics\sales_data_sample.csv", encoding="utf-8") -M> soluion for Encoding Error
# df = pd.read_csv("D:\Code\Python\PY_PANDAS\Ch-1_Basics\sales_data_sample.csv", encoding="latin1")
# df = pd.read_excel("D:\Code\Python\PY_PANDAS\Ch-1_Basics\SampleSuperstore.xlsx")
df = pd.read_json("D:\Code\Python\PY_PANDAS\Ch-1_Basics\sample_Data.json")
print(df)