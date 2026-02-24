#%%
#Analysis on 2017 file
import pandas as pd
try:
    df = pd.read_excel('raw/ssp_vehicles_stolen_file_2025.xlsx', sheet_name='VEICULOS_2025', engine='openpyxl')
    print(df)
except Exception as e:
    print(e)


#%%
import duckdb
df_test = duckdb.sql("select * from read_xlsx('./raw/ssp_vehicles_stolen_file_2025.xlsx',sheet='VEICULOS_2025',all_varchar=true)")

print(df_test)