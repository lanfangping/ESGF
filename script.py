import xarray as xr

# Load the dataset
ds = xr.open_dataset("tas_day_CESM2_piSST_r1i1p1f1_gn_00110101-00201231.nc")

# Overview of the dataset
print(ds)

# List variables (e.g., 'tas', 'pr', 'psl', etc.)
print(ds.data_vars)

# Access a variable
tas = ds['tas']  # for example, surface air temperature

# See dimensions
print(tas.dims)

# # Look at data values
# print(tas.values)


# from netCDF4 import Dataset

# # Open file
# ds = Dataset('tas_day_CESM2_piSST_r1i1p1f1_gn_00110101-00201231.nc', 'r')
# print(ds)

# # List variables
# print(ds.variables.keys())

# # Access variable data
# temperature = ds.variables['lat_bnds'][:]
# print(temperature.shape)