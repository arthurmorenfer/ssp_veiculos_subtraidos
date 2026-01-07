#%%
from datetime import date
import pandas as pd
import requests


#This year file is to get current year and start decreasing years until we have a fail.
# I inserted -1 because we only have data from 2025 and before.
year_file = date.today().year -1
url_ssp_data = f"https://www.ssp.sp.gov.br/assets/estatistica/transparencia/baseDados/veiculosSub/VeiculosSubtraidos_{year_file}.xlsx"
local_filename_year = f'ssp_vehicles_stolen_file_{year_file}.xlsx'


response = requests.get(url_ssp_data)
if response.status_code == 200:
    with open(local_filename_year, 'wb') as f:
        f.write(response.content)
    print(f"File {local_filename_year} download successfully")
else:
    print(f"Failed to download file for this year: {year_file}. Status code: {response.status_code}")

