from netCDF4 import Dataset
import numpy as np

def save_netcdf(path, data, lat, lon, var_name="DOC"):
    ds = Dataset(path, "w", format="NETCDF4_CLASSIC")

    ds.createDimension("y", len(lat))
    ds.createDimension("x", len(lon))

    latitudes = ds.createVariable("lat", np.float32, ("y",))
    longitudes = ds.createVariable("lon", np.float32, ("x",))
    var = ds.createVariable(var_name, np.float32, ("y", "x"))

    latitudes[:] = lat
    longitudes[:] = lon
    var[:, :] = data

    latitudes.units = "degrees_north"
    longitudes.units = "degrees_east"
    var.units = "mg m-3"

    ds.close()
