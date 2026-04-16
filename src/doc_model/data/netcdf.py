from netCDF4 import Dataset
import numpy as np

def load_variable(path):
    ds = Dataset(path)
    keys = list(ds.variables.keys())
    data = np.array(ds.variables[keys[2]][:])
    lat = np.array(ds.variables[keys[0]][:])
    lon = np.array(ds.variables[keys[1]][:])
    ds.close()
    return data, lat, lon

def flatten_map(data):
    return data.reshape(-1)

def reshape_map(vector, shape):
    return vector.reshape(shape)
