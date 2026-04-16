import pandas as pd
from doc_model.data.netcdf import load_variable, flatten_map, reshape_map

def run_inference(file_paths, predictors, model):

    arrays = []
    for path in file_paths:
        data, lat, lon = load_variable(path)
        arrays.append(flatten_map(data))

    df = pd.DataFrame(dict(zip(predictors, arrays)))
    shape = data.shape

    pred = model.predict(df, predictors)
    pred_map = reshape_map(pred, shape)

    return pred_map, lat, lon
