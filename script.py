import xarray as xr
import pandas as pd

def example(file_name, variable):
    ds = xr.open_dataset(f"{file_name}.nc")
    tas_data = ds[variable]

    # Convert directly to pandas DataFrame
    df = tas_data.to_dataframe().reset_index()
    
    df.to_json(f"{file_name}.json", orient='records')
    

if __name__ == '__main__':
    example(file_name="tas_day_CESM2_piSST_r1i1p1f1_gn_00110101-00201231", variable='tas')