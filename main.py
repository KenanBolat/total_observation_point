import netCDF4 as nc
import xarray as xr
import numpy as np
import datetime
import os
import glob
from netCDF4 import num2date,date2num

process_path = r"/home/knn/Desktop/total_observation_point/nc_files"
script_start = datetime.datetime.now()


nc_files = [os.path.join(process_path, row ) for row in glob.glob1(os.path.join(process_path), "*.nc")]

tname = 'time'
all_dates = []
for nc_file in nc_files:
    print(nc_file, "is being done")
    ds = nc.Dataset(nc_file)
    t_unit = ds.variables[tname].units
    try:

        t_cal = ds.variables[tname].calendar

    except AttributeError:  # Attribute doesn't exist

        t_cal = u"gregorian"  # or
    dates = num2date(ds['time'], units=t_unit, calendar=t_cal)
    all_dates.extend(dates)

total_observation_point =str(np.max(all_dates) - np.min(all_dates))
print(total_observation_point)
script_end = datetime.datetime.now()
print("Script Start Time:  ", script_start, " Duration:", script_end-script_start)