#%%
#Analysis on 2017 file
import pandas as pd
try:
    df = pd.read_excel('raw/ssp_vehicles_stolen_file_2025.xlsx', sheet_name='VEICULO_2025', engine='openpyxl')
    print(df)
except Exception as e:
    print(e)

