import numpy as np
import pandas as pd
import tensorflow as tf

class DOCModel:

    def __init__(self, model_path, scaler):
        self.model = tf.keras.models.load_model(model_path)
        self.scaler = scaler

    def predict(self, df, predictors):
        df_clean = df.dropna()
    
        if df_clean.empty:
            return np.full(len(df), np.nan)
    
        X = self.scaler.transform(df_clean[predictors])

        if len(self.model.input_shape) == 3:
            X = X.reshape((X.shape[0], 1, X.shape[1]))

        y_pred = np.squeeze(self.model.predict(X))
    
        result = pd.Series(np.nan, index=df.index)
        result.loc[df_clean.index] = y_pred

        return result.values
