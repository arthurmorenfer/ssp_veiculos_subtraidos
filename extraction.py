#%%
from datetime import date
import pandas as pd
import requests


#This year file is to get current year and start decreasing years until we have a fail.
#I inserted -1 because we only have data from 2025 and before.

def get_file_from_ssp (year_input: int) -> str:
    url_ssp_data = f"https://www.ssp.sp.gov.br/assets/estatistica/transparencia/baseDados/veiculosSub/VeiculosSubtraidos_{year_input}.xlsx"
    response = requests.get(url_ssp_data)
    save_filename_year = f'ssp_vehicles_stolen_file_{year_input}.xlsx'
    if response.status_code == 200:
        with open(f'raw/{save_filename_year}', 'wb') as f:
            f.write(response.content)
        print(f"File {save_filename_year} download successfully")
        return response.status_code
    else:
        print(f"Failed to download file for this year: {year_input}. Status code: {response.status_code}")
        return response.status_code

year_file = date.today().year -1
while get_file_from_ssp(year_file) == 200:
    year_file = year_file - 1
