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
            X = np.expand_dims(X, axis=1)

        y_pred = np.squeeze(self.model.predict(X))
        
        result = np.full(len(df), np.nan)
        result[df_clean.index] = y_pred

        return result
