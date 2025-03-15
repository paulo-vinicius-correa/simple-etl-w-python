import os
import pandas as pd

# definindo variaveis para não depender de caminho absolutos
extract_data = os.getcwd()
folder_data = os.path.join(os.path.dirname(extract_data), 'data')
data = os.path.join(folder_data, 'Chocolate Sales.csv')

# lendo o csv
df_sales = pd.read_csv(data)

def clean_data (df_sales):
   # Criando uma copia do df
   df_sales_clean = df_sales.copy()
   # Preenchendo NaN com 0
   df_sales_clean = df_sales_clean.fillna(0)

   df_sales_clean.rename(columns={
    'Sales Person': 'sales_person',
    'Country': 'country',
    'Product':'product',
    'Date':'date',
    'Amount': 'amount',
    'Boxes Shipped' : 'boxes_shipped'
   }, inplace=True)

   print('Data Frame limpo e pronto para uso!')
   return df_sales_clean

clean_dataset = clean_data(df_sales)