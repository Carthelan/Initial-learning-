import pandas as pd
from openpyxl import load_workbook

df = pd.read_excel(r'C:/Users/Klill/Downloads/BTC Margin with Fee.xlsx',sheet_name='Sheet1')
print(df)
