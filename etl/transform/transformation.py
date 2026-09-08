#%%
import pandas as pd
from datetime import date 
def read_file_transform_csv(file_name_input: str, year_input: int) -> str:
    print(file_name_input)
    try: 
        df_raw = pd.read_excel(file_name_input, sheet_name=f'VEICULO_{year_input}', dtype=object)
        print(df_raw)
        file_name_input.replace('.xlsx','.csv')
        df_raw.to_csv(file_name_input, encoding='utf-8')
        return 'success'
    except Exception as e: 
        print(e)
        if str(e).find(f"Worksheet named VEICULO_{year_input} not found"):
            print("check")
            try:
                df_raw = pd.read_excel(file_name_input, sheet_name=f'VEICULOS_{year_input}', dtype=object)
                print(df_raw)
                file_name_input.replace('.xlsx','.csv')
                print(file_name_input)
                df_raw.to_csv(file_name_input, encoding='utf-8')
                return 'success'
            except Exception as e:
                return print(e)
        return print(e)

year_file = date.today().year -1
while read_file_transform_csv(f'raw/ssp_vehicles_stolen_file_{year_file}.xlsx', year_file) == 'success':
    year_file = year_file - 1



#%%
import duckdb as dudb
from datetime import date
from pathlib import Path

current_file = Path(__file__).resolve()
root_dir = current_file.parents[2]
raw_folder_path = root_dir / "raw"
parquet_folder_path = root_dir / "parquet"
def read_file_transform_parquet(file_name_input: str, year_input: int) -> str:
    print(file_name_input)
    parquet_file = parquet_folder_path / file_name_input
    try:
        df_excel = dudb.sql(f"COPY(select * from read_xlsx({file_name_input}, sheet='VEICULO_{year_input}') TO '{parquet_file}.parquet' (FORMAT parquet);")
        return 'success'
    except Exception as e:
        print(e)
        if str(e).find(f"Worksheet named VEICULO_{year_input} not found"):
            try:
                df_excel = dudb.sql(f"COPY(select * from read_xlsx({file_name_input}, sheet='VEICULOS_{year_input}') TO '{parquet_file}.parquet' (FORMAT parquet);")
                return 'success'
            except Exception as e:
                return print(e)
        return print(e)

year_file = date.today().year -1
while read_file_transform_parquet(f'{raw_folder_path}/ssp_vehicles_stolen_file{year_file}.xlsx', year_file) == 'success':
    year_file = year_file - 1

